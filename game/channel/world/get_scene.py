def get_scene(self, data):
    """
    获取场景信息
    必要参数：character_id，根据character所在的位置，查找场景信息
    """
    send_data = {
        'action': data["callback"],
        'map_id': "",
        'NPC' : [],
        'portal': []
    }
    self.transmit(send_data)