from base.models.account import Account
from django.core.exceptions import ObjectDoesNotExist


def network_get_account(self, data):
    try:
        account = Account.objects.get(account=data["account"])
        send_data = {
            "action": "receive_account",
            "account": str(account.account),
            "characters_num": str(account.character_num)
        }
    except ObjectDoesNotExist:
        send_data = {
            "action": "receive_tip",
            "message": "账户未找到"
        }
    print(send_data)
    self.transmit(send_data)
