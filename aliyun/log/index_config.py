#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) Alibaba Cloud Computing
# All rights reserved.

import time
from aliyun.log.util import Util


class IndexKeyConfig:
    """ The index config of a special log key
    :type token_list: string list
    :param token_list: the token config list, e.g ["," , "\t" ,
                       "\n" , " " , ";"]
    :type case_sensitive: bool
    :param case_sensitive: True if the value in the log keys is case
                           sensitive, False otherwise
    """
    def __init__(self, token_list=[], case_sensitive=False):
        self.token_list = token_list
        self.case_sensitive = case_sensitive

    def to_json(self):
        json_value = {}
        json_value["token"] = self.token_list
        json_value["caseSensitive"] = bool(self.case_sensitive)
        return json_value

    def from_json(self, json_value):
        self.token_list = json_value["token"]
        self.case_sensitive = bool(json_value["caseSensitive"])


class IndexLineConfig:
    """ The index config of the log line
    :type token_list: string list
    :param token_list: the token config list,
                       e.g ["," , "\t" , "\n" , " " , ";"]

    :type case_sensitive: bool
    :param case_sensitive: True if the value in the log keys is case sensitive,
                           False otherwise

    :type include_keys: string list
    :param include_keys: only the keys in include_keys should to be indexed,
                         only one of include_keys and exclude_keys could exist
                         at the same time, if both include_keys and
                         exclude_keys are empty, then the full line
                         will be indexed

    :type exclude_keys: string list
    :param exclude_keys: the keys in the exclude_keys list will not be indexed,
                         others keys will be indexed
    """
    def __init__(self, token_list=[], case_sensitive=False, include_keys=None,
                 exclude_keys=None):
        self.token_list = token_list
        self.case_sensitive = case_sensitive
        self.include_keys = include_keys
        self.exclude_keys = exclude_keys

    def to_json(self):
        json_value = {}
        json_value["token"] = self.token_list
        json_value["caseSensitive"] = bool(self.case_sensitive)

        if self.include_keys:
            json_value["include_keys"] = self.include_keys
        if self.exclude_keys:
            json_value["exclude_keys"] = self.exclude_keys
        return json_value

    def from_json(self, json_value):
        self.token_list = json_value["token"]
        self.case_sensitive = bool(json_value["caseSensitive"])
        self.include_keys = Util.get_json_value(json_value, "include_keys",
                                                None)
        self.exclude_keys = Util.get_json_value(json_value, "exclude_keys",
                                                None)


class IndexConfig:
    """The index config of a logstore
    :type ttl : int
    :param ttl : the indexed data life cycle in days, only support 7, 30, 90

    :type line_config : IndexLineConfig
    :param line_config : the index config of the whole log line

    :type key_config_list : dict (string => IndexKeyConfig)
    :param key_config_list: the index key configs of the keys

    :type all_keys_config : IndexKeyConfig
    :param all_keys_config : the key config of all keys, the new create
                             logstore should never user this param, it
                             only used to compatible with old config
    """
    def __init__(self, ttl=1, line_config=None, key_config_list={},
                 all_keys_config=None):
        self.ttl = ttl
        self.all_keys_config = all_keys_config
        self.line_config = line_config
        self.key_config_list = key_config_list
        self.modify_time = int(time.time())

    def to_json(self):
        json_value = {}
        json_value["ttl"] = self.ttl
        if self.line_config:
            json_value["line"] = self.line_config.to_json()
        if len(self.key_config_list) != 0:
            json_value["keys"] = {}
            for key, value in self.key_config_list.items():
                json_value["keys"][key] = value.to_json()

        if self.all_keys_config:
            json_value["all_keys"] = self.all_keys_config.to_json()
        return json_value

    def from_json(self, json_value):
        self.ttl = json_value["ttl"]
        if "all_keys" in json_value:
            self.all_keys_config = IndexKeyConfig()
            self.all_keys_config.from_json(json_value["all_keys"])
        if "line" in json_value:
            self.line_config = IndexLineConfig()
            self.line_config.from_json(json_value["line"])
        if "keys" in json_value:
            self.key_config_list = {}
            key_configs = json_value["keys"]
            for key, value in key_configs.items():
                key_config = IndexKeyConfig()
                key_config.from_json(value)
                self.key_config_list[key] = key_config

        self.modify_time = Util.get_json_value(
            json_value, "lastModifyTime", int(time.time()))
