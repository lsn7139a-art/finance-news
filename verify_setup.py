#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目设置验证脚本
检查所有必要文件是否存在且配置正确
"""

import os
import json
from datetime import datetime

def verify_project_setup():
    """验证项目设置是否完整"""
    print("[INFO] 开始验证项目设置...")
    print("=" * 50)

    # 必需文件列表
    required_files = [
        'financial_news_generator.py',
        '.github/workflows/financial_news_email.yml',
        'config.json',
        'README.md'
    ]

    # 检查必需文件
    print("[STEP] 检查必需文件:")
    all_files_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"[OK] {file}")
        else:
            print(f"[ERROR] {file} - 缺失")
            all_files_exist = False

    # 检查配置文件
    print("\n[STEP] 检查配置文件:")
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)

        # 检查必要配置项
        required_configs = [
            'email.to_address',
            'schedule.timezone',
            'news_sources.a_share.count',
            'news_sources.us_share.count',
            'news_sources.crypto.count'
        ]

        config_valid = True
        for config_path in required_configs:
            keys = config_path.split('.')
            value = config
            try:
                for key in keys:
                    value = value[key]
                print(f"[OK] {config_path}: {value}")
            except KeyError:
                print(f"[ERROR] {config_path}: 配置缺失")
                config_valid = False

    except Exception as e:
        print(f"❌ 配置文件读取错误: {e}")
        config_valid = False

    # 检查Python脚本语法
    print("\n[STEP] 检查Python脚本:")
    try:
        with open('financial_news_generator.py', 'r', encoding='utf-8') as f:
            script_content = f.read()

        # 检查必要的函数
        required_functions = [
            'class FinancialNewsGenerator',
            'def get_a_share_news',
            'def get_us_share_news',
            'def get_crypto_news',
            'def generate_email_content'
        ]

        script_valid = True
        for func in required_functions:
            if func in script_content:
                print(f"[OK] {func}")
            else:
                print(f"[ERROR] {func} - 缺失")
                script_valid = False

    except Exception as e:
        print(f"❌ 脚本文件读取错误: {e}")
        script_valid = False

    # 检查GitHub Action文件
    print("\n[STEP] 检查GitHub Action配置:")
    try:
        with open('.github/workflows/financial_news_email.yml', 'r', encoding='utf-8') as f:
            action_content = f.read()

        # 检查必要配置
        action_checks = [
            'cron: \'0 1 * * *\'',
            'dawidd6/action-send-mail@v3',
            'secrets.EMAIL_USERNAME',
            'secrets.EMAIL_PASSWORD'
        ]

        action_valid = True
        for check in action_checks:
            if check in action_content:
                print(f"[OK] {check}")
            else:
                print(f"[ERROR] {check} - 缺失")
                action_valid = False

    except Exception as e:
        print(f"❌ Action文件读取错误: {e}")
        action_valid = False

    # 生成测试邮件
    print("\n[STEP] 测试邮件生成:")
    try:
        import subprocess
        result = subprocess.run(['python', 'financial_news_generator.py'],
                              capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            print("[OK] 邮件生成脚本运行成功")

            # 检查生成的文件
            today = datetime.now().strftime("%Y-%m-%d")
            filename = f"financial_news_{today}.txt"
            if os.path.exists(filename):
                print(f"[OK] 邮件文件已生成: {filename}")

                # 检查文件内容
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()

                if '【今日金融快报】' in content and '祝您投资顺利' in content:
                    print("[OK] 邮件格式正确")
                else:
                    print("[ERROR] 邮件格式有问题")
                    action_valid = False
            else:
                print("[ERROR] 邮件文件未生成")
                action_valid = False
        else:
            print(f"[ERROR] 邮件生成失败: {result.stderr}")
            action_valid = False

    except Exception as e:
        print(f"❌ 测试运行错误: {e}")
        action_valid = False

    # 总结
    print("\n" + "=" * 50)
    print("[RESULT] 验证结果总结:")

    if all_files_exist and config_valid and script_valid and action_valid:
        print("[SUCCESS] 恭喜！项目设置完整，可以正常部署！")
        print("\n[NEXT] 下一步操作:")
        print("1. 创建GitHub仓库")
        print("2. 上传所有文件")
        print("3. 配置GitHub Secrets")
        print("4. 启用GitHub Action")
        print("\n[DOC] 详细步骤请参考: DEPLOYMENT.md")
        return True
    else:
        print("[ERROR] 项目设置存在问题，请检查以上错误")
        print("\n[FIX] 需要修复的问题:")
        if not all_files_exist:
            print("- 缺失必需文件")
        if not config_valid:
            print("- 配置文件有问题")
        if not script_valid:
            print("- Python脚本有问题")
        if not action_valid:
            print("- GitHub Action配置有问题")
        return False

if __name__ == "__main__":
    verify_project_setup()