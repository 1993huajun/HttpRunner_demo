# -- coding: utf-8 --
import requests
import os
# import time
# from MysqlUtil import MyMySQL
# import Sql
from time import sleep
import random
import re
import time
import mock


app_token1 = ""

'''公共方法common'''
def hook_up():
    print("前置操作：setup！")

def hook_down():
    print("后置操作：tearDown！")


# 从环境变量中取base_url
def getBase_url():
    try:
        base_url = ENV("host")
        return base_url
    except BaseException as msg:
        print(msg)

# 取环境变量
def ENV(keyName):   #keyName对应的是.env里面的变量名称
    value = os.environ.get(keyName,"")
    print("getENV value is :%r"%value)
    # print("ENV app_token is:%r" % app_token1)#证明调用后，app_token1会失效
    return value

#设置用例间的时间延迟，避免调用过快
def setup_hook_sleep():
    time.sleep(2)

def teardown_hook_sleep(response,t):
    if response.status_code == 200:
        time.sleep(2)
    else:
        time.sleep(t)   # 根据t值，延迟设定的时间


# 跳过测试执行,那些异常情况的验证由测试跳过处理
def skip_test_in_production_env():
    """ skip this test in production environment
    """
    # 这里对应.env文件变量名TEST_ENV和变量值PRODUCTION，相等则跳过，不相等则执行
    return os.environ["TEST_ENV"] == "PRODUCTION"

# 取库数据时，要注意数据的返回类型
# 先执行特定的方法，再去数据库取数
# def getDataFromDB(tarSqlName,pre_method,parame):
#     try:
#         print(pre_method)
#
#         db = MyMySQL(
#             host="*****",
#             port=3306,
#             dbName="***",
#             username="root",
#             password="123456",
#             charset="utf8"
#         )
#
#         sql = Sql.sql
#         for i in sql:
#             print(sql.keys())
#             print(sql[i])
#             sleep(2)
#             if tarSqlName in sql.keys():  # 变量名和sql名称对应
#                 realSql = sql[i] + parame
#                 # 从testdata表中获取需要的测试数据
#                 testData = db.getDataFromDataBases(realSql)
#                 print("testData is :%r"%testData[0])
#                 testData = testData[0]
#                 print(type(testData))
#                 print(type(testData[0]))
#                 print("testData[0] is:%d"%testData[0])
#                 db.closeDatabase()
#                 return testData[0]
#             else:
#                 return 2010008000
#     except BaseException as msg:
#         print(msg)
#         return 2010008000

#获取随机手机号
def get_phone():
    return "13556"+str(random.randint(100000,999999))


# 条件为1，参数为空
def checkIfCondition(tar,condition):
    if condition:
        return None
    else:
        return tar


'''业务处理函数'''
#文件路径
def get_file(filePath):
    return open(filePath, "rb")

# 从返回的照片url中提取照片名称
def get_frontImg(tarStr):
    print(tarStr)
    tar = re.split("com",tarStr)
    return tar[1]


if __name__ == '__main__':
    print()