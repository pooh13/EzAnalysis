import os
import datetime
import time
import tempfile

from django.shortcuts import render
from cgitb import handler
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

from . import forms
from . import models
from liffpy import (
    LineFrontendFramework as LIFF,
)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# setting TIME
t = time.time()
today = datetime.date.today().strftime("%Y-%m-%d")

# filter 來過濾條件


# LINE 聊天機器人的基本資料
liff_api = LIFF(settings.LINE_CHANNEL_ACCESS_TOKEN)
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
url = settings.SET_URL

# 判斷使用者在 LINEBot 中日記事件的觸發
prev = {}

# kelly
'''
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
'''


# liff_api = LIFF(settings.LINE_CHANNEL_ACCESS_TOKEN)


def job_select():
    content = "student"
    return content


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


def menu_diary(request):
    return render(request, 'Diary/menuDiary.html', {

    })


def add_diary1(request, pk):
    today = datetime.date.today().strftime("%Y/%m/%d")
    time = datetime.datetime.today().strftime("%H:%M")
    form = forms.DiaryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    print(form)
    return render(request, 'Diary/addDiary1.html', {
        'today': today, 'time': time, 'form': form,
    })


def add_diary2(request):
    # diary = models.Diary.objects.get(id=pk)
    # form = forms.DiaryForm(request.POST or None, instance=diary)
    return render(request, 'Diary/addDiary2.html', {

    })


def add_diary3(request):
    return render(request, 'Diary/addDiary3.html', {

    })


def edit_diary(request, pk):
    diary = models.Diary.objects.get(line_id=pk)
    form = forms.DiaryForm(request.POST or None, instance=diary)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'Diary/editDiary.html', {
        'form': form,
    })


def profile(request):
    return render(request, 'UserInform/profile.html', {
    })


def edit_user(request, pk):
    userinfo = models.UserInform.objects.get(line_id=pk)
    form = forms.UserInformFrom(request.POST or None, instance=userinfo)
    # print(profile)
    # print(form)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'UserInform/editUser.html', {
        'form': form,
    })


# LINE BOT
@handler.add(FollowEvent)
def handle_follow(event):
    line_id = event.source.user_id
    profile = line_bot_api.get_profile(line_id)

    line_name = profile.display_name
    line_picture_url = profile.picture_url  # 取得使用者的大頭貼
    line_status_message = profile.status_message  # 取得使用者的個簽留言
    unfollow = False

    buttons_template_message = TemplateSendMessage(
        alt_text='Product Promotion',
        template=ButtonsTemplate(
            title="歡迎加入心情日記-臉部辨識",
            text='為了讓整個分析可以更精準\n請幫助我們回答幾項問題',
            actions=[
                PostbackAction(
                    label='開始',
                    display_text='開始',
                    data='promotion=true'
                ),
            ]
        )
    )

    # 判斷資料庫中的使用者資訊是否完整
    check_info = models.UserInform.objects.exclude(gender__isnull=True).exclude(gender="")
    check_list = [i.line_id for i in check_info]

    if line_id in check_list:
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="您已註冊過囉\U0010007A"),
            )
    else:
        # 判斷此用戶在UserInform內的line_id欄位是否存在，若存在則get到，若不存在則新增一筆預設資料
        try:
            models.UserInform.objects.get(line_id=event.source.user_id)
        except models.UserInform.DoesNotExist:
            models.UserInform.objects.create(line_id=event.source.user_id, username=line_name)

        line_bot_api.reply_message(
            event.reply_token,
            [
                # TextSendMessage(text="Hello\U0010007A"),
                # TextSendMessage(text="You are " + line_name),
                # TextSendMessage(text="You're picture is " + line_picture_url),
                # TextSendMessage(text="You're status_message is " + line_status_message),
                buttons_template_message,
            ]
        )


