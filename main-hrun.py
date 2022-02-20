import sys

from httprunner.cli import main
from config.common_config import CommonConfig

cmd = sys.argv.pop(1)
envHost = sys.argv.pop(2)

if envHost == "qa":
    pointedHost = CommonConfig.get_cf("env", "host_qa")
    CommonConfig.set_cf("env", "host", pointedHost)
elif envHost == "release":
    pointedHost = CommonConfig.get_cf("env", "host_release")
    CommonConfig.set_cf("env", "host", pointedHost)

main()

