@echo off
cls
echo ======================================
echo    金融快报系统 - 继续部署
echo ======================================
echo.
echo 当前状态：80%% 完成
echo 剩余工作：配置GitHub Secrets + 启用Actions
echo.
echo 按任意键查看部署指南...
pause > nul

start https://github.com/lsn7139a-art/finance-news/blob/main/MEMORY.md
echo.
echo 已打开记忆点文档，请查看后续步骤...
echo.
echo 接下来请按任意键继续...
pause > nul

cls
echo ======================================
echo    第一步：配置GitHub Secrets
echo ======================================
echo.
echo 即将打开GitHub Secrets配置页面...
echo 请添加以下5个Secrets：
echo.
echo 1. EMAIL_HOST_USER = 1372943709@qq.com
echo 2. EMAIL_HOST_PASSWORD = rdwczjrfwdnkbagj
echo 3. EMAIL_HOST = smtp.qq.com
echo 4. EMAIL_PORT = 465
echo 5. RECIPIENT_EMAIL = 1372943709@qq.com
echo.
start https://github.com/lsn7139a-art/finance-news/settings/secrets/actions
echo 已打开Secrets配置页面！
echo.
echo 配置完成后按任意键继续...
pause > nul

cls
echo ======================================
echo    第二步：启用GitHub Actions
echo ======================================
echo.
echo 即将打开GitHub Actions页面...
echo.
start https://github.com/lsn7139a-art/finance-news/actions
echo 已打开Actions页面！
echo.
echo 请在浏览器中：
echo 1. 点击"Enable workflow"
echo 2. 点击"Run workflow" → "Run workflow"
echo 3. 等待运行完成
echo.
echo 启用完成后按任意键继续...
pause > nul

cls
echo ======================================
echo    第三步：验证结果
echo ======================================
echo.
echo 请检查：
echo 1. 邮箱是否收到测试邮件
echo 2. Actions运行状态是否为成功
echo 3. 邮件内容是否包含15条资讯
echo.
echo 如果一切正常，您的系统就部署完成了！
echo.
echo 按任意键打开完整部署指南...
pause > nul

start https://github.com/lsn7139a-art/finance-news/blob/main/DEPLOYMENT.md
echo.
echo 部署指南已打开！
echo.
echo ======================================
echo    部署完成！
echo ======================================
echo.
echo 您的金融快报系统将在每天北京时间9:00
echo 自动发送15条精选金融资讯到您的邮箱。
echo.
echo 感谢您的使用！
echo.
pause