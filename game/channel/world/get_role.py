from base.models.account import Account
from base.models.role import Role


def network_get_role(self, data):
    """
    获取角色全部信息
    必要参数：character_id
    """
    account_model = Account.objects.get(account=data['account'])
    role_model = Role.objects.get(account=account_model, name=data['role'])
    send_data = {
        'action': "receive_main_role" if data['is_main_role'] else "receive_role",
        'account': role_model.account.account,
        'role_name': role_model.name,
        'role_level': role_model.level,
        'role_reborn': role_model.reborn,
        'race': role_model.character.race.name,
        'version': role_model.character.version_choices[role_model.character.version][1],
        'character': role_model.character.name,
        'map_id': role_model.map.version_choice[role_model.map.version][1] + role_model.map.map_id + '.map',
        'x': role_model.x,
        'y': role_model.y
    }
    print(send_data)
    self.transmit(send_data)
