from proxyPool.free_proxies.tester import Tester
from proxyPool.free_proxies.db import RedisClient
from proxyPool.free_proxies.crawler import Crawler
from proxyPool.free_proxies.settings import *
import sys


class Getter:
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到代理池限制
        :return:
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                # 返回爬虫名
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)
