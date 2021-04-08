from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

import requests
import urllib
import re
import random

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature) # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            try:
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

            except:
                # 回覆圖片 ImageSendMessage --ok
                # if event.message.text == "圖片":
                # if isinstance(event, MessageEvent):
                #     line_bot_api.reply_message(
                #         event.reply_token,
                #         ImageSendMessage(original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4dI0KzluMib7ZBG4vYHbtbtfxi88lwUmSZB1FVFE&amp;usqp=C',
                #                             preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4dI0KzluMib7ZBG4vYHbtbtfxi88lwUmSZB1FVFE&amp;usqp=C' )
                # )

                # 回覆相同文字 TextSendMessage --ok
                # if isinstance(event, MessageEvent): # 如果有訊息事件
                #     line_bot_api.reply_message(
                #         event.reply_token,
                #         TextSendMessage(text=event.message.text) # 回復傳入的訊息文字
                #     )


                # 回覆貼圖 StickerSendMessage --ok
                if isinstance(event, MessageEvent):
                    line_bot_api.reply_message(
                        event.reply_token,
                        StickerSendMessage(package_id=11539, sticker_id=52114122)
                    )

                # Imagemap message
                # if event.message.text == "圖片":
                #     line_bot_api.reply_message(event.replytoken, ImageSendMessage(
                #         type = 'imagemap',
                #         baseUrl = 'https://github.com/line/line-bot-sdk-nodejs/raw/master/examples/kitchensink/static/rich',
                #         altText = 'Imagemap alt text',
                #     ))

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
