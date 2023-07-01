import json
from flask import Flask, request
from message_sender_v2 import send_message

app = Flask(__name__)


@app.route('/')
def index():
    return 'API'


@app.route('/send_message', methods=['POST'])
def send_msg():
    try:
        data = request.get_json()
        if 'msg' in data and isinstance(data['msg'], str):
            message = data['msg']
            send_message(message)
            return {'message': 'Message sent successfully.'}
        else:
            return {'message': 'Invalid data format. "msg" field must be a string.'}, 400
    except Exception as e:
        return {'message': 'Bad request.', 'error': str(e)}, 400


if __name__ == '__main__':
    app.run()
