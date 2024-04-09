from django.contrib.auth.models import User as UserAuth

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import ChatSerializer, UserSerializer
from .models import User, Step, Log

@api_view(['POST'])
def chat_view(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        session_id = serializer.validated_data['session_id']
        user_input = serializer.validated_data['user_input']

        try:
            user = User.objects.get(session_id=session_id)
        except User.DoesNotExist:
            user = User.objects.create(session_id=session_id, current_state=Step.get_initial_state())

        current_state = user.current_state
        step = Step.objects.create(state=current_state, input=user_input)
        response_message, next_state  = step.get_next_state(user_input)

        if next_state:
            user.current_state = next_state
            step = Step.objects.create(state=next_state, input=user_input)
            Log.objects.create(user=user, response=user_input)
        else:
            response_message = 'Invalid input'

        user.save()
        step.response_message = response_message
        step.save()

        return Response({'response_message': response_message})
    else:
        return Response(serializer.errors, status=400)
    

# Bonus User Auth
class CreateUserView(generics.CreateAPIView):
    queryset = UserAuth.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]