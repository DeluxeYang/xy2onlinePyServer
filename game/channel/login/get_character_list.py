def get_character_list(self, data):
    """
    必要参数：account_id
    """
    send_data = {
        'action': "receive_character_list",
        'character_list': [
            {"character_id": 0, "character_name": "",
             "character_reborn": 0, "character_level": 0,
             "character_res_index": "feijianxia"}
        ]
    }
    self.transmit(send_data)