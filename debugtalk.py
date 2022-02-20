# -- coding: utf-8 --
import requests
import os
from time import sleep
import random
import re
import time
import mock

from config.common_config import CommonConfig
from config.common_global import CommonGlobal


'''公共方法common'''
def hook_up():
    print("前置操作：setup！")

def hook_down():
    print("后置操作：tearDown！")


# 获取host
def get_host(host='host'):
    print(CommonConfig.get_cf("env", host))
    return CommonConfig.get_cf("env", host)


def get_cf(section, key):
    value = CommonConfig.get_cf(section, key)
    return value

def setup_hook_sleep():
    time.sleep(2)

def teardown_hook_sleep(response,t):
    if response.status_code == 200:
        time.sleep(2)
    else:
        time.sleep(t)


if __name__ == '__main__':
    print()
    get_host()