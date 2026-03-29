#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Email Sender for Financial News
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

def send_test_email():
    """Send a test email to verify the email sending functionality"""

    # Email configuration
    sender_email = "your_email@example.com"  # Replace with your email
    receiver_email = "1372943709@qq.com"
    password = "your_app_password"  # Replace with your email password or app password

    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = f"【今日金融快报】{datetime.now().strftime('%Y-%m-%d')} - 测试邮件"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text version of your message
    text = f"""您好，这是一封测试邮件。

    我们正在测试金融快报邮件发送功能。
    如果收到此邮件，说明邮件发送功能正常工作。

    祝您投资顺利，日常请关注风险。
    """

    # Turn these into plain MIMEText objects
    part1 = MIMEText(text, "plain", "utf-8")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)

    # Create secure connection with server and send email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("测试邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败: {e}")
        print("请检查邮箱配置和SMTP设置")

if __name__ == "__main__":
    print("开始发送测试邮件...")
    send_test_email()