from django.shortcuts import render
from cgitb import handler
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

from . import forms
from . import models
from liffpy import (
    LineFrontendFramework as LIFF,
)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# filter 來過濾條件


# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

liff_api = LIFF(settings.LINE_CHANNEL_ACCESS_TOKEN)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # get X-Line-Signature header value 訊息驗證的加密簽章
        signature = request.META['HTTP_X_LINE_SIGNATURE']

        # get request body as text
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

def index(request):
    return render(request, 'index.html', {

    })

def usertest(request):
    form = forms.UserInformFrom(request.POST or None, request.FILES or None)
    # form.fields['line_id'].widget = form.HiddenInput()
    if form.is_valid():
        # form.save(commit=False) # 保存數據，但暫時不提交到數據庫中
        form.save()

    return render(request, 'UserInform/new.html', {
        'form': form
    })

def newUser(request):
    form = forms.UserInformFrom(request.POST or None, request.FILES or None)
    if form.is_valid():
        # newform = form.save(commit=False) # 保存數據，但暫時不提交到數據庫中

        form.save()
    # print(form.as_p())

    return render(request, 'UserInform/newUser.html', {
        'form': form
    })

def editUser(request):
    form = forms.UserInformFrom(request.POST or None, request.FILES or None)
    if form.is_valid():
        # newform = form.save(commit=False) # 保存數據，但暫時不提交到數據庫中
        form.save()
    # print(form.as_p())

    return render(request, 'UserInform/editUser.html', {
        'form': form
    })

@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_text_message(event):
    if isinstance(event, MessageEvent):

        # 取得使用者的Line資訊
        userid2 = event.source.user_id
        # print(userid)

    # LIFF
    if 'https://' in event.message.text:
        # 丟https://網址 轉換成 https://liff.line.me/
        liff_id = liff_api.add(view_type="tall", view_url=event.message.text)
        message=[]
        message.append(TextSendMessage(text='https://liff.line.me/'+liff_id))
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text == '日記':
        userid = event.source.user_id
        print("日記" + "userId=" + userid)
        liff_id = '1655950183-lEgOEwVq'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/'+liff_id))
        # user_id = models.UserInform.objects.

