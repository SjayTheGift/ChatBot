from django.test import  TestCase, Client
from django.urls import reverse
from .models import Step, User

class StepTestCase(TestCase):
    def test_initial_state(self):
        initial_state = Step.get_initial_state()
        self.assertEqual(initial_state, 'initial_state')

    def test_greeting_state(self):
        step = Step(state='initial_state', input='hi')
        response_message, next_state = step.get_next_state(step.input)
        self.assertEqual(response_message, 'Hello! How can I assist you?')
        self.assertEqual(next_state, 'greeting')


    def test_question_state(self):
        step = Step(state='greeting', input='answer')
        response_message, next_state = step.get_next_state(step.input)
        self.assertEqual(response_message, 'How can I help you?')
        self.assertEqual(next_state, 'question')


    def test_end_state(self):
        step = Step(state='question', input='bye')
        response_message, next_state = step.get_next_state(step.input)
        self.assertEqual(response_message, 'Thank you for using the chatbot. Have a great day!')
        self.assertEqual(next_state, 'end')


class ChatAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chat_endpoint(self):
        # Create a user and a step for testing
        user = User.objects.create(session_id='abc123', current_state='greeting')
        step = Step.objects.create(state='greeting', input='hi', response_message='Hello! How can I assist you?')

        # Define the URL for the chat endpoint
        url = reverse('chat')
        # Set up the POST request data
        data = {
            "session_id": user.session_id,
            "user_input": step.input
        }
        # Make a POST request to the chat endpoint
        response = self.client.post(url, data)

        # Check the response status code
        self.assertEqual(response.status_code, 200)
        self.assertEqual(step.response_message, 'Hello! How can I assist you?')


        #Next Step Question step
        response_message, next_state = step.get_next_state(data["user_input"])
        
        url = reverse('chat')
        data = {
            "session_id": user.session_id,
            "user_input": "can you please help me code?"
        }
        response = self.client.post(url, data)
        # Check the response status code
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_message, 'How can I help you?')
        self.assertEqual(next_state, 'question')
