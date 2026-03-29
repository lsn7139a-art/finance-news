#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sending email directly to your mailbox
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Test configuration - you'll need to provide your email credentials
EMAIL_HOST = "smtp.qq.com"  # For QQ mail
EMAIL_PORT = 465
EMAIL_HOST_USER = "1372943709@qq.com"
EMAIL_HOST_PASSWORD = "rdwczjrfwdnkbagj"
RECIPIENT_EMAIL = "1372943709@qq.com"

def send_test_email():
    """Send a test email with the financial news content"""

    # Read the generated news file
    try:
        with open('financial_news_2026-03-29.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract subject and body
        lines = content.split('\n')
        subject = lines[0].replace('Subject: ', '') if lines[0].startswith('Subject:') else f"【今日金融快报】{datetime.now().strftime('%Y-%m-%d')}"
        body = '\n'.join(lines[2:]) if len(lines) > 2 else content

    except FileNotFoundError:
        # If file doesn't exist, create a simple test message
        subject = f"【今日金融快报】{datetime.now().strftime('%Y-%m-%d')} - 测试邮件"
        body = """您好，这是一封测试邮件。

我们正在测试金融快报邮件发送功能。
如果收到此邮件，说明邮件发送功能正常工作。

祝您投资顺利，日常请关注风险。
"""

    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = EMAIL_HOST_USER
    message["To"] = RECIPIENT_EMAIL

    # Create the plain-text version of your message
    part1 = MIMEText(body, "plain", "utf-8")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)

    # Create secure connection with server and send email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context) as server:
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, RECIPIENT_EMAIL, message.as_string())
        print("测试邮件发送成功！")
        print(f"邮件已发送至: {RECIPIENT_EMAIL}")
        print(f"邮件主题: {subject}")
    except Exception as e:
        print(f"邮件发送失败: {e}")
        print("请检查以下配置:")
        print("1. 邮箱地址是否正确")
        print("2. 授权码是否正确")
        print("3. SMTP服务器设置是否正确")

if __name__ == "__main__":
    print("开始发送测试邮件到您的邮箱...")
    print(f"目标邮箱: {RECIPIENT_EMAIL}")
    send_test_email()