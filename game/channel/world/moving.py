from base.models.account import Account
from base.models.role import Role
from base.models.map import Map, get_version


def network_moving(self, data):
    """
    接收玩家移动信息
    必要参数：character_id
    """
    account_model = Account.objects.get(account=data['account'])
    role_model = Role.objects.get(account=account_model, name=data['role_name'])
    if role_model.map.map_id != data['map_id']:
        role_model.map = Map.objects.get(map_id=data['map_id'], version=get_version(data['map_version']))
    role_model.x = data['path_list'][-1][0]
    role_model.y = data['path_list'][-1][1]
    role_model.save()
    send_data = {
        'action': "receive_moving",
        'role_name': role_model.name,
        'map_id': role_model.map.map_id,
        'map_version': role_model.map.version_choice[role_model.map.version][1],
        'path_list': data['path_list'],
        'is_running': data['is_running']
    }
    print(send_data)
    self._server.broadcast(data=send_data, except_myself=data['account'])
