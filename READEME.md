# Chat Bot

Django application using Django REST Framework that functions as a state machine chatbot. The application interact with users via a single API endpoint, managing their state and guiding them through a conversation.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Tests](#tests)

## Prerequisites

- Python 3.x
- Django (version X.X.X or above)
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:``` git clone https://github.com/your-username/project-name.git ```
2. Open terminal or cmd and go to file location where project cloned.
3. Run command ``` python -m venv venv ``` to create virtual environment.
4. Use the requirements file to get all dependencies.
5. Run command ```pip install -r requirements.txt ```
6. Run command ``` python manage.py migrate ``` to create all models.
7. Run command ``` python manage.py createsuperuser ``` to create super user.
8. Run  command ``` python manage.py runserver ``` to runserver.
9. Click on ``` http://127.0.0.1:8000/ ``` to visit the app on browser.

## Usage

The API provides the following endpoints for interacting with the chat application: ``` http://127.0.0.1:8000/chat/ ```

###### Create a Session 
To create a new user session, send a POST request to ```http://127.0.0.1:8000/chat/ ``` with the following JSON payload:

``` shell
{
    "session_id": "your-session-id",
    "user_input": "your- message"
}
```
This will be used to create the user session and also send an input to the api then chatbot will respond with a message based on the api. 

## API Documentation

The API provides the following endpoint for interacting with the chat application:

``` shell
- Endpoint: `/chat/`
- Method: POST
- Description: Creates a new user session and send message to chatbot.
- Request Body:

{
    "session_id": "your-session-id",
    "user_input": "your- message"
}
```

* Example cURL request:

``` shell
curl -X POST -H "Content-Type: application/json" -d '{
    "session_id": "your-session-id",
    "user_input": "your- message"
}' http://localhost:8000/chat/

```

Your will send the message with the session id then the chatbot will respond base on the message sent if the user send invalid data the chatbot will respond with a message telling the user the input is invalid.

## Test

To run our test to see if the api works be use the following, hope that coverage will be installed using requirement.txt file if not please use ``` pip install coverage ```    

The run the following commands, you can copy and paste them
``` shell
1. coverage run manage.py test 
2. coverage report
```