#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging.config import dictConfig

from suuze_log.handlers import AliLogHubHandler


def test_logger():
    handler = AliLogHubHandler('cn-shanghai.log.aliyuncs.com',
                               '',
                               '',
                               'log-sdk-test', 'test',
                               log_topic='damn')

    require_args = ['levelname', 'msg', 'name', 'pathname',
                    'process', 'processName', 'stack_info',
                    'threadName', 'module', 'exc_info', 'exc_text']

    handler_2 = AliLogHubHandler('cn-shanghai.log.aliyuncs.com',
                                 '',
                                 '',
                                 'log-sdk-test',
                                 'test', 'damn',
                                 require_args=require_args)

    handler.setLevel('INFO')
    handler_2.setLevel('INFO')

    test_logger = logging.getLogger('test')
    test_logger.setLevel('INFO')

    test_logger.addHandler(handler)
    test_logger.addHandler(handler_2)

    test_logger.info('fuck')


def test_dict_config():
    require_args = ['levelname', 'msg', 'name', 'pathname',
                    'process', 'processName', 'stack_info',
                    'module', 'exc_info', 'exc_text']

    config = {
        'version': 1,
        'handlers': {
            'aliyun1': {
                'level': 'INFO',
                'class': 'suuze_log.handlers.AliLogHubHandler',
                'endpoint': 'cn-shanghai.log.aliyuncs.com',
                'access_key_id': '',
                'access_key_secret': '',
                'log_project': 'log-sdk-test',
                'log_store': 'test',
                'log_topic': 'test_topic',
            },
            'aliyun2': {
                'level': 'INFO',
                'class': 'suuze_log.handlers.AliLogHubHandler',
                'endpoint': 'cn-shanghai.log.aliyuncs.com',
                'access_key_id': '',
                'access_key_secret': '',
                'log_project': 'log-sdk-test',
                'log_store': 'test',
                'log_topic': 'test_topic',
                'require_args': require_args
            }
        },
        'loggers': {
            'dict_logger': {
                'level': 'INFO',
                'handlers': ['aliyun1', 'aliyun2']
            }
        }
    }
    dictConfig(config)

    logger = logging.getLogger('dict_logger')
    logger.info('fuck!!!!!!!!!')


if __name__ == '__main__':
    # test_logger()
    test_dict_config()