@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_text_message(event):
    print(prev)
    # test ------------------
    # test = models.UserInform.objects.exclude(gender__isnull=True).exclude(gender="")
    # check_list = [i.line_id for i in test]
    # print(event.source.user_id not in check_list)
    # career_id = models.Career.objects.get(career_name='學生')
    # print(career_id.career_id)
    # print(models.Diary.objects.filter(line_id=event.source.user_id, date=today).exists())
    # print(datetime.datetime.fromtimestamp(t))
    # ------------------------

    profile = line_bot_api.get_profile(event.source.user_id)
    username = profile.display_name

    # 判斷此用戶在UserInform內的line_id欄位是否存在，若存在則get到，若不存在則新增一筆預設資料
    try:
        models.UserInform.objects.get(line_id=event.source.user_id)
    except models.UserInform.DoesNotExist:
        models.UserInform.objects.create(line_id=event.source.user_id, username=username)

    ignore = ['設定成功！', '日記儲存成功！']
    emotion = {'超開心': 5, '開心': 4, '普通': 3, '難過': 2, '超難過': 1}
    career = ['學生', '軍公教', '服務業', '自由業', '工商業', '家管', '退休人員', '農民漁牧業', '其他']

    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
        # print(event)

        # 接收照片
        message_content = line_bot_api.get_message_content(event.message.id)

        if prev:
            if prev[event.source.user_id] == "diary_image":
                # 判斷使用者當天是否已經登入過一次照片(使用者一天只會有一張照片)
                if os.path.isfile('media/images/' + event.source.user_id + '-' + today + '.' + ext):
                    os.remove('media/images/' + event.source.user_id + '-' + today + '.' + ext)

                with open('media/images/' + event.source.user_id + '-', 'wb') as file:
                    for chunk in message_content.iter_content():
                        file.write(chunk)

                    temp_file_path = file.name

                dist_path = temp_file_path + today + '.' + ext

                # dist_name = os.path.basename(dist_path)
                os.rename(temp_file_path, dist_path)
                # print(dist_path)

                arr = dist_path.split("/")
                db_pic_path = arr[-1::-1][1] + "/" + arr[-1::-1][0]  # img/XXX.jpg
                # print(db_pic_path)

                upload_img = models.Diary.objects.get(line_id=event.source.user_id, date=today)
                upload_img.pic = db_pic_path
                upload_img.save()

                prev.update({event.source.user_id: ''})

                # 取得日記心情並轉換為文字
                diary = models.Diary.objects.get(line_id=event.source.user_id, date=today)
                mood = ""
                for mood_name, mood_int in emotion.items():
                    if mood_int == diary.mood:
                        mood = mood_name

                confirm_template = TemplateSendMessage(
                    alt_text='確認訊息',
                    template=ConfirmTemplate(
                        title='這是ConfirmTemplate',
                        text='確認以上內容是否正確！',
                        actions=[
                            MessageAction(
                                label='確認',
                                text='確認',
                            ),
                            MessageAction(
                                label='修改',
                                text='修改'
                            ),
                        ]
                    )
                )

                # print('https://' + url + '/' + dist_path.replace("\\", "/"))

                line_bot_api.reply_message(
                    event.reply_token, [
                        TextSendMessage(text="已成功上傳照片"),
                        TextSendMessage(text="您今天的心情為：" + mood + "\n\n所輸入的日記內容為：\n" + diary.note),
                        TextSendMessage(text="所上傳的照片為："),
                        ImageSendMessage(
                            original_content_url='https://' + url + '/' + dist_path,
                            preview_image_url='https://' + url + '/' + dist_path
                        ),
                        confirm_template
                    ]
                )
            else:
                # 即時照片接收/分析
                with tempfile.NamedTemporaryFile(dir='media/images/', prefix=event.source.user_id + '-', delete=False) as file:
                    for chunk in message_content.iter_content():
                        file.write(chunk)

                    temp_file_path = file.name

                dist_path = temp_file_path + '.' + ext
                # print(dist_path)

                # dist_name = os.path.basename(dist_path)
                os.rename(temp_file_path, dist_path)

                arr = dist_path.split("/")
                db_pic_path = arr[-1::-1][1] + "/" + arr[-1::-1][0]  # img/XXX.jpg
                # print(db_pic_path)

                upload_img = models.InstantPhotoAnalysis(line_id_id=event.source.user_id, date=datetime.datetime.fromtimestamp(t), pic=db_pic_path)
                # upload_img.pic.save(event.source.user_id + '.' + ext, File(open(dist_path, 'rb')))  # 同張照片會存兩次
                upload_img.save()

                line_bot_api.reply_message(
                    event.reply_token, [
                        TextSendMessage(text="已成功上傳照片")
                    ]
                )
        else:  # if dictionary prev={}
            # 即時照片接收/分析
            with tempfile.NamedTemporaryFile(dir='media/images/', prefix=event.source.user_id + '-', delete=False) as file:
                for chunk in message_content.iter_content():
                    file.write(chunk)

                temp_file_path = file.name

            dist_path = temp_file_path + '.' + ext
            # print(dist_path)

            # dist_name = os.path.basename(dist_path)
            os.rename(temp_file_path, dist_path)

            arr = dist_path.split("/")
            db_pic_path = arr[-1::-1][1] + "/" + arr[-1::-1][0]  # img/XXX.jpg
            # print(db_pic_path)

            upload_img = models.InstantPhotoAnalysis(line_id_id=event.source.user_id, date=datetime.datetime.fromtimestamp(t), pic=db_pic_path)
            # upload_img.pic.save(event.source.user_id + '.' + ext, File(open(dist_path, 'rb')))  # 同張照片會存兩次
            upload_img.save()

            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text="已成功上傳照片")
                ]
            )

    elif isinstance(event, MessageEvent):
        msg = event.message.text
        msg = msg.encode('utf-8')
        user_line_id = event.source.user_id

        # LIFF
        # if 'https://' in event.message.text:
        #     # 丟https://網址 轉換成 https://liff.line.me/
        #     liff_id = liff_api.add(view_type="tall", view_url=event.message.text)
        #     message=[]
        #     message.append(TextSendMessage(text='https://liff.line.me/'+liff_id))
        #     line_bot_api.reply_message(event.reply_token, message)

        # print(event)
        if event.message.text == "文字":
            print("收到了")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )
        elif event.message.text == "現在時間":
            line_bot_api.reply_message(
                event.reply_token,
                # TextSendMessage(text=str(datetime.datetime.now())[11:16])
                TextSendMessage(text=today)
            )
        elif event.message.text == "填寫資料":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="url")
            )
        elif event.message.text in ["輸入日記", "修改"]:
            imagemap_message = ImagemapSendMessage(
                base_url='https://imgur.com/758BclP.png',
                alt_text='this is an image map',
                base_size=BaseSize(height=1040, width=1040),
                actions=[
                    MessageImagemapAction(
                        text='超開心',
                        area=ImagemapArea(
                            x=60, y=200, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='開心',
                        area=ImagemapArea(
                            x=400, y=200, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='普通',
                        area=ImagemapArea(
                            x=740, y=200, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='難過',
                        area=ImagemapArea(
                            x=210, y=600, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='超難過',
                        area=ImagemapArea(
                            x=590, y=600, width=240, height=240
                        )
                    ),
                ]
            )

            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text="您現在您可以輸入日記囉~"),
                    TextSendMessage(text="請選擇今天一整天下來感受到的心情"),
                    imagemap_message
                ]
            )
        elif event.message.text in emotion.keys():
            if models.Diary.objects.filter(line_id=event.source.user_id, date=today).exists():

                user_mood = models.Diary.objects.get(line_id=event.source.user_id, date=today)
                user_mood.mood = emotion.get(event.message.text)
                user_mood.save()

                prev[user_line_id] = 'get_diary'

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='接下來您可以開始輸入您今天的心情日記囉~')
                )
            else:
                models.Diary.objects.create(line_id_id=event.source.user_id, date=today, mood=emotion.get(event.message.text))
                prev[user_line_id] = 'get_diary'

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='接下來您可以開始輸入您今天的心情日記囉~')
                )
        # 16--------------------------------------------------------------------------
        # elif event.message.text == '日記':
        #     userid = event.source.user_id
        #     print("日記" + "userId=" + userid)
        #     liff_id = '1655950183-lEgOEwVq'
        #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/'+liff_id))
        #     # user_id = models.UserInform.objects.
        # ----------------------------------------------------------------------------
        elif event.message.text == "設定性別":
            # emoji_f = {"index": 0, "productId": "5ac1bfd5040ab15980c9b435", "emojiId": "001"}
            # emoji_m = {"index": 0, "productId": "5ac1bfd5040ab15980c9b435", "emojiId": "001"}
            # emoji = chr(0x100078)
            # print(emoji_f)

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
                alt_text='請輸入生日日期',
                template=ButtonsTemplate(
                    text='請輸入生日日期',
                    title='設定生日',
                    actions=[
                        DatetimePickerAction(
                            label='設定',
                            data='promotion=date',
                            mode='date',
                            initial=today,
                        )
                    ]
                )
            )
            line_bot_api.reply_message(
                event.reply_token,
                date_picker
            )
        elif event.message.text == "選擇清單":
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
                        link_uri='https://' + url + '/AI_analyze/userdata/',
                        area=ImagemapArea(
                            x=520, y=520, width=520, height=520
                        )
                    ),
                ]
            )
            line_bot_api.reply_message(
                event.reply_token,
                imagemap_message
            )
        elif event.message.text == "填寫日記":
            imagemap_message = ImagemapSendMessage(
                base_url='https://imgur.com/yPTyIWN.jpg',
                alt_text='choose how to write diary',
                base_size=BaseSize(height=240, width=1040),
                actions=[
                    MessageImagemapAction(
                        text='輸入日記',
                        area=ImagemapArea(
                            x=0, y=0, width=520, height=240
                        )
                    ),
                    URIImagemapAction(
                        link_uri='https://liff.line.me/1655976131-1rjWz2x3',
                        area=ImagemapArea(
                            x=520, y=0, width=520, height=240
                        )
                    ),
                    # MessageImagemapAction(
                    #     text='設定生日',
                    #     area=ImagemapArea(
                    #         x=0, y=520, width=520, height=520
                    #     )
                    # ),
                    # URIImagemapAction(
                    #     link_uri='https://' + url + '/AI_analyze/userinform/' + event.source.user_id,
                    #     area=ImagemapArea(
                    #         x=520, y=520, width=520, height=520
                    #     )
                    # ),
                ]
            )
            line_bot_api.reply_message(
                event.reply_token,
                imagemap_message
            )
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
        elif event.message.text == "心情":
            imagemap_message = ImagemapSendMessage(
                base_url='https://imgur.com/758BclP.png',
                alt_text='this is an image map',
                base_size=BaseSize(height=1040, width=1040),
                actions=[
                    MessageImagemapAction(
                        text='超開心',
                        area=ImagemapArea(
                            x=60, y=200, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='開心',
                        area=ImagemapArea(
                            x=400, y=200, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='普通',
                        area=ImagemapArea(
                            x=740, y=200, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='難過',
                        area=ImagemapArea(
                            x=210, y=600, width=240, height=240
                        )
                    ),
                    MessageImagemapAction(
                        text='超難過',
                        area=ImagemapArea(
                            x=590, y=600, width=240, height=240
                        )
                    ),
                ]
            )
            line_bot_api.reply_message(event.reply_token, imagemap_message)
        elif event.message.text in ignore:
            pass
        elif event.message.text in career:

            career_text = models.Career.objects.get(career_name=event.message.text)
            userinfo = models.UserInform.objects.get(line_id=event.source.user_id)
            userinfo.career_id_id = career_text.career_id
            userinfo.save()

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="您的職業設定成功！")
            )
        elif event.message.text == "確認":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="日記儲存成功！")
            )
        else:
            if user_line_id not in prev:
                e = chr(0x100010)
                e2 = chr(0x10008D)
                line_bot_api.reply_message(
                    event.reply_token, [
                        TextSendMessage(text='不好意思 我不太清楚你的意思'),
                        # StickerSendMessage(package_id=11539, sticker_id=52114129)
                    ]
                )
            elif prev[user_line_id] == "get_diary":
                diary = event.message.text
                prev.update({event.source.user_id: 'diary_image'})

                # 儲存輸入之日記內容
                set_diary = models.Diary.objects.get(line_id=event.source.user_id, date=today)
                set_diary.note = diary
                set_diary.save()

                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="請傳送一張今天的照片~"),
                )
            elif prev[user_line_id] == "diary_image":
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="請傳送一張今天的照片~"),
                )
            else:
                e = chr(0x100010)
                e2 = chr(0x10008D)
                line_bot_api.reply_message(
                    event.reply_token, [
                        TextSendMessage(text='不好意思 我不太清楚你的意思'),
                        # StickerSendMessage(package_id=11539, sticker_id=52114129)
                    ]
                )


