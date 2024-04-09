from django.db import models

class User(models.Model):
    session_id = models.CharField(max_length=255)
    current_state = models.CharField(max_length=255)

    def __str__(self):
        return self.session_id


class Step(models.Model):
    # STATE_CHOICES = [
    #     ('greeting', 'Welcome! How can I assist you?'),
    #     ('question', 'What is your question?'),
    #     ('end', 'Thank you for using the chatbot. Have a great day!'),
    # ]

    state = models.CharField(max_length=255)
    input = models.CharField(max_length=100)
    response_message = models.TextField()

    def __str__(self):
        return self.state

    @staticmethod
    def get_initial_state():
        return 'initial_state'

    def get_next_state(self, user_input):
        if self.state == self.get_initial_state():
            if user_input.lower() in ['hi', 'hello']:
                self.response_message = 'Hello! How can I assist you?'
                next_state = 'greeting'
        elif self.state == 'greeting':
                self.response_message = 'How can I help you?'
                next_state = 'question'
        elif self.state == 'question':
                self.response_message = 'Thank you for using the chatbot. Have a great day!'
                next_state = 'end'
        else:
             next_state = ''
        
        return self.response_message, next_state    

    def generate_response_message(self):
        return self.response_message
    
class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} response {self.response}'

