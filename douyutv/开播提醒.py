import requests
import time
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header
from email.utils import formataddr

mail_host = "smtp.qq.com" 
mail_user = ""
mail_pass = ""

sender = mail_user
receivers = mail_user
roomid = "67373"

message = MIMEText('', 'plain', 'utf-8')  #正文内容
message['From'] = formataddr(["", sender])
message['To'] =  formataddr(["", receivers])
message['Subject'] = Header("小主播thebs开播啦")
message['Content-Type'] = 'Text/HTML';  
def sendmsg():
	smtpObj = smtplib.SMTP_SSL(mail_host, 465)
	smtpObj.login(mail_user,mail_pass)    
	smtpObj.sendmail(sender, receivers, message.as_string())  
	smtpObj.quit()

url = 'http://open.douyucdn.cn/api/RoomApi/room/' + roomid
last_status = '2'

while True :
	data = requests.get(url).json()
	room_status = data['data']['room_status']
	if last_status == '2' and room_status == '1':
		#开播了
		try :
			sendmsg()
		except Error as e:
			print(e)
	last_status = room_status
	time.sleep(90)
