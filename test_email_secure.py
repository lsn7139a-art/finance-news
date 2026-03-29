#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安全的邮件测试脚本
使用环境变量获取邮箱配置，避免硬编码敏感信息
"""

import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def get_email_config():
    """从环境变量获取邮箱配置"""
    return {
        'host': os.environ.get('EMAIL_HOST', 'smtp.qq.com'),
        'port': int(os.environ.get('EMAIL_PORT', 465)),
        'username': os.environ.get('EMAIL_HOST_USER'),
        'password': os.environ.get('EMAIL_HOST_PASSWORD'),
        'recipient': os.environ.get('RECIPIENT_EMAIL', '1372943709@qq.com')
    }

def send_test_email():
    """发送测试邮件"""
    config = get_email_config()

    # 检查必要的配置
    if not config['username'] or not config['password']:
        print("错误：请设置环境变量 EMAIL_HOST_USER 和 EMAIL_HOST_PASSWORD")
        print("或者直接在代码中配置邮箱信息")
        return False

    # 读取生成的新闻文件或使用默认内容
    try:
        with open('financial_news_2026-03-29.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.split('\n')
        subject = lines[0].replace('Subject: ', '') if lines[0].startswith('Subject:') else f"【今日金融快报】{datetime.now().strftime('%Y-%m-%d')} - 测试邮件"
        body = '\n'.join(lines[2:]) if len(lines) > 2 else content
    except FileNotFoundError:
        subject = f"【今日金融快报】{datetime.now().strftime('%Y-%m-%d')} - 测试邮件"
        body = """您好，这是一封测试邮件。

我们正在测试金融快报邮件发送功能。
如果收到此邮件，说明邮件发送功能正常工作。

祝您投资顺利，日常请关注风险。
"""

    # 创建邮件
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = config['username']
    message["To"] = config['recipient']

    # 添加邮件正文
    part1 = MIMEText(body, "plain", "utf-8")
    message.attach(part1)

    # 发送邮件
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config['host'], config['port'], context=context) as server:
            server.login(config['username'], config['password'])
            server.sendmail(config['username'], config['recipient'], message.as_string())
        print("测试邮件发送成功！")
        print(f"邮件已发送至: {config['recipient']}")
        print(f"邮件主题: {subject}")
        return True
    except Exception as e:
        print(f"邮件发送失败: {e}")
        print("请检查以下配置:")
        print("1. 邮箱地址是否正确")
        print("2. 授权码是否正确")
        print("3. SMTP服务器设置是否正确")
        return False

def main():
    print("=== 安全的邮件测试脚本 ===")
    print("")
    print("此脚本使用环境变量获取邮箱配置，避免硬编码敏感信息")
    print("")
    print("配置方法：")
    print("1. 设置环境变量（推荐）：")
    print("   export EMAIL_HOST_USER='1372943709@qq.com'")
    print("   export EMAIL_HOST_PASSWORD='your_authorization_code'")
    print("   export RECIPIENT_EMAIL='1372943709@qq.com'")
    print("")
    print("2. 或者在代码中直接配置（不推荐）")
    print("")

    input("按回车键开始发送测试邮件...")
    send_test_email()

if __name__ == "__main__":
    main()