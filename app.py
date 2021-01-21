import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import utils 

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ZHI/OgIUx7IsyImXYg+9X6ANFG47iHuiaj6/Fn8da5cyYwPTTuGh91Egg8vvHre2k9eofGf5fuF5qhOhLklgLRg3x9xYAjQn/0FDw5j355vgPAtoT5gIxGRanTESEVBjv7mWI+IeY6oUd/LLTcU1+AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0dcfb97e623da9942a3acb6b86e0e9a1')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(401)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text.strip()
    
    if input_text in ['education', 'background']:
        text = utils.get_education()
    elif input_text in ['cmlab', 'lab']:
        text = utils.get_lab_msg()
    elif input_text == 'intern':
        text = utils.get_intern_msg()
    elif input_text in ['skill', 'skills']:
        text = utils.get_skill_msg()
    elif input_text == 'contact':
        text = utils.get_contact_msg()
    elif input_text in ['award', 'honor']:
        text = utils.get_award_msg()
    else:
        text = utils.get_default_msg()
    message = TextSendMessage(text=text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

