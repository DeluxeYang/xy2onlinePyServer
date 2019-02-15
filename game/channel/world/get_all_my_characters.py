from base.models.role import Character


def get_all_my_characters(self, data):
    """
    获取当前客户端账户的所有角色的全部信息
    """
    character_list = []
    for _id, c in self.characters.items():
        temp = {
            'character_id': c.id,
            'character_name': c.name,
            'x' : c.x,
            'y' : c.y,
            'map_id': c.map_id}
        character_list.append(temp)
    send_data = {
        'action': "receive_character",
        'character_list': character_list
    }
    self.transmit(send_data)