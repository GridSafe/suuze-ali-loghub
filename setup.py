#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (C) Alibaba Cloud Computing
# All rights reserved.

"""Setup script for log service SDK.

You need to install google protocol buffer, setuptools and python-requests.
https://code.google.com/p/protobuf/
https://pypi.python.org/pypi/setuptools
http://docs.python-requests.org/

"""

from setuptools import setup, find_packages

install_requires = [
    'requests>2.11.1',
    'protobuf==3.2.0',
]

version = '0.6.4'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3.5',
    'License :: Copyright (C) Alibaba Cloud Computing. All rights reserved.'
]

setup(
    name='LogService',
    version=version,
    description='log service Python client SDK',
    author='sls_dev',
    url='http://www.aliyun.com/product/sls',
    install_requires=install_requires,
    packages=find_packages(),
    classifiers=classifiers,
)
