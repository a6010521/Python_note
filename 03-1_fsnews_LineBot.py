from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 設定你的 Line Bot Token & Secret
LINE_ACCESS_TOKEN = "Access Token"
LINE_SECRET = "Channel Secret"

app = Flask(__name__)
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
handler = WebhookHandler(LINE_SECRET)

# Webhook 接收來自 LINE 的請求
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

# 處理使用者發送的訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_msg = event.message.text

    if user_msg == "新聞":
        from news_crawler import get_news  # 引入剛剛的爬蟲函式
        news = get_news()
        reply_msg = f" 最新新聞：\n\n{news}"
    else:
        reply_msg = "請輸入『新聞』來獲取最新消息！"

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_msg))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
