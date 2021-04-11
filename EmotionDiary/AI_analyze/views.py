from django.shortcuts import render
from cgitb import handler
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

from . import forms
from . import models

import tempfile
import requests
import datetime
import urllib
import re
import random

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

liff_api = LIFF(settings.LINE_CHANNEL_ACCESS_TOKEN)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature) # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def user_inform_from(request):
    form = forms.UserInformFrom(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    return render(request, 'UserInform/new.html', {
        'form': form
    })

@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_text_message(event):
    if isinstance(event.message, ImageMessage):
        print("success")

        # 接收照片
        message_content = line_bot_api.get_message_content(event.message.id)
        with tempfile.NamedTemporaryFile(dir='media/images/', prefix=event.source.user_id + '-', delete=False) as file:
            for chunk in message_content.iter_content():
                file.write(chunk)

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="成功上傳照片")
        )
    # LIFF
    # if event.message.text == '加入':
        # line_bot_api.reply_message(event.reply_token, SendMessage('http://127.0.0.1:8000/AI_analyez/userinform/')
        # liff_id = '1655797178-gdXONrPE'
        # line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/'+liff_id))

    elif isinstance(event, MessageEvent):
        # 回覆圖片 ImageSendMessage --ok
        find_pic = {'tbm': 'isch', 'q': event.message.text}
        url = f"https://www.google.com/search?{urllib.parse.urlencode(find_pic)}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

        req = urllib.request.Request(url, headers=headers)
        conn = urllib.request.urlopen(req)
        data = conn.read()

        pattern = 'img data-src="\S*"'
        img_list = []

        for match in re.finditer(pattern, str(data)):
            img_list.append(match.group()[14:-3])

        random_img_url = img_list[random.randint(0, len(img_list)+1)]
        print(random_img_url)

        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url = random_img_url,
                             preview_image_url = random_img_url))

        # 回覆相同文字 TextSendMessage --ok
        # if isinstance(event, MessageEvent): # 如果有訊息事件
        #     line_bot_api.reply_message(
        #         event.reply_token,
        #         TextSendMessage(text=event.message.text) # 回復傳入的訊息文字
        #     )

        # 回覆貼圖 StickerSendMessage --ok
        # if isinstance(event, MessageEvent):
        #     line_bot_api.reply_message(
        #         event.reply_token,
        #         StickerSendMessage(package_id=11539, sticker_id=52114122)
        #     )



        # Imagemap message
        # if event.message.text == "圖片":
        #     line_bot_api.reply_message(event.replytoken, ImageSendMessage(
        #         type = 'imagemap',
        #         baseUrl = 'https://github.com/line/line-bot-sdk-nodejs/raw/master/examples/kitchensink/static/rich',
        #         altText = 'Imagemap alt text',
        #     ))
