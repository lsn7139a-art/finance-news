#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试邮件格式和内容
"""

import os
from datetime import datetime

def test_email_format():
    """测试邮件格式是否正确"""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"financial_news_{today}.txt"

    if not os.path.exists(filename):
        print(f"错误：未找到文件 {filename}")
        return False

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    print("邮件格式检查：")
    print("=" * 50)

    # 检查主题
    lines = content.split('\n')
    if lines[0].startswith('Subject: 【今日金融快报】'):
        print("[OK] 邮件主题格式正确")
    else:
        print("[ERROR] 邮件主题格式错误")

    # 检查问候语
    if '您好，以下为今天' in content and '的金融资讯快报，请查收' in content:
        print("[OK] 问候语格式正确")
    else:
        print("[ERROR] 问候语格式错误")

    # 检查资讯数量
    news_count = content.count('原文链接：')
    if news_count == 10:
        print(f"[OK] 资讯数量正确：{news_count}条")
    else:
        print(f"[ERROR] 资讯数量错误：{news_count}条（应为10条）")

    # 检查投资建议
    advice_count = content.count('投资建议：')
    if advice_count == 10:
        print(f"[OK] 投资建议数量正确：{advice_count}个")
    else:
        print(f"[ERROR] 投资建议数量错误：{advice_count}个（应为10个）")

    # 检查风险提示
    risk_count = content.count('**风险提示**')
    if risk_count == 10:
        print(f"[OK] 风险提示数量正确：{risk_count}个")
    else:
        print(f"[ERROR] 风险提示数量错误：{risk_count}个（应为10个）")

    # 检查结尾
    if '祝您投资顺利，日常请关注风险' in content:
        print("[OK] 结尾格式正确")
    else:
        print("[ERROR] 结尾格式错误")

    # 检查市场分类
    a_share_keywords = ['A股', '银行', '新能源', '房地产', '科技股']
    us_share_keywords = ['美联储', '特斯拉', 'Meta', '美股']
    crypto_keywords = ['比特币', '以太坊', '加密货币', 'SEC']

    a_share_count = sum(1 for keyword in a_share_keywords if keyword in content)
    us_share_count = sum(1 for keyword in us_share_keywords if keyword in content)
    crypto_count = sum(1 for keyword in crypto_keywords if keyword in content)

    print(f"\n市场分类检查：")
    print(f"A股相关：{a_share_count}个关键词")
    print(f"美股相关：{us_share_count}个关键词")
    print(f"加密货币相关：{crypto_count}个关键词")

    print("\n" + "=" * 50)
    print("邮件格式检查完成！")

    return True

if __name__ == "__main__":
    test_email_format()