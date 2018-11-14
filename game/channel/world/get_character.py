def get_character(self, data):
    """
    获取角色全部信息
    必要参数：character_id
    """
    send_data = {
        'action': "receive_character",
        'character_name': "",
        'character_position' : (0, 0)
    }
    self.transmit(send_data)