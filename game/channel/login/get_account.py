from base.models.account import Account as AccountModel
from base.models.role import Role as RoleModel
from django.core.exceptions import ObjectDoesNotExist

from game.channel.account import Account
from game.channel.role import Role


def network_get_account(self, data):
    try:
        account = AccountModel.objects.get(account=data["account"])
        self.account = Account(account.account)
        roles = RoleModel.objects.filter(account=account)
        self.account.role_num = len(roles)
        for role in roles:
            role_instance = Role()
        send_data = {
            "action": "receive_account",
            "account": str(account.account),
            "characters_num": str(account.character_num)
        }
    except ObjectDoesNotExist:
        send_data = {
            "action": "notify",
            "text": "账户未找到"
        }
    self.transmit(send_data)
