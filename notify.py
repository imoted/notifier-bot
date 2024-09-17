# notify.py

import requests
import os
from datetime import datetime

# LINE Notifyにメッセージを送信する関数
def send_line_notify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {os.getenv("LINE_NOTIFY_TOKEN")}'
    }
    data = {'message': message}
    requests.post(url, headers=headers, data=data)

# 曜日ごとのメッセージを送信
today = datetime.today()
weekday = today.weekday()

if weekday == 4:  # 金曜日
    send_line_notify('資源プラスチックの回収日')
elif weekday == 1:  # 火曜日
    send_line_notify('資源ゴミの回収日')
elif weekday == 2 or weekday == 5:  # 水曜日または土曜日
    send_line_notify('燃えるゴミの回収日')
elif weekday == 3:  # 木曜日
    if today.day in range(1, 8) or 15 <= today.day <= 21:  # 第1 or 第3木曜日
        send_line_notify('燃えないゴミの回収日')
