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
        super(AliLogHubHandler, self).__init__()
        self.log_client = LogClient(endpoint, access_key_id,
                                    access_key_secret)
        self.log_project = log_project
        self.log_store = log_store
        self.log_topic = log_topic
        self.log_source = log_source
        if self._are_valid_record_args(require_args):
            self.require_args = require_args
        else:
            raise ValueError('Invalid require_args')

    def _are_valid_record_args(self, require_args):
        if not require_args:
            # Not providing require_args is valid action
            return True

        if not isinstance(require_args, (list, tuple)):
            return False

        for arg in require_args:
            if arg not in self._record_args:
                return False

        return True

    def _to_string_list(self, dict_obj):
        ret = {}
        for key, value in dict_obj.items():
            ret[key] = str(value)
        return list(ret.items())

    def emit(self, record):
        """
        Use aliyun log python sdk to send logs
        """
        item = LogItem()
        item.set_time(int(time.time()))
        if not self.require_args:
            record_msg = deepcopy(record.__dict__)
            record_msg.pop('args')
            item.set_contents(self._to_string_list(record_msg))
        else:
            msg = {}
            for arg in self.require_args:
                msg[arg] = record.__dict__[arg]
            item.set_contents(self._to_string_list(msg))

        req = PutLogsRequest(self.log_project, self.log_store, self.log_topic,
                             self.log_source, [item])
        self.log_client.put_logs(req)
