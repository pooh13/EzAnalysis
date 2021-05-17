from linebot import (
    LineBotApi, WebhookHandler
)

LINE_CHANNEL_ACCESS_TOKEN = '6pzegJmVUuwqq78rLWl87O9Tr5N8kNU7r8+kxhizZ2emhpTiWMt2OdBCnA19Xqi/nla5PeZNwO++cZYOMHDZKuCpezNxMVYbyDRK1g3RGemZD7XR09bIOaOW3uIBnpBga6XGUXS5M0smEIW4O32aHgdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

rich_menu_list = line_bot_api.get_rich_menu_list()

for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)

# 刪除 richMenu
# line_bot_api.delete_rich_menu('richmenu-5790a3e528abc5c1391c0272b6e54040')
