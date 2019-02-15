from base.models.role import Character


def get_character(self, data):
    """
    获取角色全部信息
    必要参数：character_id
    """
    character = self.characters[data["character_id"]]
    send_data = {
        'action': "receive_character",
        'character_name': character.name,
        'x' : character.x,
        'y' : character.y,
        'map_id': character.map_id
    }
    self.transmit(send_data)