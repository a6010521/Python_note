import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#設定基本資料
send_email = "a6010521@gmail.com"
recive_email = "sharon881020@yahoo.com.tw"
password = "lkrd wtca sezf azjr"

#設定標頭
subject = "自動發送"
body = "首封自動發送的郵件"

#郵件訊息
msg = MIMEMultipart()
msg['From'] = send_email
msg['To'] = recive_email
msg['subject'] = subject
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(send_email, password)

text = msg.as_string()
server.sendmail(send_email, recive_email, text)

server.quit()

print("發送成功")