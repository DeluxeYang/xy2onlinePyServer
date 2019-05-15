from base.models.account import Account
from base.models.role import Role
from base.models.map import Map, get_version


def network_get_other_players(self, data):
    """
    获取角色全部信息
    必要参数：character_id
    """
    _map = Map.objects.get(map_id=data['map_id'], version=get_version(data['map_version']))
    role_models = Role.objects.exclude(account__account=data['account']).filter(map=_map)
    send_data = {
        'action': "receive_other_players",
        'map_version': data['map_version'],
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
            'map_version': data['map_version'],
            'x': role.x,
            'y': role.y
        } for role in role_models]
    }
    print(send_data)
    self.transmit(send_data)
