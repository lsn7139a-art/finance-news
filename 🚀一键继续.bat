@echo off
color 0A
cls
echo.
echo          ************************************
echo          *    金融快报系统部署助手    *
echo          ************************************
echo.
echo  当前进度：80%% 完成
 剩余工作：配置GitHub Secrets + 启用Actions
 预计时间：5-10分钟

echo.
echo  按任意键开始继续部署...
pause > nul

:step1
cls
echo.
echo  [步骤 1/3] 配置GitHub Secrets
 echo  ===================================
 echo.
echo  即将打开配置页面...
echo  请添加以下5个Secrets：
echo.
echo  ✓ EMAIL_HOST_USER = 1372943709@qq.com
 ✓ EMAIL_HOST_PASSWORD = rdwczjrfwdnkbagj
 ✓ EMAIL_HOST = smtp.qq.com
 ✓ EMAIL_PORT = 465
 ✓ RECIPIENT_EMAIL = 1372943709@qq.com
 echo.
start "" "https://github.com/lsn7139a-art/finance-news/settings/secrets/actions"
echo  配置页面已打开！
echo.
echo  请在浏览器中完成配置，然后返回此处按任意键继续...
pause > nul

:step2
cls
echo.
echo  [步骤 2/3] 启用GitHub Actions
 echo  ===============================
 echo.
echo  即将打开Actions页面...
 echo.
start "" "https://github.com/lsn7139a-art/finance-news/actions"
echo  Actions页面已打开！
echo.
echo  请在浏览器中：
 echo  1. 点击"Enable workflow"
 echo  2. 点击"Run workflow" → "Run workflow"
 echo  3. 等待运行完成（约2-3分钟）
 echo.
echo  完成上述操作后，按任意键继续...
pause > nul

:step3
cls
echo.
echo  [步骤 3/3] 验证部署结果
 echo  ===============================
 echo.
echo  请检查：
echo  1. 您的邮箱(1372943709@qq.com)是否收到测试邮件
 echo  2. GitHub Actions运行状态是否为"成功"
 echo  3. 邮件内容是否包含15条金融资讯
 echo.
echo  如果遇到问题，请按1查看帮助文档
 如果一切正常，请按2完成部署
 echo.
set /p choice=请输入选择(1或2)：
if "%choice%"=="1" goto help
tif "%choice%"=="2" goto complete
goto step3

:help
start "" "https://github.com/lsn7139a-art/finance-news/blob/main/DEPLOYMENT.md"
echo.
echo  帮助文档已打开，请参考解决...
echo.
echo  按任意键返回验证步骤...
pause > nul
goto step3

:complete
cls
echo.
echo          ************************************
echo          *        🎉 部署完成！ 🎉        *
echo          ************************************
echo.
echo  恭喜！您的金融快报系统已成功部署：
echo.
echo  ✓ 每天北京时间9:00自动发送
 ✓ 15条精选金融资讯（A股+美股+加密货币）
 ✓ 中英双语显示
 ✓ 完整的投资建议和风险提示
 ✓ 发送至：1372943709@qq.com
 echo.
echo  系统将在明天上午9:00发送第一封快报！
echo.
echo  感谢您的使用，祝您投资顺利！
echo.
echo  按任意键退出...
pause > nul
exit