#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2018/7/17 4:27 PM
# @Author: jasmine sun
# @File  : emailDemo.py

import smtplib
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可
import logging

logger = logging.getLogger("email_log")
logger.setLevel(logging.DEBUG)

# 输出到屏幕
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
# 输出到文件
fh = logging.FileHandler("log.log")
fh.setLevel(logging.INFO)
# 设置日志格式
fomatter = logging.Formatter('%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s')
ch.setFormatter(fomatter)
fh.setFormatter(fomatter)
logger.addHandler(ch)
logger.addHandler(fh)


def sendEmail(receiver):
    # 发件人和收件人
    sender = 'sender@163.com'


    # 所使用的用来发送邮件的SMTP服务器
    smtpServer = 'smtp.163.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = 'xxxxx'
    password = 'xxxxx'

    mail_title = '2018.7.23邮件测试'
    mail_body = '邮件测试'

    # 创建一个实例
    message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = receiver  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    try:
        smtp = smtplib.SMTP()  # 创建一个连接
        smtp.connect(smtpServer)  # 连接发送邮件的服务器
        smtp.login(username, password)  # 登录服务器
        smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
        logger.info("邮件发送成功！！！")
        print("邮件发送成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        logger.info("邮件发送失败！！！")
        print("邮件发送失败！！！")


if __name__ == '__main__':
    receiver = input("To: ")
    sendEmail(receiver)
