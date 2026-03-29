#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Email Sender for Financial News
Reads the generated news file and sends it via email
"""

import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import glob

def find_latest_news_file():
    """Find the latest financial news file"""
    list_of_files = glob.glob('financial_news_*.txt')
    if not list_of_files:
        return None
    return max(list_of_files, key=os.path.getctime)

def read_news_file(filename):
    """Read the news file and extract subject and content"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract subject and body
    lines = content.split('\n')
    subject = lines[0].replace('Subject: ', '') if lines[0].startswith('Subject:') else f"【今日金融快报】{datetime.now().strftime('%Y-%m-%d')}"
    body = '\n'.join(lines[2:]) if len(lines) > 2 else content

    return subject, body

def send_email(subject, body):
    """Send email using environment variables"""

    # Get email configuration from environment variables
    email_host = os.environ.get('EMAIL_HOST', 'smtp.qq.com')
    email_port = int(os.environ.get('EMAIL_PORT', 465))
    email_host_user = os.environ.get('EMAIL_HOST_USER')
    email_host_password = os.environ.get('EMAIL_HOST_PASSWORD')
    recipient_email = os.environ.get('RECIPIENT_EMAIL', '1372943709@qq.com')

    if not email_host_user or not email_host_password:
        print("Error: Email credentials not provided")
        return False

    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = email_host_user
    message["To"] = recipient_email

    # Create the plain-text version of your message
    part1 = MIMEText(body, "plain", "utf-8")

    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part1)

    # Create secure connection with server and send email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(email_host, email_port, context=context) as server:
            server.login(email_host_user, email_host_password)
            server.sendmail(email_host_user, recipient_email, message.as_string())
        print("邮件发送成功！")
        return True
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return False

def main():
    """Main function"""
    print("开始发送金融快报邮件...")

    # Find the latest news file
    news_file = find_latest_news_file()
    if not news_file:
        print("Error: No financial news file found")
        return

    print(f"找到新闻文件: {news_file}")

    # Read the news file
    subject, body = read_news_file(news_file)
    print(f"邮件主题: {subject}")

    # Send the email
    success = send_email(subject, body)

    if success:
        print("金融快报邮件发送完成！")
    else:
        print("邮件发送失败，请检查配置")

if __name__ == "__main__":
    main()