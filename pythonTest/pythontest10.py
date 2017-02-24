"""
#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方SMTP服务
mail_host="smtp.126.com" #设置服务器
mail_user="15720826020@126.com"
mail_pass="yangyh93959697"
#mail_pass="yzdcmajjzxkqjceb"

sender = "15720826020@126.com"
receivers = ['1332850274@qq.com']

message = MIMEText('Pypthon test', 'plain', 'utf-8')
message['From'] = Header("杨云华 软件1231", 'utf-8')
message['To'] = Header("圈圈圈", 'utf-8')
subject = 'python email test'
message['Subject'] = Header(subject, 'utf-8')

print("test1")

try:
    smtpObj= smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    print("test2")
    smtpObj.login(mail_user,mail_pass)
    print("test3")
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("test4")
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error:无法发送邮件")
"""


#coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='15720826020@126.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user='2361031948@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
def mail():
    ret=True
    try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
        msg['From']=formataddr(["杨云华 软件1231",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["圈圈圈",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="主题" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.126.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"yangyh93959697")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed