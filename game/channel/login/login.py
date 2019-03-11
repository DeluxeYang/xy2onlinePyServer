from base.models.account import Account as AccountModel
from base.models.role import Role as RoleModel
from django.core.exceptions import ObjectDoesNotExist

from game.channel.account import Account
from game.channel.role import Role


def network_login(self, data):
    try:
        self.account = AccountModel.objects.get(account=data["account"])
        role_models = RoleModel.objects.filter(account=self.account)
        send_data = {
            "action": "receive_account",
            "account": str(self.account.account),
            "characters_num": str(self.account.role_num),
            "roles": []
        }
        for role in role_models:
            role_data = role.get_data()
            self.roles[role.name] = role
            send_data["role"].append(role_data)
        print(send_data)
    except ObjectDoesNotExist:
        send_data = {
            "action": "notify",
            "text": "账户未找到"
        }
    self.transmit(send_data)
