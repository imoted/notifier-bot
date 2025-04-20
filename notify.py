from datetime import datetime, timezone, timedelta
import requests
import os

# LINE Messaging APIを使用してメッセージを送信する関数
def send_line_message(message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    }
    user_id = os.getenv("LINE_USER_ID")  # メッセージを送信するユーザーID

    data = {
        'to': user_id,
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # エラーステータスコードの場合例外を発生
        print(f"メッセージを送信しました: {message}")
        return True
    except requests.exceptions.HTTPError as http_err:
        error_message = f"HTTP エラーが発生しました: {http_err} - レスポンス: {response.text}"
        print(error_message)
        return error_message
    except requests.exceptions.RequestException as err:
        error_message = f"リクエストエラーが発生しました: {err}"
        print(error_message)
        return error_message

# 日本標準時（JST）のタイムゾーンを設定
JST = timezone(timedelta(hours=9))
today = datetime.now(JST)
weekday = today.weekday()

if weekday == 4:  # 金曜日
    send_line_message('資源プラスチックの回収日')
elif weekday == 1:  # 火曜日
    send_line_message('資源ゴミの回収日')
elif weekday == 2 or weekday == 5:  # 水曜日または土曜日
    send_line_message('燃えるゴミの回収日')
elif weekday == 3:  # 木曜日
    if today.day in range(1, 8) or 15 <= today.day <= 21:  # 第1 or 第3木曜日
        send_line_message('燃えないゴミの回収日')
