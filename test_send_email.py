#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试邮件发送脚本
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_test_email():
    """发送测试邮件"""

    # 邮件配置
    smtp_server = "smtp.qq.com"
    port = 465
    sender_email = "1372943709@qq.com"
    receiver_email = "1372943709@qq.com"
    password = input("请输入您的QQ邮箱授权码: ")

    # 读取测试邮件内容
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"financial_news_{today}.txt"

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 解析邮件内容
        lines = content.split('\n')
        subject_line = lines[0]
        body_content = '\n'.join(lines[2:])  # 跳过Subject行和空行

        # 创建邮件
        message = MIMEMultipart("alternative")
        message["Subject"] = subject_line.replace("Subject: ", "")
        message["From"] = sender_email
        message["To"] = receiver_email

        # 添加纯文本内容
        text_part = MIMEText(body_content, "plain", "utf-8")
        message.attach(text_part)

        # 创建安全连接并发送邮件
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print("[SUCCESS] 测试邮件发送成功！")
        print(f"[INFO] 邮件已发送到: {receiver_email}")
        print("[INFO] 请检查您的邮箱确认收到测试邮件")

    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        print("可能的原因：")
        print("1. 授权码错误")
        print("2. 网络连接问题")
        print("3. 邮箱配置问题")

if __name__ == "__main__":
    print("[INFO] 开始发送测试邮件...")
    print("=" * 50)
    send_test_email()