#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单邮件测试脚本
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from datetime import datetime

def send_test_email():
    """发送测试邮件"""

    print("邮件配置信息：")
    print("SMTP服务器: smtp.qq.com")
    print("端口: 465")
    print("发送邮箱: 1372943709@qq.com")
    print("接收邮箱: 1372943709@qq.com")
    print()

    # 获取授权码
    password = input("请输入QQ邮箱授权码: ")

    try:
        # 读取测试邮件内容
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"financial_news_{today}.txt"

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # 解析邮件内容
        lines = content.split('\n')
        subject = lines[0].replace("Subject: ", "")
        body = '\n'.join(lines[2:])

        # 邮件配置
        smtp_server = "smtp.qq.com"
        port = 465
        sender_email = "1372943709@qq.com"
        receiver_email = "1372943709@qq.com"

        # 创建邮件
        message = MIMEText(body, "plain", "utf-8")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        print("正在连接邮件服务器...")

        # 发送邮件
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            print("正在登录邮箱...")
            server.login(sender_email, password)
            print("正在发送邮件...")
            server.sendmail(sender_email, receiver_email, message.as_string())

        print()
        print("=" * 60)
        print("[成功] 测试邮件已发送！")
        print(f"[信息] 发送时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"[信息] 发送到: {receiver_email}")
        print("[提示] 请检查您的QQ邮箱收件箱")
        print("[注意] 如果没收到，请检查垃圾邮件箱")
        print("=" * 60)

    except Exception as e:
        print()
        print("[错误] 邮件发送失败")
        print(f"错误信息: {e}")
        print()
        print("可能的原因:")
        print("1. 授权码错误或已过期")
        print("2. 网络连接问题")
        print("3. 邮箱安全设置阻止")
        print("4. 防火墙阻止SMTP连接")
        print()
        print("解决方案:")
        print("1. 重新生成QQ邮箱授权码")
        print("2. 检查网络连接")
        print("3. 暂时关闭防火墙测试")
        print("4. 使用其他网络环境")

if __name__ == "__main__":
    print("今日金融资讯邮件测试")
    print("=" * 60)
    send_test_email()