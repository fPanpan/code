# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # ָ���Ǹ�����ȥ��request����ȥ��
SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # ֪��scheduler����
SCHEDULER_PERSIST = True     # �����е������Ƿ�־ñ��棬ΪFalse��ʱ���ڹر�redlis��ʱ�����redis
REDIS_URL = "redis://127.0.0.1:6379" # ָ��redis�ĵ�ַ
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,   # Scrapy_redisʵ�ֵ�items���浽redis��pipline
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

