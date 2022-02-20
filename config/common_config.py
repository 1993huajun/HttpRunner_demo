import configparser
import hashlib
import os

cf = configparser.ConfigParser()
cfp = os.path.dirname(os.path.abspath(__file__)) + "/conf.ini"
print(cfp)

class CommonConfig(object):

    @staticmethod
    def get_cf(section, key):
        cf.read(cfp, encoding="gbk")
        value = cf.get(section, key)
        if key == "passwd":
            m = hashlib.md5()
            m.update(bytes(value, encoding="utf8"))
            return m.hexdigest()
        else:
            return value

    @staticmethod
    def set_cf(section, key, value):
        cf.read(cfp, encoding="gbk")
        if not cf.has_section(section):
            cf.add_section(section)
        cf.set(section, key, value)
        with open(cfp, 'w') as configfile:
            cf.write(configfile)


if __name__ == "__main__":
    CommonConfig.set_cf("global", "1", "token")
    CommonConfig.set_cf("global", "2", "account_id")
