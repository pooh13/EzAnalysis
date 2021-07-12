import os
import datetime
import time
import tempfile

from django.shortcuts import render, redirect
from cgitb import handler
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseForbidden
from django.urls import reverse
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


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        # get X-Line-Signature header value 訊息驗證的加密簽章
        signature = request.META['HTTP_X_LINE_SIGNATURE']

        # get request body as text
        body = request.body.decode('utf-8')

        try:
            # 傳入的事件
            handler.handle(body, signature)
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


def profile(request):
    return render(request, 'UserInform/profile.html', {
    })


def edit_user(request, pk):
    userinfo = models.UserInform.objects.get(line_id=pk)
    form = forms.UserInForm(request.POST or None, instance=userinfo)
    # print(profile)
    # print(form)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'UserInform/editUser.html', {
        'form': form,
    })


def diary(request):
    return render(request, 'Diary/diary.html', {

    })


def menu_diary(request, pk):
    get_diary = models.Diary.objects.filter(line_id=pk)
    # 判斷該使用者當天是否填寫過
    if get_diary:
        for d in get_diary:
            if d.date.strftime('%Y-%m-%d') == today:
                message = '已填過'
            else:
                message = ''    
    else:
        message = ''

    # UserThingForm.save
    thing_form = forms.UserThingsForm(request.POST)
    if request.method == 'POST':
        thing_form.save()

    return render(request, 'Diary/menuDiary.html', {
        'message': message, 'pk': pk,
    })


def add_diary1(request, pk):
    user = models.UserInform.objects.get(line_id=pk)
    form = forms.DiaryForm(instance=user)

    return render(request, 'Diary/addDiary1.html', {
        'form': form
    })


def add_diary2(request):
    # DiaryForm.save
    diary_form = forms.DiaryForm(request.POST, request.FILES)
    userid = request.POST['line_id']
    upload_photo = request.FILES['pic']
    day = datetime.datetime.today().date().strftime('%Y%m%d')
    if request.method == 'POST':
        # 修改上傳照片名稱 (userid-day.jpg)
        if upload_photo:
            photo = diary_form.save(commit=False)
            ext = upload_photo.name.split('.')[-1]
            filename = userid + '-' + day + '.' + ext
            photo.pic.name = filename
            photo.save()

    # 儲存的Diary_id - Diary object(id)
    diary_id = photo.id

    # 選取所做的事的id
    thing_form = forms.UserThingsForm(request.POST)

    return render(request, 'Diary/addDiary2.html', {
        'thing_form': thing_form, 'diary_id': diary_id,
    })


def add_diary3(request, id):
    # id = Diary_id
    thing_form = forms.UserThingsForm(request.POST)
    print(thing_form)

    thing = request.POST['things_id']
    split = thing.split(',')
    thing_list = list(split)

    # 取得Thing
    default_thing = models.DefaultThing.objects.all()

    # 取得所做的事的細項note
    default_note = models.DefaultNote.objects.all()

    return render(request, 'Diary/addDiary3.html', {
        'id': id, 'thing_form': thing_form, 'thing_list': thing_list,
        'default_thing': default_thing, 'default_note': default_note,
    })


def edit_diary(request, pk):
    # 取得使用者當天的Diary
    get_diary = models.Diary.objects.filter(line_id=pk)
    for d in get_diary:
        if d.date.strftime('%Y-%m-%d') == today:
            date = d.date.strftime('%Y-%m-%d')
            time = d.date.strftime('%H:%M')
            mood = d.mood
            pic = d.pic
            user_things = models.UserThings.objects.filter(diary_id=d.id).all()


    # form = forms.DiaryForm(request.POST or None, instance=diary)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()

    return render(request, 'Diary/editDiary.html', {
        'date': date, 'time': time, 'mood': mood,
        'pic': pic, 'user_things': user_things,
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

    # 判斷此用戶在UserInform內的line_id欄位是否存在，若存在則get到，若不存在則新增一筆預設資料
    try:
        models.UserInform.objects.get(line_id=event.source.user_id)
    except models.UserInform.DoesNotExist:
        models.UserInform.objects.create(line_id=event.source.user_id, username=line_name)

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
    profile = line_bot_api.get_profile(event.source.user_id)
    username = profile.display_name
    # print(linebot.models.insight.GenderInsight(gender=))

    # 判斷此用戶在UserInform內的line_id欄位是否存在，若存在則get到，若不存在則新增一筆預設資料
    try:
        models.UserInform.objects.get(line_id=event.source.user_id)
    except models.UserInform.DoesNotExist:
        models.UserInform.objects.create(line_id=event.source.user_id, username=username)

    ignore = ['設定成功！']

    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
        print(event)

        # 接收照片
        message_content = line_bot_api.get_message_content(event.message.id)
        with tempfile.NamedTemporaryFile(dir='media\\img\\', prefix=event.source.user_id + '-', delete=False) as file:
            for chunk in message_content.iter_content():
                file.write(chunk)

            temp_file_path = file.name
            # dist_path = temp_file_path + '.' + ext
            #
            # os.rename(temp_file_path, dist_path)
            #
            # upload_img = models.InstantPhotoAnalysis(line_id_id=event.source.user_id, date=datetime.datetime.fromtimestamp(t))
            # upload_img.pic.save(event.source.user_id + '.' + ext, File(open(dist_path, 'rb')))
            # upload_img.save()

        dist_path = temp_file_path + '.' + ext
        # print(dist_path)

        # dist_name = os.path.basename(dist_path)
        os.rename(temp_file_path, dist_path)

        arr = dist_path.split("\\")
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

        # print(event)
        if event.message.text == "文字":
            print("收到了")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )
        # elif 'https://' in event.message.text:
        #     # 丟https://網址 轉換成 https://liff.line.me/
        #     liff_id = liff_api.add(view_type="tall", view_url=event.message.text)
        #     message=[]
        #     message.append(TextSendMessage(text='https://liff.line.me/'+liff_id))
        #     line_bot_api.reply_message(event.reply_token, message)

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
        elif event.message.text == '日記':
            userid = event.source.user_id
            print("日記" + "userId=" + userid)
            liff_id = '1655950183-lEgOEwVq'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://liff.line.me/'+liff_id))
            # user_id = models.UserInform.objects.
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


@handler.add(PostbackEvent)
def handle_post_message(event):
    if event.postback.data == "promotion=true":
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

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='嗨~帥哥'),
                TextSendMessage(text="性別設定成功！"),
            ]
        )
    elif event.postback.data == "gender=female":
        gender_choice = models.UserInform.objects.get(line_id=event.source.user_id)
        gender_choice.gender = "F"
        gender_choice.save()

        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='嗨~美女'),
                TextSendMessage(text="性別設定成功！"),
            ]
        )
    elif event.postback.data == "action=nextpage":
        print("one")
        line_bot_api.link_rich_menu_to_user(event.source.user_id, "richmenu-3045108a9995f171da79f56000760fa0")  # first
    elif event.postback.data == "action=previouspage":
        print("two")
        line_bot_api.link_rich_menu_to_user(event.source.user_id, "richmenu-258ba2db128c7d79f836b04bbaa93f31")  # second





