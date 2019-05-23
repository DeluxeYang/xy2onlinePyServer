from base.models.account import Account
from base.models.role import Role


# def network_get_role(self, data):
#     """
#     获取角色全部信息
#     必要参数：character_id
#     """
#     role_model = Role.objects.get(account__account=data['account'], name=data['role'])
#     send_data = {
#         'action': "receive_main_role" if data['is_main_role'] else "receive_role",
#         'account': role_model.account.account,
#         'role_name': role_model.name,
#         'map_version': role_model.map.version_choice[role_model.map.version][1],
#         'map_id': role_model.map.map_id,
#         'x': role_model.x,
#         'y': role_model.y
#     }
#     print(send_data)
#     self.transmit(send_data)


def network_get_roles(self, data):
    role_models = Role.objects.filter(account__account=data['account'])
    send_data = {
        'action': "receive_roles",
        'account': data['account'],
        'roles': []
    }
    for rm in role_models:
        send_data['roles'].append({
            'role_id': rm.id,
            'role_name': rm.name,
            'map_version': rm.map.version_choice[rm.map.version][1],
            'map_id': rm.map.map_id,
            'x': rm.x,
            'y': rm.y
        })
    print(send_data)
    self.transmit(send_data)
