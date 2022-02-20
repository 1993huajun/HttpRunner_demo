import configparser
import os


class CommonGlobal(object):

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cfp = os.path.dirname(os.path.abspath(__file__)) + "\\global.ini"

    def get_global(self, key):
        try:
            self.cf.read(self.cfp, encoding="gbk")
            value = self.cf.get("global", key)
        except:
            return False
        else:
            return value

    def set_global(self, key, value):
        self.cf.read(self.cfp, encoding="gbk")
        self.cf.set("global", key, str(value))
        with open(self.cfp, 'w') as configfile:
            self.cf.write(configfile)

    # 删除[global]下所有option和value
    def clear_global(self):
        self.cf.remove_section("global")
        self.cf.add_section("global")
        with open(self.cfp, 'w') as configfile:
            self.cf.write(configfile)


if __name__ == "__main__":
    CommonGlobal().clear_global()
