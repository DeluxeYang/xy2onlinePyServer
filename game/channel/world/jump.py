from base.models.account import Account
from base.models.role import Role
from base.models.map import Map, get_version


def network_jump(self, data):
    """
    接收玩家移动信息
    必要参数：character_id
    """
    role_model = Role.objects.get(account__account=data['account'], name=data['role_name'])
    if role_model.map.map_id != data['target_map_id']:
        role_model.map = Map.objects.get(map_id=data['target_map_id'], version=get_version(data['target_map_version']))
    role_model.x = data['target_x']
    role_model.y = data['target_y']
    role_model.save()
    send_data = {
        'action': "refresh_scene"
    }
    print(send_data)
    self.transmit(send_data)
    send_data = {
        'action': "remove_role",
        'map_version': data["map_version"],
        'map_id': data["map_id"],
        'role_id': data["role_id"],
        'role_name': data["role_name"]
    }
    self._server.broadcast(send_data, data['account'])
    send_data = {
        'action': "add_role",
        'map_version': data["target_map_version"],
        'map_id': data["target_map_id"],
        'x': role_model.x,
        'y': role_model.y,
        'role_id': role_model.id,
        'role_name': role_model.name,
        'level': role_model.level,
        'reborn': role_model.reborn,
        'race': role_model.character.race.name,
        'version': role_model.character.version_choices[role_model.character.version][1],
        'character': role_model.character.name,
        'gender': role_model.character.gender
    }
    self._server.broadcast(send_data, data['account'])
