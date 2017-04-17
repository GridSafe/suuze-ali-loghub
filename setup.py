#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (C) Alibaba Cloud Computing
# All rights reserved.

"""Setup script for log service SDK.

"""

from setuptools import setup, find_packages

install_requires = [
    'requests>2.11.1',
    'protobuf==3.2.0',
]

alisdk_version = '0.6.4'

version = '0.0.1'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3.5',
]

setup(
    name='suuze-ali-loghub',
    version=version,
    description='Log service Python client SDK integrating aliyun log service',
    author='suuze and sls_dev',
    url='https://github.com/GridSafe/suuze-ali-loghub',
    install_requires=install_requires,
    packages=find_packages(),
    classifiers=classifiers,
)