@handler.add(PostbackEvent)
def handle_post_message(event):
    if event.postback.data == "promotion=true":
        # if models.UserInform.objects.filter(line_id=event.source.user_id).exists():
        #     line_bot_api.reply_message(
        #         event.reply_token,
        #         [
        #             TextSendMessage(text="您已註冊過囉\U0010007A"),
        #         ]
        #     )
        # else:
        date_picker = TemplateSendMessage(
            alt_text='請輸入生日日期',
            template=ButtonsTemplate(
                text='請輸入生日日期',
                title='設定生日',
                actions=[
                    DatetimePickerAction(
                        label='設定',
                        data='promotion=date',
                        mode='date',
                        initial=today,
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,
            date_picker
        )
    elif event.postback.data == "promotion=date":
        time_type = event.postback.params
        print(time_type)

        birth_date = models.UserInform.objects.get(line_id=event.source.user_id)
        birth_date.birth = time_type.get('date')
        birth_date.save()

        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://imgur.com/6KC33AK.jpg',
                title='選擇您的性別',
                text='請選擇',
                actions=[
                    PostbackAction(
                        label='女生(Female)',
                        data='gender=female'
                    ),
                    PostbackAction(
                        label='男生(Male)',
                        data='gender=male'
                    ),
                ]
            )
        )

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='您的生日是 {}'.format(str(time_type.get('date')))),
                TextSendMessage(text="生日設定成功！"),
                buttons_template_message
            ]
        )
    elif event.postback.data == "gender=male":
        gender_choice = models.UserInform.objects.get(line_id=event.source.user_id)
        gender_choice.gender = "M"
        gender_choice.save()

        career_image_map_message = ImagemapSendMessage(
            base_url='https://imgur.com/uJHMGjf.png',
            alt_text='this is an image map',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='學生',
                    area=ImagemapArea(
                        x=120, y=120, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='軍公教',
                    area=ImagemapArea(
                        x=400, y=120, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='服務業',
                    area=ImagemapArea(
                        x=680, y=120, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='自由業',
                    area=ImagemapArea(
                        x=120, y=400, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='工商業',
                    area=ImagemapArea(
                        x=400, y=400, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='家管',
                    area=ImagemapArea(
                        x=680, y=400, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='退休人員',
                    area=ImagemapArea(
                        x=120, y=680, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='農民漁牧業',
                    area=ImagemapArea(
                        x=400, y=680, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='其他',
                    area=ImagemapArea(
                        x=680, y=680, width=240, height=240
                    )
                ),
            ]
        )

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='嗨~帥哥'),
                TextSendMessage(text="性別設定成功！"),
                career_image_map_message
            ]
        )
    elif event.postback.data == "gender=female":
        gender_choice = models.UserInform.objects.get(line_id=event.source.user_id)
        gender_choice.gender = "F"
        gender_choice.save()

        career_image_map_message = ImagemapSendMessage(
            base_url='https://imgur.com/uJHMGjf.png',
            alt_text='this is an image map',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='學生',
                    area=ImagemapArea(
                        x=120, y=120, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='軍公教',
                    area=ImagemapArea(
                        x=400, y=120, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='服務業',
                    area=ImagemapArea(
                        x=680, y=120, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='自由業',
                    area=ImagemapArea(
                        x=120, y=400, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='工商業',
                    area=ImagemapArea(
                        x=400, y=400, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='家管',
                    area=ImagemapArea(
                        x=680, y=400, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='退休人員',
                    area=ImagemapArea(
                        x=120, y=680, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='農民漁牧業',
                    area=ImagemapArea(
                        x=400, y=680, width=240, height=240
                    )
                ),
                MessageImagemapAction(
                    text='其他',
                    area=ImagemapArea(
                        x=680, y=680, width=240, height=240
                    )
                ),
            ]
        )

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='嗨~美女'),
                TextSendMessage(text="性別設定成功！"),
                career_image_map_message
            ]
        )
    # elif event.postback.data == "confirm=alter":
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text="日記儲存成功！"),
    #     )
    # 切換 RichMenu 清單
    # elif event.postback.data == "action=nextpage":
    #     print("one")
    #     line_bot_api.link_rich_menu_to_user(event.source.user_id, "richmenu-3045108a9995f171da79f56000760fa0")  # first
    # elif event.postback.data == "action=previouspage":
    #     print("two")
    #     line_bot_api.link_rich_menu_to_user(event.source.user_id, "richmenu-258ba2db128c7d79f836b04bbaa93f31")  # second





