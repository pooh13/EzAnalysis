import os
import requests
from linebot import LineBotApi
from linebot.models import (
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds,
    URIAction, PostbackAction
    )

LINE_CHANNEL_ACCESS_TOKEN = '6pzegJmVUuwqq78rLWl87O9Tr5N8kNU7r8+kxhizZ2emhpTiWMt2OdBCnA19Xqi/nla5PeZNwO++cZYOMHDZKuCpezNxMVYbyDRK1g3RGemZD7XR09bIOaOW3uIBnpBga6XGUXS5M0smEIW4O32aHgdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

# create rich menu
# from https://developers.line.biz/en/reference/messaging-api/#create-rich-menu
rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=800, height=270),  # 2500x1686, 2500x843, 1200x810, 1200x405, 800x540, 800x270
    selected=True,
    name="PreviousPage",
    chat_bar_text="See Menu",
    areas=[
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=400, height=270),
            action=PostbackAction(label='Previous Page', data='action=nextpage')),
        RichMenuArea(
            bounds=RichMenuBounds(x=400, y=0, width=400, height=270),
            action=URIAction(label='Google', uri='https://www.google.com/')),
        ]
)

rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
print("rich_menu_id=", rich_menu_id)

# upload image and link it to richmenu
# from https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image
with open(os.path.join('images', 'secondpage.jpg'), 'rb') as f:
    line_bot_api.set_rich_menu_image(rich_menu_id, 'image/jpeg', f)

# richmenu-258ba2db128c7d79f836b04bbaa93f31
