import os
import datetime
import time
import tempfile
from cgitb import handler

from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from .models import PhotoAnalysis
from django.core.files.base import ContentFile
from django.core.files import File

from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, StickerSendMessage, ImageMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

t = time.time()


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        # for event in events:
            # print(events)
            # if isinstance(event, MessageEvent):
            #     mtext = event.message.text
            #     message = []
            #     message.append(TextSendMessage(text=mtext))
            #     line_bot_api.reply_message(event.reply_token, message)
            # else:
            #     print(events)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_text_message(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
        print(event)

        # 接收照片
        message_content = line_bot_api.get_message_content(event.message.id)
        with tempfile.NamedTemporaryFile(dir='media\\images\\', prefix=event.source.user_id + '-', delete=False) as file:
            for chunk in message_content.iter_content():
                file.write(chunk)
            temp_file_path = file.name

        dist_path = temp_file_path + '.' + ext
        # dist_name = os.path.basename(dist_path)
        os.rename(temp_file_path, dist_path)

        print(dist_path)
        upload_img = PhotoAnalysis(line_id=event.source.user_id, date=datetime.datetime.fromtimestamp(t))
        upload_img.pic.save(event.source.user_id + '.' + ext, File(open(dist_path, 'rb')))
        # os.remove(dist_path)

        # print("datetime = ", datetime.datetime)
        # print("t = ", t)

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="已成功上傳照片")
            ]
        )

    elif isinstance(event, MessageEvent):
        msg = event.message.text
        msg = msg.encode('utf-8')
        print(event)
        if event.message.text == "文字":
            print("收到了")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )
        elif event.message.text == "現在時間":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=str(datetime.datetime.now())[11:16])
            )
        else:
            e = chr(0x100010)
            e2 = chr(0x10008D)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='不好意思 我不太清楚你的意思'),
                    StickerSendMessage(package_id=11539, sticker_id=52114129)
                ]
            )
