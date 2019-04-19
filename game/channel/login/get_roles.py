from base.models.role import Character
from base.models.account import Account
from base.models.role import Role
from resource.models.character import CharacterPhoto


def network_get_roles(self, data):
    """
    必要参数：account_id
    """
    account = data["account"]

    roles = Role.objects.filter(account__account=account)
    roles_list = []
    for role in roles:
        character_photo = CharacterPhoto.objects.get(character=role.character, level=4)
        role_data = {
            'account': role.account.account,
            'level': role.level,
            'reborn': role.reborn,
            'race': role.character.race.name,
            'version': role.character.version_choices[role.character.version][1],
            'character': role.character.name,
            'role_name': role.name,
            'gender': role.character.gender,
            'avatar': [character_photo.was.wdf.name, character_photo.was.hash]
        }
        roles_list.append(role_data)

    send_data = {
        'action': "receive_roles",
        'roles_list': roles_list,
        'account': account
    }
    print(send_data)
    self.transmit(send_data)
