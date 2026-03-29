@echo off
echo 正在准备GitHub部署...
echo.

:: 检查Git是否安装
git --version >nul 2>&1
if errorlevel 1 (
    echo 错误：Git未安装
    echo 请先安装Git：https://git-scm.com/download/win
    pause
    exit /b 1
)

echo 1. Git已安装

:: 获取GitHub用户名
set /p github_username=请输入您的GitHub用户名:

:: 获取仓库URL
set repo_url=https://github.com/%github_username%/financial-news.git

echo.
echo 2. 仓库URL: %repo_url%
echo.

:: 初始化Git仓库
echo 3. 初始化本地Git仓库...
git init
if errorlevel 1 (
    echo 错误：Git初始化失败
    pause
    exit /b 1
)

:: 配置Git用户信息
echo 4. 配置Git用户信息...
git config user.name "%github_username%"
git config user.email "1372943709@qq.com"

:: 添加所有文件
echo 5. 添加项目文件...
git add .
if errorlevel 1 (
    echo 错误：添加文件失败
    pause
    exit /b 1
)

:: 提交代码
echo 6. 提交代码...
git commit -m "初始化金融资讯邮件生成系统

- 添加主程序脚本
- 配置GitHub Action工作流
- 添加配置文件和文档

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
if errorlevel 1 (
    echo 错误：提交代码失败
    pause
    exit /b 1
)

:: 添加远程仓库
echo 7. 添加远程仓库...
git remote add origin %repo_url%
if errorlevel 1 (
    echo 错误：添加远程仓库失败
    pause
    exit /b 1
)

:: 推送到GitHub
echo 8. 推送到GitHub...
git branch -M main
git push -u origin main
if errorlevel 1 (
    echo 错误：推送失败
    echo 可能原因：
    echo 1. GitHub用户名或仓库名错误
    echo 2. 需要GitHub个人访问令牌
    echo 3. 网络连接问题
    pause
    exit /b 1
)

echo.
echo ====================================
echo ✅ 文件上传成功！
echo ====================================
echo.
echo 下一步操作：
echo 1. 配置GitHub Secrets
echo 2. 启用GitHub Action
echo.
echo 详细步骤请参考：DEPLOYMENT.md
pause