# 使用
```Python3
python3 main-hrun.py hrun {testcase or path} {appointedHost}
# main-hrun.py为TestDeploy默认执行入口，见TestDeploy配置文件ini/config.ini
# 其他符合HttpRunner2.X规范
```

# 例子
## 执行release环境指定api
```Python3
python3 main-hrun.py hrun api/api_getUser.yml release
```

## 执行qa环境testcases文件夹下所有的用例
```Python3
python3 main-hrun.py hrun testcases/ qa
```
