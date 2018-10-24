from PIL import Image, TgaImagePlugin
from io import BytesIO
from .WDF import WDF
import imageio
import numpy


class WAS:
    """
    WAS动画管理类，存储各个方向的帧图片和帧mask
    """
    def __init__(self, direction_num, frame_num, x, y, w, h):
        self.image_group = []
        self.direction_num = direction_num
        self.frame_num = frame_num
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class ResManager:
    """
    WDF资源管理类，单例，WDF缓存
    """
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.wdf_pool = {}

    def get_res(self, wdf_name, _hash):
        """
        获得WDF资源
        :param wdf_name: wdf 文件名
        :param _hash:  hash值
        :return:
        """
        if wdf_name not in self.wdf_pool:  # 该实例为单例模式，并且将所有已读取的wdf资源缓存
            self.wdf_pool[wdf_name] = WDF(wdf_name)
        _wdf = self.wdf_pool[wdf_name]  # wdf
        _instance = _wdf.get(_hash)  # was tga jpg 等
        res = None
        if _instance.type == "WAS":
            res = WAS(_instance.direction_num, _instance.direction_pic_num,
                      _instance.x, _instance.y, _instance.width, _instance.height)  # Res资源实例
            for i in range(_instance.direction_num):
                temp = []
                for j in range(_instance.direction_pic_num):
                    pic = _instance.pic[i * _instance.direction_pic_num + j]
                    im = Image.frombuffer("RGBA", (pic.width, pic.height), pic.data, "raw", "RGBA", 0, 1)
                    size = pic.width * pic.height
                    arr = numpy.array(im)
                    temp.append((size, arr))
                _max = 0
                cur = 0
                pos = 0
                for obj in temp:
                    if obj[0] > _max:
                        _max = obj[0]
                        cur = pos
                    pos += 1
                temp = temp[cur:] + temp[:cur]
                pic_list = [x[1] for x in temp]
                res.image_group.append(pic_list)

        elif _instance.type == "JPG":
            jpg_file = BytesIO(_instance.data)
            res = Image.open(jpg_file)
        elif _instance.type == "TGA":
            tga_file = BytesIO(_instance.data)
            res = Image.open(tga_file)
        elif _instance.type == "Chat":
            res = _instance.chats
        else:
            raise Exception("类型错误")
        return res

    def get_wdf_file_list(self, wdf_name):
        if wdf_name not in self.wdf_pool:  # 该实例为单例模式，并且将所有已读取的wdf资源缓存
            self.wdf_pool[wdf_name] = WDF(wdf_name)
        return self.wdf_pool[wdf_name].file_dict.keys()


res_manager = ResManager()


def save_gif(wdf, _hash, path):
    res = res_manager.get_res(wdf, _hash)
    wdf_name = wdf.replace(".", "_")
    if isinstance(res, WAS):
        file_name = wdf_name + "_" + _hash + ".gif"
        imageio.mimsave(path + file_name, res.image_group[0], duration=0.1)
        return file_name, res.direction_num, res.frame_num
    elif isinstance(res, TgaImagePlugin.TgaImageFile):
        file_name = wdf_name + "_" + _hash + ".bmp"
        res.save(path + file_name, "BMP")
        res.close()
        return file_name, 1, 1
