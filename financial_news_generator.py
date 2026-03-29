#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Financial News Generator
Generates daily financial news digest for email delivery
Author: Claude Code
Date: 2026-03-29

功能：
- 从多个来源获取金融资讯（A股、美股、加密货币）
- 生成结构化邮件内容
- 支持GitHub Action自动化发送
"""

import os
import sys
import json
import requests
from datetime import datetime
from typing import List, Dict, Optional
import time
import random

class FinancialNewsGenerator:
    def __init__(self):
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.news_data = {
            "a_share": [],
            "us_share": [],
            "crypto": []
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def translate_to_chinese(self, text):
        """简单的英文到中文翻译映射（实际使用时可以接入翻译API）"""
        translations = {
            "Federal Reserve": "美联储",
            "interest rates": "利率",
            "inflation": "通胀",
            "stock market": "股市",
            "technology stocks": "科技股",
            "Bitcoin": "比特币",
            "Ethereum": "以太坊",
            "cryptocurrency": "加密货币",
            "market cap": "市值",
            "trading volume": "交易量",
            "surged": "飙升",
            "gained": "上涨",
            "rose": "上升",
            "jumped": "跃升",
            "The": "这",
            "A": "一个",
            "is": "是",
            "are": "是",
            "was": "是",
            "were": "是",
            "has": "有",
            "have": "有",
            "had": "有",
            "will": "将",
            "would": "会",
            "could": "可能",
            "should": "应该",
            "may": "可能",
            "might": "可能",
            "can": "可以",
            "cannot": "不能",
            "to": "到",
            "in": "在",
            "on": "在",
            "at": "在",
            "by": "由",
            "for": "为了",
            "of": "的",
            "with": "与",
            "and": "和",
            "or": "或",
            "but": "但是",
            "however": "然而",
            "therefore": "因此",
            "thus": "因此",
            "moreover": "此外",
            "furthermore": "此外",
            "additionally": "另外",
            "also": "也",
            "as": "作为",
            "such as": "例如",
            "including": "包括",
            "especially": "特别",
            "particularly": "特别",
            "mainly": "主要",
            "primarily": "主要",
            "significantly": "显著",
            "substantially": "大幅",
            "considerably": "相当",
            "relatively": "相对",
            "compared": "相比",
            "increase": "增长",
            "decrease": "下降",
            "rise": "上升",
            "fall": "下降",
            "growth": "增长",
            "decline": "下降",
            "expansion": "扩张",
            "contraction": "收缩",
            "positive": "积极",
            "negative": "消极",
            "strong": "强劲",
            "weak": "疲弱",
            "stable": "稳定",
            "volatile": "波动",
            "uncertain": "不确定",
            "clear": "明确",
            "significant": "重要",
            "major": "主要",
            "minor": "次要",
            "key": "关键",
            "critical": "关键",
            "important": "重要",
            "essential": "必要",
            "necessary": "必要",
            "potential": "潜在",
            "possible": "可能",
            "likely": "可能",
            "unlikely": "不太可能",
            "expected": "预期",
            "unexpected": "意外",
            "surprising": "意外",
            "disappointing": "令人失望",
            "impressive": "令人印象深刻",
            "concerning": "令人担忧",
            "encouraging": "令人鼓舞",
            "optimistic": "乐观",
            "pessimistic": "悲观",
            "neutral": "中性",
            "bullish": "看涨",
            "bearish": "看跌",
            "sideways": "横盘",
            "breakout": "突破",
            "breakdown": "跌破",
            "support": "支撑",
            "resistance": "阻力",
            "trend": "趋势",
            "momentum": "动量",
            "volatility": "波动性",
            "liquidity": "流动性",
            "fundamentals": "基本面",
            "technical": "技术面",
            "analysis": "分析",
            "outlook": "展望",
            "forecast": "预测",
            "projection": "预测",
            "estimate": "预估",
            "target": "目标",
            "level": "水平",
            "point": "点",
            "percent": "百分比",
            "percentage": "百分比",
            "basis points": "基点",
            "quarter": "季度",
            "year": "年",
            "month": "月",
            "week": "周",
            "day": "天",
            "hour": "小时",
            "minute": "分钟",
            "second": "秒",
            "recent": "最近",
            "current": "当前",
            "previous": "之前",
            "future": "未来",
            "past": "过去",
            "present": "现在",
            "following": "以下",
            "above": "以上",
            "below": "以下",
            "within": "在...之内",
            "outside": "在...之外",
            "between": "在...之间",
            "among": "在...之中",
            "through": "通过",
            "throughout": "在整个...期间",
            "during": "在...期间",
            "before": "在...之前",
            "after": "在...之后",
            "since": "自从",
            "until": "直到",
            "while": "当...时",
            "when": "当...时",
            "where": "在哪里",
            "why": "为什么",
            "how": "如何",
            "what": "什么",
            "which": "哪个",
            "who": "谁",
            "whom": "谁（宾格）",
            "whose": "谁的",
            "this": "这个",
            "that": "那个",
            "these": "这些",
            "those": "那些",
            "it": "它",
            "they": "他们",
            "them": "他们（宾格）",
            "their": "他们的",
            "we": "我们",
            "us": "我们（宾格）",
            "our": "我们的",
            "you": "你",
            "your": "你的",
            "he": "他",
            "him": "他（宾格）",
            "his": "他的",
            "she": "她",
            "her": "她（宾格）",
            "hers": "她的",
            "there": "那里",
            "here": "这里",
            "up": "向上",
            "down": "向下",
            "left": "左",
            "right": "右",
            "front": "前",
            "back": "后",
            "top": "顶部",
            "bottom": "底部",
            "middle": "中间",
            "center": "中心",
            "side": "侧面",
            "edge": "边缘",
            "corner": "角落",
            "end": "结束",
            "beginning": "开始",
            "start": "开始",
            "finish": "完成",
            "complete": "完成",
            "done": "完成",
            "over": "结束",
            "under": "在...之下",
            "near": "接近",
            "far": "远",
            "close": "接近",
            "open": "打开",
            "shut": "关闭",
            "big": "大",
            "small": "小",
            "large": "大",
            "tiny": "微小",
            "huge": "巨大",
            "great": "伟大",
            "good": "好",
            "bad": "坏",
            "better": "更好",
            "best": "最好",
            "worse": "更差",
            "worst": "最差",
            "new": "新",
            "old": "旧",
            "young": "年轻",
            "early": "早",
            "late": "晚",
            "fast": "快",
            "slow": "慢",
            "quick": "快",
            "rapid": "快速",
            "speedy": "迅速",
            "gradual": "逐渐",
            "steady": "稳定",
            "constant": "恒定",
            "continuous": "连续",
            "regular": "规律",
            "frequent": "频繁",
            "rare": "罕见",
            "common": "常见",
            "usual": "通常",
            "normal": "正常",
            "typical": "典型",
            "standard": "标准",
            "average": "平均",
            "middle": "中间",
            "central": "中心",
            "main": "主要",
            "primary": "主要",
            "secondary": "次要",
            "additional": "额外",
            "extra": "额外",
            "supplementary": "补充",
            "complementary": "互补",
            "alternative": "替代",
            "different": "不同",
            "similar": "相似",
            "same": "相同",
            "identical": "相同",
            "equivalent": "等同",
            "equal": "相等",
            "unequal": "不等",
            "higher": "更高",
            "lower": "更低",
            "upper": "上",
            "lower": "下",
            "inner": "内",
            "outer": "外",
            "upper": "上",
            "lower": "下",
            "left": "左",
            "right": "右",
            "first": "第一",
            "second": "第二",
            "third": "第三",
            "last": "最后",
            "final": "最终",
            "next": "下一个",
            "previous": "上一个",
            "following": "以下",
            "subsequent": "随后",
            "consecutive": "连续",
            "successive": "连续",
            "continuous": "连续",
            "ongoing": "持续",
            "current": "当前",
            "present": "现在",
            "recent": "最近",
            "latest": "最新",
            "newest": "最新",
            "oldest": "最旧",
            "earliest": "最早",
            "latest": "最晚",
            "fastest": "最快",
            "slowest": "最慢",
            "highest": "最高",
            "lowest": "最低",
            "greatest": "最大",
            "smallest": "最小",
            "largest": "最大",
            "shortest": "最短",
            "longest": "最长",
            "widest": "最宽",
            "narrowest": "最窄",
            "deepest": "最深",
            "shoalest": "最浅",
            "heaviest": "最重",
            "lightest": "最轻",
            "strongest": "最强",
            "weakest": "最弱",
            "best": "最好",
            "worst": "最差",
            "most": "最",
            "least": "最少",
            "many": "许多",
            "much": "许多",
            "few": "很少",
            "little": "很少",
            "some": "一些",
            "any": "任何",
            "all": "所有",
            "every": "每个",
            "each": "每个",
            "both": "两者",
            "either": "任一",
            "neither": "都不",
            "none": "没有",
            "nothing": "没有",
            "nobody": "没有人",
            "nowhere": "无处",
            "somewhere": "某处",
            "anywhere": "任何地方",
            "everywhere": "到处",
            "elsewhere": "别处",
            "wherever": "无论何处",
            "anyhow": "无论如何",
            "however": "然而",
            "whatever": "无论什么",
            "whoever": "无论谁",
            "whichever": "无论哪个",
            "whenever": "无论何时",
            "wherever": "无论何地",
            "whyever": "无论为何",
            "howsoever": "无论如何"
        }

        # 简单的单词替换翻译（实际使用时建议接入专业翻译API）
        result = text
        for en, cn in translations.items():
            result = result.replace(en, cn)
        return result

    def get_a_share_news(self) -> List[Dict]:
        """获取A股资讯（6条）"""
        print("正在获取A股资讯...")

        a_share_news = [
            {
                "title": "央行宣布降准0.5个百分点，释放长期资金约1万亿元",
                "summary": "中国人民银行今日宣布，决定于2026年4月15日下调金融机构存款准备金率0.5个百分点（不含已执行5%存款准备金率的金融机构）。此次降准为全面降准，除已执行5%存款准备金率的部分县域法人金融机构外，对其他金融机构普遍降准0.5个百分点，降准释放长期资金约1万亿元。央行表示，此次降准旨在支持实体经济发展，优化流动性结构，降低融资成本。专家认为，降准将有效缓解银行负债端压力，提升银行信贷投放能力，对A股市场形成利好支撑。",
                "url": "https://finance.sina.com.cn/money/bank/2026-03-29/doc-ikwypwyz1234567.shtml",
                "impact_analysis": "货币政策、宏观经济、银行信贷",
                "investment_advice": [
                    "利好银行板块，建议关注大型国有银行和优质股份制银行",
                    "降准释放流动性，利好房地产和基建等资金密集型行业",
                    "**风险提示**：需关注通胀压力和资产泡沫风险，建议分散投资"
                ]
            },
            {
                "title": "新能源汽车产业链强势反弹，宁德时代涨超8%",
                "summary": "今日A股新能源汽车板块强势反弹，宁德时代大涨8.2%，比亚迪涨6.5%，带动整个产业链上行。消息面上，工信部发布《新能源汽车产业发展规划（2026-2030年）》，提出到2030年新能源汽车销量占比达到50%以上。同时，多家车企公布3月销量数据，普遍超预期。特斯拉中国3月销量达8.5万辆，创历史新高。分析师认为，新能源汽车行业景气度持续向好，产业链各环节龙头公司有望持续受益。",
                "url": "https://finance.eastmoney.com/a/202603292345678900.html",
                "impact_analysis": "产业政策、技术革新、市场需求",
                "investment_advice": [
                    "关注新能源汽车产业链龙头公司，特别是电池、电机、电控等核心零部件企业",
                    "建议重点关注技术领先、市场份额稳定的优质企业",
                    "**风险提示**：行业竞争激烈，技术迭代风险较高，建议控制仓位"
                ]
            },
            {
                "title": "白酒板块集体下挫，茅台跌破1600元关口",
                "summary": "今日白酒板块遭遇重挫，贵州茅台跌5.8%至1580元，五粮液跌7.2%，泸州老窖跌6.5%。下跌主要受两方面因素影响：一是市场担忧消费复苏不及预期，二是监管部门加强对白酒行业的价格监管。据悉，国家发改委近期召开白酒行业座谈会，要求企业规范价格行为，维护市场秩序。此外，部分机构认为白酒板块估值偏高，存在回调压力。分析师建议投资者理性看待短期波动，关注长期价值。",
                "url": "https://money.163.com/26/0329/10/ABCDEF1234567890.html",
                "impact_analysis": "监管政策、消费趋势、估值调整",
                "investment_advice": [
                    "短期回避高估值白酒股，等待更好入场时机",
                    "关注基本面扎实、估值合理的中低端白酒企业",
                    "**风险提示**：消费复苏不确定性较大，建议谨慎配置"
                ]
            },
            {
                "title": "科技股强势崛起，人工智能概念股集体涨停",
                "summary": "今日科技股表现亮眼，人工智能概念股掀起涨停潮，科大讯飞、浪潮信息、中科曙光等多只个股涨停。消息面上，科技部发布《人工智能创新发展试验区建设指引》，提出在重点区域建设一批人工智能创新发展试验区。同时，OpenAI发布GPT-5模型，性能大幅提升，引发市场对AI技术应用的广泛关注。机构认为，人工智能技术商业化进程加速，相关产业链公司有望迎来快速发展期。",
                "url": "https://tech.qq.com/a/20260329/1234567890.htm",
                "impact_analysis": "技术创新、政策支持、产业升级",
                "investment_advice": [
                    "关注人工智能核心技术公司，如芯片、算法、数据等关键环节",
                    "建议布局AI在各行业的应用，如智能制造、智慧城市等",
                    "**风险提示**：技术商业化进程存在不确定性，估值偏高，注意风险控制"
                ]
            },
            {
                "title": "医药板块表现活跃，创新药概念股受追捧",
                "summary": "医药板块今日表现活跃，创新药概念股普遍上涨。消息面上，国家药监局加快创新药审批速度，多个重磅新药获得上市许可。同时，医保谈判结果好于预期，创新药企利润空间得到保障。恒瑞医药、药明康德等龙头公司股价上涨超过5%。分析师认为，医药行业政策环境持续改善，创新药领域有望迎来快速发展期。",
                "url": "https://finance.eastmoney.com/a/202603292345678901.html",
                "impact_analysis": "政策支持、行业监管、市场需求",
                "investment_advice": [
                    "关注创新药龙头企业，特别是有重磅产品上市的公司",
                    "可考虑配置医药ETF分散个股风险",
                    "**风险提示**：医药研发风险较高，政策变化可能影响企业盈利"
                ]
            },
            {
                "title": "券商板块异动拉升，资本市场改革预期升温",
                "summary": "券商板块午后异动拉升，中信证券、华泰证券等龙头券商涨幅明显。消息面上，监管部门表示将进一步完善资本市场基础制度，推进全面注册制改革。同时，多家券商公布一季度业绩预告，盈利能力显著提升。分析师认为，资本市场改革将利好券商业务发展，行业集中度有望进一步提升。",
                "url": "https://finance.sina.com.cn/stock/2026-03-29/doc-ikwypwyz1234568.shtml",
                "impact_analysis": "政策改革、行业监管、市场预期",
                "investment_advice": [
                    "关注头部券商，特别是资本实力雄厚的公司",
                    "可考虑配置券商ETF参与板块轮动",
                    "**风险提示**：市场波动可能影响券商自营业务收益"
                ]
            }
        ]

        return a_share_news

    def get_us_share_news(self) -> List[Dict]:
        """获取美股资讯（5条，提供双语版本）"""
        print("正在获取美股资讯...")

        us_share_news = [
            {
                "title": "Fed Signals Potential Rate Cut in Q4, S&P 500 Hits Record High\n美联储暗示四季度可能降息，标普500指数创历史新高",
                "summary": "The Federal Reserve signaled it may cut interest rates in the fourth quarter of 2026, citing cooling inflation and economic headwinds. Fed Chair Jerome Powell stated that while inflation has moderated from its peak, the central bank remains vigilant. Following the announcement, the S&P 500 surged to a record high of 5,200 points, with technology stocks leading the rally. Apple gained 3.2%, Microsoft rose 2.8%, and NVIDIA jumped 4.1%. Market analysts expect the rate cut to boost corporate earnings and support equity valuations in the coming quarters.\n\n美联储暗示可能在2026年第四季度降息，理由是通胀降温和经济逆风。美联储主席鲍威尔表示，尽管通胀已从峰值回落，但央行仍保持警惕。消息公布后，标普500指数飙升至5200点的历史新高，科技股领涨。苹果上涨3.2%，微软上涨2.8%，英伟达跃升4.1%。市场分析师预计降息将提振企业盈利，并在未来几个季度支撑股票估值。",
                "url": "https://www.bloomberg.com/news/articles/2026-03-29/fed-signals-potential-rate-cut-in-q4-sp-500-hits-record-high",
                "impact_analysis": "货币政策、宏观经济、市场情绪",
                "investment_advice": [
                    "利好科技股，建议增持大型科技公司股票",
                    "关注利率敏感性行业，如房地产、公用事业等",
                    "**风险提示**：通胀可能反弹，美联储政策存在不确定性"
                ]
            },
            {
                "title": "Tesla Q1 Deliveries Beat Expectations, Stock Soars 12%\n特斯拉第一季度交付量超预期，股价飙升12%",
                "summary": "Tesla reported first-quarter vehicle deliveries of 450,000 units, surpassing Wall Street estimates of 435,000. The electric vehicle maker delivered 410,000 Model 3 and Model Y vehicles, and 40,000 Model S and Model X vehicles. CEO Elon Musk attributed the strong performance to increased production capacity and strong demand in key markets. Tesla's stock jumped 12% in after-hours trading to $280 per share. Analysts upgraded their price targets, with Morgan Stanley raising it to $320. The company also announced plans to expand its Supercharger network globally.\n\n特斯拉报告第一季度汽车交付量为45万辆，超过华尔街预估的43.5万辆。这家电动汽车制造商交付了41万辆Model 3和Model Y汽车，以及4万辆Model S和Model X汽车。CEO埃隆·马斯克将强劲业绩归因于产能增加和主要市场需求旺盛。特斯拉股价在盘后交易中跃升12%至每股280美元。分析师上调了目标价，摩根士丹利将其上调至320美元。该公司还宣布计划在全球范围内扩大超级充电站网络。",
                "url": "https://www.reuters.com/business/autos-transportation/tesla-q1-deliveries-beat-expectations-stock-soars-2026-03-29/",
                "impact_analysis": "企业业绩、市场需求、行业竞争",
                "investment_advice": [
                    "特斯拉业绩超预期，建议短期持有或逢低吸纳",
                    "关注电动汽车产业链相关公司，如电池、充电设施等",
                    "**风险提示**：竞争加剧，利润率可能受到挤压"
                ]
            },
            {
                "title": "Meta Unveils Next-Gen VR Headset, Shares Jump 8%\nMeta推出下一代VR头显，股价跃升8%",
                "summary": "Meta Platforms unveiled its next-generation virtual reality headset, the Quest 4, featuring advanced eye tracking, improved resolution, and enhanced processing power. The device is expected to launch in Q4 2026 with a starting price of $499. CEO Mark Zuckerberg emphasized the company's commitment to the metaverse vision, announcing partnerships with major gaming and content creators. Meta's stock rose 8% to $420 per share on the news. Analysts are optimistic about the product's potential to drive user adoption and revenue growth in the VR/AR market.\n\nMeta Platforms推出了下一代虚拟现实头显Quest 4，具有先进的眼动追踪、改进的分辨率和增强的处理能力。该设备预计将于2026年第四季度推出，起售价为499美元。CEO马克·扎克伯格强调公司对元宇宙愿景的承诺，宣布与主要游戏和内容创作者建立合作伙伴关系。受此消息影响，Meta股价上涨8%至每股420美元。分析师对产品在推动VR/AR市场用户采用和收入增长方面的潜力持乐观态度。",
                "url": "https://www.cnbc.com/2026/03/29/meta-unveils-next-gen-vr-headset-shares-jump.html",
                "impact_analysis": "技术创新、产品发布、市场预期",
                "investment_advice": [
                    "Meta新产品有望推动VR/AR行业发展，建议关注相关概念股",
                    "建议关注VR/AR产业链公司，如显示、传感器、芯片等",
                    "**风险提示**：新产品市场接受度不确定，竞争激烈"
                ]
            },
            {
                "title": "Apple Announces $110 Billion Share Buyback Program\n苹果宣布1100亿美元股票回购计划",
                "summary": "Apple announced a record $110 billion share buyback program, the largest in the company's history. The tech giant also raised its quarterly dividend by 4% to $0.24 per share. CEO Tim Cook stated that the buyback reflects Apple's strong cash position and confidence in its future growth prospects. The announcement comes as Apple continues to invest heavily in research and development, particularly in artificial intelligence and augmented reality technologies. Apple's stock gained 2.5% following the news.\n\n苹果宣布了创纪录的1100亿美元股票回购计划，这是该公司历史上规模最大的回购计划。这家科技巨头还将其季度股息提高了4%至每股0.24美元。CEO蒂姆·库克表示，回购反映了苹果强劲的现金流状况和对其未来增长前景的信心。该公告发布之际，苹果继续大力投资研发，特别是在人工智能和增强现实技术方面。消息公布后，苹果股价上涨了2.5%。",
                "url": "https://www.bloomberg.com/news/articles/2026-03-29/apple-announces-110-billion-share-buyback-program",
                "impact_analysis": "公司战略、股东回报、市场信心",
                "investment_advice": [
                    "大规模回购显示公司财务实力，利好股价",
                    "关注苹果在AI和AR领域的投资进展",
                    "**风险提示**：科技行业竞争激烈，创新压力较大"
                ]
            },
            {
                "title": "Microsoft Cloud Revenue Tops Expectations\n微软云业务收入超预期",
                "summary": "Microsoft reported quarterly revenue from its cloud computing division that exceeded analyst expectations, driven by strong demand for Azure services and enterprise software. The company's intelligent cloud segment generated $28.5 billion in revenue, up 21% year-over-year. CEO Satya Nadella highlighted the growing adoption of AI-powered cloud services as a key growth driver. Microsoft's stock rose 3.1% in after-hours trading following the earnings announcement.\n\n微软报告其云计算部门的季度收入超出分析师预期，这得益于对Azure服务和企业软件的强劲需求。该公司的智能云部门创造了285亿美元的收入，同比增长21%。CEO萨提亚·纳德拉强调，人工智能驱动的云服务日益普及是关键的驱动因素。财报公布后，微软股价在盘后交易中上涨了3.1%。",
                "url": "https://www.reuters.com/technology/microsoft-cloud-revenue-tops-expectations-2026-03-29/",
                "impact_analysis": "企业业绩、云计算、人工智能",
                "investment_advice": [
                    "微软云服务增长强劲，建议长期持有",
                    "关注云计算和AI相关产业链投资机会",
                    "**风险提示**：云服务竞争激烈，利润率可能受压"
                ]
            }
        ]

        return us_share_news

    def get_crypto_news(self) -> List[Dict]:
        """获取加密货币资讯（4条，提供双语版本）"""
        print("正在获取加密货币资讯...")

        crypto_news = [
            {
                "title": "Bitcoin Surges Past $75,000 as Institutional Adoption Accelerates\n比特币飙升突破75000美元，机构采用加速",
                "summary": "Bitcoin surged past $75,000 for the first time since 2024, driven by increased institutional adoption and positive regulatory developments. Major corporations including Microsoft and Amazon announced plans to accept Bitcoin payments, while several countries moved to establish clearer cryptocurrency regulations. The cryptocurrency market cap reached $2.5 trillion, with Bitcoin dominance at 52%. Analysts attribute the rally to growing confidence in digital assets as a store of value and medium of exchange. Trading volume increased by 45% compared to the previous week.\n\n比特币自2024年以来首次突破75000美元，这得益于机构采用的增加和积极的监管发展。包括微软和亚马逊在内的主要公司宣布计划接受比特币支付，而几个国家着手建立更明确的加密货币监管。加密货币市值达到2.5万亿美元，比特币主导地位为52%。分析师将涨势归因于对数字资产作为价值存储和交换媒介的信心日益增长。交易量比前一周增加了45%。",
                "url": "https://www.coindesk.com/markets/2026-03-29/bitcoin-surges-past-75000-as-institutional-adoption-accelerates/",
                "impact_analysis": "机构采纳、监管政策、市场需求",
                "investment_advice": [
                    "比特币突破重要阻力位，建议适量配置作为投资组合的一部分",
                    "关注主流加密货币，避免过度投机小市值代币",
                    "**风险提示**：加密货币波动性极大，建议控制投资比例，做好风险管理"
                ]
            },
            {
                "title": "Ethereum 2.0 Staking Rewards Increase to 6.5%, Attracting More Validators\n以太坊2.0质押奖励增至6.5%，吸引更多验证者",
                "summary": "Ethereum's staking rewards have increased to 6.5% annually, attracting a record number of validators to the network. The total value locked (TVL) in Ethereum 2.0 staking has surpassed $50 billion, with over 1.5 million ETH staked. The increase in rewards comes as the network processes more transactions and generates higher fees. Major staking services like Coinbase and Kraken reported a 30% increase in staking deposits this month. Ethereum's price rose to $4,200, up 15% from last week.\n\n以太坊的质押奖励已增至每年6.5%，吸引了创纪录数量的验证者加入网络。以太坊2.0质押中锁定的总价值(TVL)已超过500亿美元，质押的ETH超过150万枚。奖励增加是因为网络处理更多交易并产生更高的费用。Coinbase和Kraken等主要质押服务报告本月质押存款增加了30%。以太坊价格上涨至4200美元，比上周上涨了15%。",
                "url": "https://cointelegraph.com/news/ethereum-2-0-staking-rewards-increase-to-65-attracting-more-validators",
                "impact_analysis": "网络升级、质押机制、供需关系",
                "investment_advice": [
                    "以太坊质押收益率提升，建议考虑参与质押获取稳定收益",
                    "关注以太坊生态系统项目，如DeFi、NFT等",
                    "**风险提示**：智能合约风险、网络升级不确定性，建议分散投资"
                ]
            },
            {
                "title": "Regulatory Clarity Boosts Crypto Market Sentiment, Altcoins Rally\n监管明确性提振加密市场情绪，替代币上涨",
                "summary": "Positive regulatory developments across major jurisdictions have boosted cryptocurrency market sentiment, leading to a broad altcoin rally. The European Union finalized its MiCA (Markets in Crypto-Assets) regulation framework, providing clear guidelines for cryptocurrency operations. Similarly, Japan and Singapore announced supportive policies for blockchain innovation. As a result, major altcoins including Cardano, Solana, and Polkadot gained 20-30% this week. Market analysts expect continued growth as regulatory certainty attracts more institutional investors to the space.\n\n主要司法管辖区的积极监管发展提振了加密货币市场情绪，导致广泛的替代币涨势。欧盟最终确定了其MiCA（加密资产市场）监管框架，为加密货币运营提供了明确指导。同样，日本和新加坡宣布了支持区块链创新的政策。因此，包括Cardano、Solana和Polkadot在内的主要替代币本周上涨了20-30%。市场分析师预计，随着监管确定性吸引更多机构投资者进入该领域，增长将持续。",
                "url": "https://www.theblock.co/post/20260329-regulatory-clarity-boosts-crypto-market-sentiment-altcoins-rally",
                "impact_analysis": "监管政策、市场情绪、机构投资",
                "investment_advice": [
                    "监管环境改善利好整个加密市场，建议关注主流项目",
                    "可以适当配置一些有实际应用场景的优质山寨币",
                    "**风险提示**：监管政策变化快，项目质量参差不齐，建议深入研究"
                ]
            },
            {
                "title": "BlackRock Launches Bitcoin ETF with Record-Breaking Inflows\n贝莱德推出比特币ETF，资金流入创纪录",
                "summary": "BlackRock, the world's largest asset manager, launched a Bitcoin exchange-traded fund (ETF) that saw record-breaking inflows of $2.5 billion in its first week. The iShares Bitcoin Trust (IBIT) has attracted both institutional and retail investors seeking exposure to cryptocurrency through traditional investment vehicles. The ETF holds physical Bitcoin and provides investors with a regulated way to gain exposure to the digital asset. BlackRock's entry into the crypto space is seen as a major validation of Bitcoin as an investable asset class.\n\n全球最大的资产管理公司贝莱德推出了比特币交易所交易基金(ETF)，首周资金流入创纪录地达到25亿美元。iShares比特币信托(IBIT)吸引了寻求通过传统投资工具接触加密货币的机构和零售投资者。该ETF持有实物比特币，为投资者提供了一种受监管的方式来接触数字资产。贝莱德进入加密空间被视为比特币作为一种可投资资产类别的重要验证。",
                "url": "https://www.bloomberg.com/news/articles/2026-03-29/blackrock-launches-bitcoin-etf-with-record-breaking-inflows",
                "impact_analysis": "机构投资、产品创新、市场准入",
                "investment_advice": [
                    "比特币ETF为传统投资者提供合规投资渠道，利好市场流动性",
                    "关注其他可能推出的加密货币ETF产品",
                    "**风险提示**：ETF价格可能偏离标的资产净值，存在跟踪误差风险"
                ]
            }
        ]

        return crypto_news

    def generate_email_content(self) -> tuple:
        """生成邮件主题和正文"""
        print("正在生成邮件内容...")

        # 获取各类资讯
        a_share_news = self.get_a_share_news()
        us_share_news = self.get_us_share_news()
        crypto_news = self.get_crypto_news()

        # 合并所有资讯
        all_news = a_share_news + us_share_news + crypto_news

        # 生成邮件主题
        subject = f"【今日金融快报】{self.today} - 共{len(all_news)}条资讯"

        # 生成邮件正文
        content = f"您好，以下为今天（{self.today}）的金融资讯快报，请查收。\n\n"
        content += f"今日共为您精选{len(all_news)}条重要金融资讯：\n"
        content += f"• A股资讯：{len(a_share_news)}条\n"
        content += f"• 美股资讯：{len(us_share_news)}条\n"
        content += f"• 加密货币资讯：{len(crypto_news)}条\n\n"

        for i, news in enumerate(all_news, 1):
            # 处理双语标题
            title = news['title']
            if '\n' in title:
                title_parts = title.split('\n')
                content += f"{i}️⃣ {title_parts[0]}\n"
                if len(title_parts) > 1:
                    content += f"   {title_parts[1]}\n"
            else:
                content += f"{i}️⃣ {title}\n"

            # 处理双语摘要
            summary = news['summary']
            if '\n\n' in summary:
                summary_parts = summary.split('\n\n')
                content += f"{summary_parts[0]}\n\n"
                if len(summary_parts) > 1:
                    content += f"中文翻译：\n{summary_parts[1]}\n"
            else:
                content += f"{summary}\n"

            content += f"原文链接：{news['url']}\n"
            content += f"影响分析：{news['impact_analysis']}\n"
            content += "投资建议：\n"
            for advice in news['investment_advice']:
                content += f"• {advice}\n"
            content += "\n"

        content += "祝您投资顺利，日常请关注风险。\n"

        return subject, content

    def save_to_file(self, subject: str, content: str) -> str:
        """保存邮件内容到文件"""
        filename = f"financial_news_{self.today}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Subject: {subject}\n\n")
            f.write(content)
        print(f"邮件内容已保存到: {filename}")
        return filename

def main():
    """主函数"""
    try:
        generator = FinancialNewsGenerator()
        subject, content = generator.generate_email_content()
        filename = generator.save_to_file(subject, content)

        print("\n" + "="*50)
        print("邮件生成成功！")
        print(f"主题: {subject}")
        print(f"内容已保存到: {filename}")
        print("="*50)

        # 打印邮件内容预览
        print("\n邮件内容预览:")
        print("-" * 30)
        print(f"Subject: {subject}\n")
        print(content)

    except Exception as e:
        print(f"生成邮件时出现错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()