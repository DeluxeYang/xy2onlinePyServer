from base.models.account import Account as AccountModel
from base.models.role import Role as RoleModel
from django.core.exceptions import ObjectDoesNotExist

from game.channel.account import Account
from game.channel.role import Role


def network_get_account(self, data):
    try:
        account_model = AccountModel.objects.get(account=data["account"])
        self.account = Account(account_model.account)
        role_models = RoleModel.objects.filter(account=account_model)
        self.account.role_num = len(role_models)
        send_data = {
            "action": "receive_account",
            "account": str(account_model.account),
            "characters_num": str(account_model.role_num),
            "roles": []
        }
        for role in role_models:
            role_data = role.get_data()
            role_instance = Role(role_data)
            self.account.accept_role(role_instance)
            send_data["role"].append(role_data)
        print(send_data)
    except ObjectDoesNotExist:
        send_data = {
            "action": "notify",
            "text": "账户未找到"
        }
    self.transmit(send_data)
