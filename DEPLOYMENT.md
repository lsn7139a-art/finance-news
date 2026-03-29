# 部署指南

## 快速开始

### 1. 创建GitHub仓库

```bash
# 1. 在GitHub上创建新的仓库
# 2. 克隆仓库到本地
git clone https://github.com/your-username/financial-news.git
cd financial-news
```

### 2. 上传文件

将所有项目文件上传到仓库：
- `financial_news_generator.py`
- `.github/workflows/financial_news_email.yml`
- `config.json`
- `README.md`
- `DEPLOYMENT.md`

### 3. 配置GitHub Secrets

在GitHub仓库设置中添加以下Secrets：

1. 进入仓库 → Settings → Secrets and variables → Actions
2. 点击 "New repository secret"
3. 添加以下Secrets：

   **EMAIL_HOST_USER**
   - 名称：`EMAIL_HOST_USER`
   - 值：`1372943709@qq.com`

   **EMAIL_HOST_PASSWORD**
   - 名称：`EMAIL_HOST_PASSWORD`
   - 值：`rdwczjrfwdnkbagj`

   **EMAIL_HOST**
   - 名称：`EMAIL_HOST`
   - 值：`smtp.qq.com`

   **EMAIL_PORT**
   - 名称：`EMAIL_PORT`
   - 值：`465`

   **RECIPIENT_EMAIL**
   - 名称：`RECIPIENT_EMAIL`
   - 值：`1372943709@qq.com`

### 4. 获取QQ邮箱授权码

1. 登录QQ邮箱网页版（mail.qq.com）
2. 点击右上角设置图标 → 账户
3. 找到 "POP3/SMTP服务" 部分
4. 点击 "开启" 按钮
5. 按照提示完成身份验证
6. 获取16位授权码（请妥善保存）

### 5. 启用GitHub Action

1. 在GitHub仓库中点击 "Actions" 标签
2. 找到 "金融快报邮件发送" 工作流
3. 点击 "Enable workflow" 启用

## 验证部署

### 手动测试

1. **手动触发工作流**：
   - 进入Actions页面
   - 选择工作流
   - 点击 "Run workflow" → "Run workflow"

2. **检查运行结果**：
   - 查看工作流运行状态
   - 检查是否有错误信息
   - 确认邮件是否成功发送

### 本地测试

```bash
# 在本地运行脚本测试
python financial_news_generator.py
python test_email_format.py
```

## 时间安排

- **发送时间**：北京时间每天9:00
- **GitHub Action时区**：已配置为UTC+8（Asia/Shanghai）
- **cron表达式**：`0 1 * * *`（UTC时间1:00 = 北京时间9:00）

## 故障排查

### 常见问题

1. **邮件发送失败**
   - 检查EMAIL_USERNAME和EMAIL_PASSWORD是否正确
   - 确认QQ邮箱授权码是否有效
   - 检查SMTP服务器设置

2. **工作流不运行**
   - 确认GitHub Action已启用
   - 检查工作流文件语法是否正确
   - 查看GitHub Actions运行日志

3. **时间不准确**
   - 确认cron表达式是否正确
   - 检查时区设置
   - GitHub Actions使用UTC时间，注意转换

### 日志查看

1. 进入GitHub仓库的Actions页面
2. 选择最近的工作流运行
3. 查看每个步骤的执行日志
4. 根据错误信息进行修复

## 自定义配置

### 修改配置文件

编辑 `config.json` 文件：

```json
{
  "email": {
    "to_address": "1372943709@qq.com",  // 修改接收邮箱
    "smtp_server": "smtp.qq.com",
    "smtp_port": 465
  },
  "schedule": {
    "timezone": "Asia/Shanghai",
    "hour": 9,  // 修改发送时间
    "minute": 0
  }
}
```

### 修改工作流时间

编辑 `.github/workflows/financial_news_email.yml`：

```yaml
schedule:
  # 修改cron表达式
  - cron: '0 1 * * *'  # 格式：分钟 小时 日 月 周
```

常用cron表达式：
- `0 1 * * *` - 每天UTC时间1:00（北京时间9:00）
- `0 8 * * *` - 每天UTC时间8:00（北京时间16:00）
- `0 0 * * 1-5` - 工作日UTC时间0:00（北京时间8:00）

## 监控与维护

### 日常监控

1. **检查发送状态**：
   - 每天9:00后检查邮件是否收到
   - 查看GitHub Actions运行状态

2. **内容质量检查**：
   - 确认资讯数量是否正确（10条）
   - 检查链接是否有效
   - 验证投资建议是否包含风险提示

### 定期维护

1. **更新资讯源**：
   - 定期检查和更新资讯来源
   - 确保链接的有效性和权威性

2. **优化内容**：
   - 根据市场变化调整资讯分类
   - 改进摘要撰写质量
   - 更新投资建议模板

3. **系统更新**：
   - 定期更新Python依赖
   - 优化代码性能和可靠性

## 安全注意事项

1. **保护邮箱授权码**：
   - 不要在代码中硬编码敏感信息
   - 使用环境变量或GitHub Secrets
   - 定期更换授权码

2. **数据备份**：
   - 定期备份配置文件
   - 保存重要的运行日志
   - 记录系统配置变更

3. **访问控制**：
   - 限制仓库访问权限
   - 审核代码变更
   - 监控异常活动

## 联系支持

如遇到问题，请检查：
1. 本部署指南的故障排查部分
2. GitHub Actions官方文档
3. QQ邮箱SMTP设置文档

如需进一步帮助，请提供：
- 错误日志
- 配置文件（隐藏敏感信息）
- 问题描述和重现步骤