from django.shortcuts import render
from cgitb import handler
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
from flask import Flask, request, abort

from . import forms
from . import models
from liffpy import (
    LineFrontendFramework as LIFF,
)

import requests
import datetime
import urllib
import re
import random

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# filter 來過濾條件

# app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

liff_api = LIFF(settings.LINE_CHANNEL_ACCESS_TOKEN)


# @app.route("callback/", methods=['POST'])
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # get X-Line-Signature header value 訊息驗證的加密簽章
        signature = request.META['HTTP_X_LINE_SIGNATURE']

        # get request body as text
        # body = request.body.decode('utf-8')
        body = request.get_data(as_text = True)
        # app.logger.info("Request body: " + body)

        try:
            handler.handle(body, signature) # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()

        except LineBotApiError:
            return HttpResponseBadRequest()

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


# @app.route("/userinform", methods=['GET', 'POST'])
def user_inform_from(request):
    form = forms.UserInformFrom(request.POST or None, request.FILES or None)
    if form.is_valid():

        form.save()

#     line_bot_api.reply_message(event.reply_token, text="新增成功")
    return render(request, 'UserInform/new.html', {
        'form': form
    })

    # return render(request, 'UserInform/newUserInform.html', {
    #     'form': form
    # })



def menu_diary(request):

    return render(request, 'Diary/MenuDiary.html', {
    })

# @app.route("/editdiary", methods=['GET', 'POST'])
def edit_diary(event):
    # userid = event.source.user_id
    # print(userid)
    # diary = models.Diary.objects.get(line_id=userid)

    return render(request, 'Diary/editDiary.html', {
    })


@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_text_message(event):
    if isinstance(event, MessageEvent):
        # 取得使用者的Line資訊
        userid = event.source.user_id
        print(userid)

    # LIFF
    elif 'https://' in event.message.text:
        # 丟https://網址 轉換成 https://liff.line.me/
        liff_id = liff_api.add(view_type="tall", view_url=event.message.text)
        message=[]
        message.append(TextSendMessage(text='https://liff.line.me/'+liff_id))
        line_bot_api.reply_message(event.reply_token, message)

    # if event.message.text == '日記':
    #     liff_id = '1655797178-OAZa4b85'
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/'+liff_id))

