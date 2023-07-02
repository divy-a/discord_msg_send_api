import json
from flask import Flask, request
from message_sender_v2 import send_message
import traceback

app = Flask(__name__)


@app.route('/')
def index():
    return 'API'


@app.route('/send_message', methods=['POST'])
def send_msg():
    try:
        data = request.get_json()
        message = data['msg']
        send_message(message)
        return {'message': 'Message sent successfully.'}
    except Exception as e:
        return {'message': 'Failed to send message.', 'error': traceback.format_exc}, 400


if __name__ == '__main__':
    app.run()
