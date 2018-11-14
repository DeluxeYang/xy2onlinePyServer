import os
import types
import importlib
from game.network.channel import Channel

modules = [
    "login"
]


class PlayerChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)
        for package_name in modules:
            file_list = [x[:-3] for x in os.listdir(package_name) if x[:2] != "__"]  # 从包中获取.py文件名
            for module_name in file_list:
                module = importlib.import_module(package_name + "." + module_name)  # 导入.py文件
                func_name_list = [x for x in dir(module) if x[:2] != "__"]  # 获得.py中的方法名
                for func_name in func_name_list:
                    self.__setattr__("network_"+func_name, types.MethodType(getattr(module, func_name), self))


if __name__ == "__main__":
    pc = PlayerChannel()
