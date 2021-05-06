import os
import datetime
import time
import tempfile
# from cgitb import handler

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.core.files.base import ContentFile
from django.core.files import File
from . import forms

from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, StickerSendMessage, ImageMessage, \
    ImagemapSendMessage, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, TemplateSendMessage, \
    ButtonsTemplate, PostbackAction, MessageAction, URIAction, responses, DatetimePickerAction, PostbackEvent, \
    ConfirmTemplate
import linebot.models
from linebot.models.emojis import Emojis


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
url = settings.SET_URL

t = time.time()
# print(datetime.date.today().strftime("%Y-%m-%d"))
today = datetime.date.today().strftime("%Y-%m-%d")


def user_inform_from(request, pk):
    box = get_object_or_404(models.UserInform, pk=pk)
    form = forms.UserInformFrom(request.POST or None, request.FILES or None, instance=box)
    # career = models.Career.objects.get(career_id=1)
    if form.is_valid():
        # models.UserInform.objects.get(line_id=request)

        form.save()

    return render(request, 'UserInform/new.html', {
        # 'id': user_line_id,
        'form': form,
        # 'career': career
    })


# 網頁 -------------------------------------------
def test(request):
    return render(request, 'test2.html')


def add(request):
    return render(request, 'add.html')
# -----------------------------------------------


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = handler.handle(body, signature)
            # events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        # print(events)

        # for event in events:
        #     print(events)
        #     if isinstance(event, MessageEvent):
        #         mtext = event.message.text
        #         message = []
        #         message.append(TextSendMessage(text=mtext))
        #         line_bot_api.reply_message(event.reply_token, message)
        #     else:
        #         print(events)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_text_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    username = profile.display_name
    # print(linebot.models.insight.GenderInsight(gender=))

    # 判斷此用戶在UserInform內的line_id欄位是否存在，若存在則get到，若不存在則新增一筆預設資料
    try:
        models.UserInform.objects.get(line_id=event.source.user_id)
    except models.UserInform.DoesNotExist:
        models.UserInform.objects.create(line_id=event.source.user_id, username=username)

    ignore = ['設定成功！']

    # if
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
        print(event)

        # 接收照片
        message_content = line_bot_api.get_message_content(event.message.id)
        with tempfile.NamedTemporaryFile(dir='media\\img\\', prefix=event.source.user_id + '-', delete=False) as file:
            for chunk in message_content.iter_content():
                file.write(chunk)
            temp_file_path = file.name

        dist_path = temp_file_path + '.' + ext
        # dist_name = os.path.basename(dist_path)
        os.rename(temp_file_path, dist_path)

        # print(dist_path)
        upload_img = models.InstantPhotoAnalysis(line_id_id=event.source.user_id, date=datetime.datetime.fromtimestamp(t))
        upload_img.pic.save(event.source.user_id + '.' + ext, File(open(dist_path, 'rb')))
        # upload_img.save()

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="已成功上傳照片")
            ]
        )

    elif isinstance(event, MessageEvent):
        msg = event.message.text
        msg = msg.encode('utf-8')
        user_line_id = event.source.user_id

        # print(event)
        if event.message.text == "文字":
            print("收到了")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )
        elif event.message.text == "選擇":
            insight = line_bot_api.get_insight_demographic()
            print(insight.genders)
            line_bot_api.reply_message(
                event.reply_token,
                insight.genders
            )
        elif event.message.text == "現在時間":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=str(datetime.datetime.now())[11:16])
            )
        elif event.message.text == "填寫資料":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="url")
            )
        elif event.message.text == "設定性別":
            # emoji_f = {"index": 0, "productId": "5ac1bfd5040ab15980c9b435", "emojiId": "001"}
            # emoji_m = {"index": 0, "productId": "5ac1bfd5040ab15980c9b435", "emojiId": "001"}
            # emoji = chr(0x100078)
            # print(emoji_f)

            gender = ""

            buttons_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://imgur.com/6KC33AK.jpg',
                    title='選擇您的性別',
                    text='請選擇',
                    actions=[
                        MessageAction(
                            label='女生(Female)',
                            text='我是女生',
                        ),
                        MessageAction(
                            label='男生(Male)',
                            text='我是男生',
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(
                event.reply_token, buttons_template_message
            )
        elif event.message.text == "設定生日":
            date_picker = TemplateSendMessage(
                alt_text='請輸入日期',
                template=ButtonsTemplate(
                    text='請輸入日期',
                    title='輸入年/月/日',
                    actions=[
                        DatetimePickerAction(
                            label='設定',
                            data='action=buy&itemid=1',
                            mode='date',
                            initial='2019-05-09',
                            min='2019-05-09',
                            max='2099-12-31'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(
                event.reply_token,
                date_picker
            )
        elif event.message.text == "日記":
            # https://50509fc4ca20.ngrok.io/AI_analyze/userinform/
            imagemap_message = ImagemapSendMessage(
                            base_url='https://imgur.com/p1iMJMn.jpg',
                            alt_text='this is an image map',
                            base_size=BaseSize(height=1040, width=1040),
                            actions=[
                                URIImagemapAction(
                                    base_url='https://imgur.com/cStUqlu.jpg',
                                    link_uri='https://' + url + '/AI_analyze/userinform/' + event.source.user_id,
                                    area=ImagemapArea(
                                        x=0, y=0, width=520, height=520
                                    )
                                ),
                                MessageImagemapAction(
                                    text='設定性別',
                                    area=ImagemapArea(
                                        x=520, y=0, width=520, height=520
                                    )
                                ),
                                MessageImagemapAction(
                                    text='設定生日',
                                    area=ImagemapArea(
                                        x=0, y=520, width=520, height=520
                                    )
                                ),
                                URIImagemapAction(
                                    link_uri='https://imgur.com/UtnXde0.jpg',
                                    area=ImagemapArea(
                                        x=520, y=520, width=520, height=520
                                    )
                                ),
                            ]
                        )

            # check = models.UserInform.objects.get(username='kelly')
            # check.line_id = event.source.user_id
            # check.save()

            line_bot_api.reply_message(event.reply_token, imagemap_message)
        elif event.message.text == '我是女生':
            gender_choice = models.UserInform.objects.get(line_id=event.source.user_id)
            gender_choice.gender = "F"
            gender_choice.save()

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="設定成功！")
            )
        elif event.message.text == '我是男生':
            gender_choice = models.UserInform.objects.get(line_id=event.source.user_id)
            gender_choice.gender = "M"
            gender_choice.save()

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="設定成功！")
            )
        elif event.message.text in ignore:
            pass
        else:
            e = chr(0x100010)
            e2 = chr(0x10008D)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='不好意思 我不太清楚你的意思'),
                    # StickerSendMessage(package_id=11539, sticker_id=52114129)
                ]
            )


# @handler.add(PostbackEvent)
# def handle_post_message(event):
#     time_type = event.postback.params
#     print('time' in time_type)
#
#     confirm_template = TemplateSendMessage(
#         alt_text='目錄 template',
#         template=ConfirmTemplate(
#             title='再次確認時間',
#             text='您設定的時間是 {} 嗎?'.format(str(event.postback.params.get('time'))),
#             actions=[
#                 MessageAction(
#                     label='沒錯',
#                     text='沒錯',
#                 ),
#                 MessageAction(
#                     label='更改',
#                     text='更改',
#                 )
#             ]
#         )
#     )
#     line_bot_api.reply_message(
#         event.reply_token,
#         confirm_template
#     )
