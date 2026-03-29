#!/bin/bash
# GitHub部署脚本

echo "=== 金融快报系统GitHub部署脚本 ==="
echo ""

# 检查git是否安装
if ! command -v git &> /dev/null; then
    echo "错误：Git未安装，请先安装Git"
    exit 1
fi

echo "1. 初始化Git仓库..."
git init
if [ $? -eq 0 ]; then
    echo "✓ Git仓库初始化成功"
else
    echo "✗ Git仓库初始化失败"
    exit 1
fi

echo ""
echo "2. 添加文件到Git..."
git add .
if [ $? -eq 0 ]; then
    echo "✓ 文件添加成功"
else
    echo "✗ 文件添加失败"
    exit 1
fi

echo ""
echo "3. 提交代码..."
git commit -m "初始化金融快报系统"
if [ $? -eq 0 ]; then
    echo "✓ 代码提交成功"
else
    echo "✗ 代码提交失败"
    exit 1
fi

echo ""
echo "4. 设置主分支..."
git branch -M main
if [ $? -eq 0 ]; then
    echo "✓ 主分支设置成功"
else
    echo "✗ 主分支设置失败"
    exit 1
fi

echo ""
echo "=== 部署准备完成 ==="
echo ""
echo "请按照以下步骤完成GitHub部署："
echo ""
echo "步骤1：在GitHub上创建新仓库"
echo "  - 访问 https://github.com/new"
echo "  - 仓库名称：financial-news-digest"
echo "  - 选择Private（私密仓库）"
echo "  - 点击Create repository"
echo ""
echo "步骤2：连接本地仓库到GitHub"
echo "  在终端中执行以下命令（替换YOUR_USERNAME）："
echo "  git remote add origin https://github.com/YOUR_USERNAME/financial-news-digest.git"
echo "  git push -u origin main"
echo ""
echo "步骤3：配置GitHub Secrets"
echo "  在GitHub仓库中："
echo "  - 进入Settings → Secrets and variables → Actions"
echo "  - 添加以下5个Secrets："
echo "    * EMAIL_HOST_USER: 1372943709@qq.com"
echo "    * EMAIL_HOST_PASSWORD: rdwczjrfwdnkbagj"
echo "    * EMAIL_HOST: smtp.qq.com"
echo "    * EMAIL_PORT: 465"
echo "    * RECIPIENT_EMAIL: 1372943709@qq.com"
echo ""
echo "步骤4：启用GitHub Actions"
echo "  - 进入仓库Actions页面"
echo "  - 启用工作流"
echo "  - 手动运行一次测试"
echo ""
echo "部署完成后，系统将在每天北京时间9:00自动发送金融快报！"
echo ""
echo "详细部署指南请查看：DEPLOYMENT.md"