from base.models.account import Account
from base.models.role import Role


def network_get_other_players(self, data):
    """
    获取角色全部信息
    必要参数：character_id
    """
    role_models = Role.objects.\
        exclude(account__account=data['account']).\
        filter(map__map_id=data['map_id'])
    send_data = {
        'action': "receive_other_players",
        'map_id': data['map_id'],
        'players': [{
            'role_name': role.name,
            'level': role.level,
            'reborn': role.reborn,
            'race': role.character.race.name,
            'version': role.character.version_choices[role.character.version][1],
            'character': role.character.name,
            'gender': role.character.gender,
            'map_id': role.map.map_id,
            'x': role.x,
            'y': role.y
        } for role in role_models]
    }
    print(send_data)
    self.transmit(send_data)
