from base.models.account import Account as AccountModel
from base.models.role import Role as RoleModel
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
        # account_model = AccountModel.objects.get(account=data["account"])
        # self.account = Account(account_model.account)
        # role_models = RoleModel.objects.filter(account=account_model)
        # self.account.role_num = len(role_models)
        # send_data = {
        #     "action": "receive_account",
        #     "account": str(account_model.account),
        #     "characters_num": str(account_model.role_num),
        #     "roles": []
        # }
        # for role in role_models:
        #     role_data = role.get_data()
        #     role_instance = Role(role_data)
        #     self.account.accept_role(role_instance)
        #     send_data["role"].append(role_data)
        # print(send_data)
    except ObjectDoesNotExist:
        send_data = {
            "action": "notify",
            "text": "请选择角色"
        }
    self.transmit(send_data)
