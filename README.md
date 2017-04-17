# 整合阿里云的 loghub 服务到 python 的 logger 处理 

## Environment Version changed

1. protobuf: --> version: 3.2.0
2. python: --> version: 3.5

## Fix:

Coding style


# 使用示例：

    见 `sample_logger.py`，有直接调用和dictConfig配置两种示例

## 参数说明

* `suuze_log.handlers.AliLogHubHandler`
    * `endpoint`: 阿里云日志服务入口， 见:  
        `https://help.aliyun.com/document_detail/29008.html?spm=5176.doc29077.6.664.fwypef`
    * `access_key_id`: 阿里云帐号 access key id
    * `access_key_secret`: 阿里云帐号 密钥
    * `log_project`: 阿里云日志服务 项目名，需在阿里云管理平台上创建 
    * `log_store`: 阿里云日志服务 日志库名，需在阿里云管理平台上创建
    * `log_topic`: 可选参数，日志主题，同一库下可用不同主题区分以方便日志查询
    * `log_source`: 可选参数，日志来源，不填则由阿里云 sdk 自动生成
    * `require_args`: 可选参数，type: list/tuple, 日志中可携带参数，不填则表示发送所有可携带参数，可选参数如下：
        * `msg`: 日志内容
        * `name`: Logger 名 
        * `levelname`: logger level 名(DEBUG, INFO, WARNING, ERROR, CRITICAL)
        * `levelno`: logger level 的数字形式(0, 10, 20, 30, 40)
        * `pathname`: 调用 logger 的文件的详细路径 
        * `filename`: 调用 logger 的文件的文件名
        * `module`: 调用 logger 的模块名
        * `lineno`: 调用 logger 的行数
        * `funcName`: 调用 logger 的函数名
        * `created`: 日志的创建时间，time.time() 的值
        * `asctime`: 日志创建时间的文本形式
        * `msecs`: 创建时间的小数部份
        * `relativeCreated`: logging module 加载到日志创建时间的相对毫秒数
        * `thread`: 线程 id
        * `threadName`: 线程名
        * `process`: 进程 id
        * `exc_info`: 程序调用信息
        * `exc_text`: 程序调用信息的文本形式
        * `stack_info`: 和序调用栈信息

# 阿里云日志服务Python SDK

## 版本

0.6.0

## 发布时间

2015-11-16

## 基本介绍：

这是Log Service SDK for Python的开源版本。Log Service SDK for Python是阿里云日志服务
（Log Service）API的Python编程接口，提供了对于Log Service Rest API所有接口的封装
和支持，帮助Python开发人员更快编程使用阿里云Log Service服务。

### 具体功能：

1. 封装Rest API。
2. 实现API请求的数字签名
3. 实现API的Protocol Buffer格式发送日志
4. 支持API定义的数据压缩方式
5. 实现API查询数据和批量消费数据
6. 使用异常统一处理错误

## 环境要求：

1. Python 2.5及其以后版本

## 支持API版本：

1. Log Service API 0.6.0

## 其他资源：

1. 日志服务产品介绍：http://www.aliyun.com/product/sls/
2. 日志服务产品文档：http://docs.aliyun.com/#/sls
3. 其他问题请提工单
