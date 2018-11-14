def get_around(self, data):
    """
    获取玩家周围其他玩家
    必要参数：character_id，根据character所在的位置，查找其他玩家
    """
    send_data = {
        'action': "receive_character",

    }
    self.transmit(send_data)