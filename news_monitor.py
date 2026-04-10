#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻源监控和错误处理系统
"""

import os
import sys
import json
import requests
import feedparser
from datetime import datetime, timedelta
import time
import logging
from typing import List, Dict, Optional

class NewsMonitor:
    def __init__(self):
        self.setup_logging()
        self.monitoring_data_file = 'news_monitoring.json'
        self.load_monitoring_data()

    def setup_logging(self):
        """设置日志"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('news_monitor.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_monitoring_data(self):
        """加载监控数据"""
        if os.path.exists(self.monitoring_data_file):
            try:
                with open(self.monitoring_data_file, 'r', encoding='utf-8') as f:
                    self.monitoring_data = json.load(f)
            except Exception as e:
                self.logger.error(f"加载监控数据失败: {e}")
                self.monitoring_data = {'sources': {}, 'daily_stats': {}}
        else:
            self.monitoring_data = {'sources': {}, 'daily_stats': {}}

    def save_monitoring_data(self):
        """保存监控数据"""
        try:
            with open(self.monitoring_data_file, 'w', encoding='utf-8') as f:
                json.dump(self.monitoring_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.logger.error(f"保存监控数据失败: {e}")

    def test_rss_source(self, source_name: str, rss_url: str) -> Dict:
        """测试RSS源可用性"""
        start_time = time.time()
        result = {
            'name': source_name,
            'url': rss_url,
            'status': 'failed',
            'response_time': 0,
            'item_count': 0,
            'last_error': '',
            'last_checked': datetime.now().isoformat()
        }

        try:
            # 测试RSS源
            feed = feedparser.parse(rss_url)
            result['response_time'] = time.time() - start_time

            if feed.bozo == 0:  # RSS解析成功
                result['status'] = 'success'
                result['item_count'] = len(feed.entries)
                self.logger.info(f"RSS源 {source_name} 测试成功，获取到 {len(feed.entries)} 条新闻")
            else:
                result['last_error'] = f"RSS解析错误: {feed.bozo_exception}"
                self.logger.warning(f"RSS源 {source_name} 解析错误: {feed.bozo_exception}")

        except Exception as e:
            result['last_error'] = str(e)
            result['response_time'] = time.time() - start_time
            self.logger.error(f"RSS源 {source_name} 测试失败: {e}")

        # 更新监控数据
        self.monitoring_data['sources'][source_name] = result
        return result

    def test_api_source(self, source_name: str, api_url: str, params: Dict = None) -> Dict:
        """测试API源可用性"""
        start_time = time.time()
        result = {
            'name': source_name,
            'url': api_url,
            'status': 'failed',
            'response_time': 0,
            'item_count': 0,
            'last_error': '',
            'last_checked': datetime.now().isoformat()
        }

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(api_url, params=params, headers=headers, timeout=10)
            result['response_time'] = time.time() - start_time

            if response.status_code == 200:
                # 尝试解析JSON
                try:
                    data = response.json()
                    result['status'] = 'success'
                    # 估算数据项数量
                    articles = data.get('articles', data.get('data', data.get('items', [])))
                    result['item_count'] = len(articles) if isinstance(articles, list) else 0
                    self.logger.info(f"API源 {source_name} 测试成功，获取到 {result['item_count']} 条数据")
                except json.JSONDecodeError:
                    result['last_error'] = 'JSON解析失败'
                    self.logger.warning(f"API源 {source_name} JSON解析失败")
            else:
                result['last_error'] = f"HTTP {response.status_code}: {response.reason}"
                self.logger.warning(f"API源 {source_name} HTTP错误: {response.status_code}")

        except Exception as e:
            result['last_error'] = str(e)
            result['response_time'] = time.time() - start_time
            self.logger.error(f"API源 {source_name} 测试失败: {e}")

        # 更新监控数据
        self.monitoring_data['sources'][source_name] = result
        return result

    def check_all_sources(self):
        """检查所有新闻源"""
        self.logger.info("开始检查所有新闻源...")

        # 定义要测试的新闻源
        sources_to_test = [
            # RSS源
            {'name': '华尔街见闻A股', 'type': 'rss', 'url': 'https://wallstreetcn.com/rss/news?category=a_stock&limit=20'},
            {'name': '华尔街见闻美股', 'type': 'rss', 'url': 'https://wallstreetcn.com/rss/news?category=us_stock&limit=20'},
            {'name': '华尔街见闻Crypto', 'type': 'rss', 'url': 'https://wallstreetcn.com/rss/news?category=crypto&limit=20'},
            {'name': '第一财经RSS', 'type': 'rss', 'url': 'https://www.yicai.com/rss/yicaiweb.xml'},
            {'name': 'CoinDesk', 'type': 'rss', 'url': 'https://www.coindesk.com/feed'},
            {'name': 'Bloomberg Asia', 'type': 'rss', 'url': 'https://www.bloomberg.com/feeds/bview/asia.xml'},
        ]

        results = []
        for source in sources_to_test:
            if source['type'] == 'rss':
                result = self.test_rss_source(source['name'], source['url'])
            elif source['type'] == 'api':
                result = self.test_api_source(source['name'], source['url'], source.get('params'))
            results.append(result)

        # 生成统计报告
        total_sources = len(results)
        working_sources = len([r for r in results if r['status'] == 'success'])
        avg_response_time = sum(r['response_time'] for r in results) / total_sources if total_sources > 0 else 0

        today = datetime.now().strftime('%Y-%m-%d')
        self.monitoring_data['daily_stats'][today] = {
            'total_sources': total_sources,
            'working_sources': working_sources,
            'success_rate': working_sources / total_sources if total_sources > 0 else 0,
            'avg_response_time': avg_response_time,
            'timestamp': datetime.now().isoformat()
        }

        self.save_monitoring_data()

        # 生成报告
        report = f"""
新闻源监控报告 - {today}
{'='*50}
总源数量: {total_sources}
可用源数量: {working_sources}
成功率: {(working_sources/total_sources*100):.1f}%
平均响应时间: {avg_response_time:.2f}秒

源状态详情:
"""

        for result in results:
            status_icon = "✅" if result['status'] == 'success' else "❌"
            report += f"{status_icon} {result['name']}: {result['status']} ({result['response_time']:.2f}s, {result['item_count']} items)\n"
            if result['last_error']:
                report += f"   错误: {result['last_error']}\n"

        self.logger.info(f"\n{report}")
        return report

    def get_source_status(self, source_name: str) -> Optional[Dict]:
        """获取特定源的状态"""
        return self.monitoring_data['sources'].get(source_name)

    def get_daily_stats(self, date: str = None) -> Optional[Dict]:
        """获取每日统计"""
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        return self.monitoring_data['daily_stats'].get(date)

    def generate_alert_if_needed(self):
        """根据监控数据生成警"""
        today = datetime.now().strftime('%Y-%m-%d')
        stats = self.get_daily_stats(today)

        if not stats:
            return

        # 如果成功率低于50%，生成警
        if stats['success_rate'] < 0.5:
            alert_msg = f"⚠️ 警报: 今日新闻源成功率过低 ({stats['success_rate']*100:.1f}%)"
            self.logger.warning(alert_msg)

        # 如果平均响应时间过长，生成警
        if stats['avg_response_time'] > 5.0:
            alert_msg = f"⚠️ 警报: 新闻源平均响应时间过长 ({stats['avg_response_time']:.2f}秒)"
            self.logger.warning(alert_msg)

def main():
    """主函数"""
    monitor = NewsMonitor()

    print("新闻源监控系统")
    print("="*50)

    # 检查所有源
    report = monitor.check_all_sources()

    # 生成警
    monitor.generate_alert_if_needed()

    # 保存报告到文件
    with open(f"news_monitor_report_{datetime.now().strftime('%Y%m%d')}.txt", 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n监控报告已保存到文件")
    print("详细日志请查看 news_monitor.log")

if __name__ == "__main__":
    main()