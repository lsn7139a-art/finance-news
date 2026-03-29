# 安全配置指南

## 🔒 安全最佳实践

### 1. GitHub Secrets配置

**推荐方式**：使用GitHub Secrets存储敏感信息

1. 进入仓库 → Settings → Secrets and variables → Actions
2. 添加以下Secrets：

   | Name | Value | 说明 |
   |------|-------|------|
   | `EMAIL_HOST_USER` | `1372943709@qq.com` | 发件邮箱 |
   | `EMAIL_HOST_PASSWORD` | `your_authorization_code` | QQ邮箱授权码 |
   | `EMAIL_HOST` | `smtp.qq.com` | SMTP服务器 |
   | `EMAIL_PORT` | `465` | SMTP端口 |
   | `RECIPIENT_EMAIL` | `1372943709@qq.com` | 收件邮箱 |

### 2. 环境变量配置（本地测试）

**Windows**:
```cmd
set EMAIL_HOST_USER=1372943709@qq.com
set EMAIL_HOST_PASSWORD=your_authorization_code
set RECIPIENT_EMAIL=1372943709@qq.com
python test_email_secure.py
```

**Linux/Mac**:
```bash
export EMAIL_HOST_USER="1372943709@qq.com"
export EMAIL_HOST_PASSWORD="your_authorization_code"
export RECIPIENT_EMAIL="1372943709@qq.com"
python test_email_secure.py
```

### 3. 避免的安全风险

#### ❌ 不要这样做：
- 在代码中硬编码邮箱密码或授权码
- 将包含敏感信息的文件提交到Git仓库
- 在公开的文档中显示授权码
- 使用邮箱主密码，而应该使用授权码

#### ✅ 正确的做法：
- 使用GitHub Secrets存储敏感信息
- 使用环境变量在本地测试
- 使用应用专用授权码（不是邮箱密码）
- 定期更换授权码

## 🛡️ 授权码安全

### 获取QQ邮箱授权码

1. 登录QQ邮箱网页版 (mail.qq.com)
2. 进入"设置" → "账户"
3. 找到"POP3/SMTP服务"
4. 点击"开启"并按照提示操作
5. **重要**：记录授权码并妥善保管

### 授权码管理

1. **定期更换**：建议每3-6个月更换一次授权码
2. **最小权限**：只授予必要的权限
3. **及时撤销**：如果怀疑授权码泄露，立即在QQ邮箱设置中关闭并重新生成

## 🔍 安全检查清单

- [ ] 没有在代码中硬编码敏感信息
- [ ] 所有敏感信息都存储在GitHub Secrets中
- [ ] 使用私密仓库（Private repository）
- [ ] 定期检查GitHub安全警报
- [ ] 授权码定期更换
- [ ] 不在公共场合显示授权码

## 🚨 如果授权码泄露

1. **立即行动**：
   - 登录QQ邮箱
   - 进入设置 → 账户
   - 关闭POP3/SMTP服务
   - 重新开启并生成新的授权码

2. **更新配置**：
   - 更新GitHub Secrets中的`EMAIL_HOST_PASSWORD`
   - 更新本地环境变量（如果有）
   - 测试新的授权码是否工作

3. **检查日志**：
   - 查看GitHub Actions运行日志
   - 确认没有异常活动

## 📞 安全支持

如果发现安全问题：
1. 立即更改授权码
2. 检查GitHub安全警报
3. 查看Actions运行日志
4. 如有必要，联系QQ邮箱客服

---

**记住：保护好您的授权码，就像保护您的密码一样重要！**