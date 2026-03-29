# 快速开始指南 🚀

## 3分钟快速部署

### 步骤1：准备GitHub仓库
1. 在GitHub创建新仓库
2. 克隆到本地：`git clone https://github.com/你的用户名/financial-news.git`
3. 复制所有项目文件到仓库目录

### 步骤2：获取QQ邮箱授权码
1. 登录QQ邮箱网页版
2. 设置 → 账户 → POP3/SMTP服务
3. 开启服务并获取16位授权码

### 步骤3：配置GitHub Secrets
在仓库设置中添加：
- `EMAIL_USERNAME` = 你的QQ邮箱地址
- `EMAIL_PASSWORD` = 16位授权码

### 步骤4：启用工作流
1. 进入仓库Actions页面
2. 启用"金融快报邮件发送"工作流
3. 完成！系统将在每天9:00自动运行

## 项目文件说明

| 文件名 | 用途 | 是否必需 |
|--------|------|----------|
| `financial_news_generator.py` | 主程序脚本 | ✅ 必需 |
| `.github/workflows/financial_news_email.yml` | GitHub Action配置 | ✅ 必需 |
| `config.json` | 配置文件 | ✅ 必需 |
| `README.md` | 详细说明 | 📖 推荐 |
| `DEPLOYMENT.md` | 部署指南 | 📖 推荐 |
| `PROJECT_SUMMARY.md` | 项目摘要 | 📖 可选 |
| `test_email_format.py` | 测试脚本 | 🧪 可选 |

## 预期效果

✅ **每天9:00** 收到一封邮件
📧 **邮件主题**：【今日金融快报】YYYY-MM-DD
📊 **内容包含**：10条专业金融资讯
🔗 **每条资讯**：标题+摘要+链接+分析+建议
⚠️ **风险提示**：每条建议都包含风险提醒

## 自定义设置

### 修改接收邮箱
编辑 `config.json`：
```json
{
  "email": {
    "to_address": "你的邮箱@qq.com"
  }
}
```

### 修改发送时间
编辑 `.github/workflows/financial_news_email.yml`：
```yaml
cron: '0 1 * * *'  # 修改此处的cron表达式
```

## 常见问题

❓ **收不到邮件？**
- 检查GitHub Secrets配置
- 确认QQ邮箱授权码正确
- 查看Actions运行日志

❓ **时间不对？**
- GitHub使用UTC时间
- `0 1 * * *` = UTC 1:00 = 北京时间9:00

❓ **如何测试？**
```bash
python financial_news_generator.py
python test_email_format.py
```

## 技术支持

📖 **详细文档**：查看 `README.md`
🛠️ **部署指南**：查看 `DEPLOYMENT.md`
📋 **项目概览**：查看 `PROJECT_SUMMARY.md`

## 重要提醒

⚠️ **投资有风险**：本系统提供的建议仅供参考
🔒 **保护隐私**：不要在代码中硬编码敏感信息
⏰ **时间准确**：确保时区设置正确

---

**恭喜！** 🎉 您已成功创建了一个专业的金融资讯自动化系统。系统将在每天北京时间9:00为您发送精心整理的金融快报，助您把握市场脉搏！

**下一步**：按照上述步骤完成部署，享受自动化金融资讯服务！