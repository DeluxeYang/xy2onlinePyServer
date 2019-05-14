from base.models.account import Account
from base.models.role import Role
from base.models.map import Map


def network_jump(self, data):
    """
    接收玩家移动信息
    必要参数：character_id
    """
    role_model = Role.objects.get(account__account=data['account'], name=data['role_name'])
    if role_model.map.map_id != data['target_map_id']:
        role_model.map = Map.objects.get(map_id=data['target_map_id'])
    role_model.x = data['target_x']
    role_model.y = data['target_y']
    role_model.save()
    send_data = {
        'action': "refresh_scene"
    }
    print(send_data)
    self.transmit(send_data)
