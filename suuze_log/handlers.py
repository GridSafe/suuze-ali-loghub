#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from copy import deepcopy
from logging import Handler

from aliyun.log.logclient import LogClient
from aliyun.log.logitem import LogItem
from aliyun.log.putlogsrequest import PutLogsRequest


class AliLogHubHandler(Handler):

    _record_args = ['created', 'exc_info', 'exc_text', 'filename',
                    'funcName', 'levelname', 'levelno', 'lineno',
                    'module', 'msecs', 'msg', 'name', 'pathname',
                    'process', 'processName', 'relativeCreated',
                    'stack_info', 'thread', 'threadName']

    def __init__(self, endpoint, access_key_id, access_key_secret,
                 log_project, log_store, log_topic='',
                 log_source='', require_args=None):
        """
        :param endpoint: aliyun log service host name
        :param access_key_id: aliyun access key id
        :param access_key_secret: aliyun access key secret
        :param log_project: aliyun log service project
        :param log_store: aliyun log service store
        :param log_topic: custom log topic for better log search
        :param log_source: host ip 
        :param require_args: require args that need to send to aliyun loghub,
                             should be a subset of _record_args or None
        """
        super(AliLogHubHandler, self).__init__()
        self.log_client = LogClient(endpoint, access_key_id,
                                    access_key_secret)
        self.log_project = log_project
        self.log_store = log_store
        self.log_topic = log_topic
        self.log_source = log_source

        if self._are_valid_record_args(require_args):
            self.require_args = require_args or self._record_args
        else:
            raise ValueError('Invalid require_args')

    def _are_valid_record_args(self, require_args):
        """
        Check whether user input require_args is subset of _record_args
        None means send all of _record_args

        :param require_args: user input require args
        :return: <True/False>
        """
        if not require_args:
            return True

        if not isinstance(require_args, (list, tuple)):
            return False

        for arg in require_args:
            if arg not in self._record_args:
                return False

        return True

    def emit(self, record):
        """
        Use aliyun log python sdk to send logs
        """
        item = LogItem()
        item.set_time(int(time.time()))

        msg = {}
        for arg in self.require_args:
            msg[arg] = str(record.__dict__[arg])
        item.set_contents(list(msg.items()))

        req = PutLogsRequest(self.log_project, self.log_store, self.log_topic,
                             self.log_source, [item])
        self.log_client.put_logs(req)
