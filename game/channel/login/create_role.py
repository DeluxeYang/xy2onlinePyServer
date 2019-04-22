from base.models.account import Account as AccountModel
from base.models.role import Role as RoleModel
from base.models.map import Map
from resource.models.character import Character
from django.core.exceptions import ObjectDoesNotExist

from game.channel.account import Account
from game.channel.role import Role


def network_create_role(self, data):
    try:
        print(data)
        roles = RoleModel.objects.filter(name=data["role_name"])
        if len(roles) == 0:
            version = 0 if data["character_version"] == "old" else 1
            character = Character.objects.get(
                name=data["character_name"],
                version=version)
            new_role = RoleModel()
            new_role.account = self.account
            new_role.character = character
            new_role.name = data["role_name"]
            new_role.level = 0
            new_role.reborn = 0
            new_role.map = Map.objects.get(map_id='1001')
            new_role.x = 600
            new_role.y = 600
            new_role.save()
            self.roles[new_role.name] = new_role
            send_data = {
                "action": "receive_new_role",
                "account": str(self.account.account),
                "characters_num": str(self.account.role_num),
                "roles": []
            }
        else:
            send_data = {
                "action": "notify",
                "text": "角色名重复"
            }
    except ObjectDoesNotExist:
        send_data = {
            "action": "notify",
            "text": "请选择角色"
        }
    self.transmit(send_data)
