from base.models.account import Account
from base.models.role import Role


def network_get_role(self, data):
    """
    获取角色全部信息
    必要参数：character_id
    """
    account_model = Account.objects.get(account=data['account'])
    role_model = Role.objects.get(account=account_model, name=data['main_role'])
    send_data = {
        'action': "receive_role",
        'account': role_model.account.account,
        'name': role_model.name,
        'level': role_model.level,
        'reborn': role_model.reborn,
        'race': role_model.character.race.name,
        'version': role_model.character.version_choices[role_model.character.version][1],
        'character': role_model.character.name,
        'map_id': role_model.map.version_choice[role_model.map.version][1] + role_model.map.map_id,
        'x': role_model.x,
        'y': role_model.y
    }
    print(send_data)
    self.transmit(send_data)
