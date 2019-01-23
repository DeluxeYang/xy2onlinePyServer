from base.models.account import Account


def get_account_list(self, data):
    accounts = Account.objects.all()
    account_list = []
    for ac in accounts:
        temp = {"account_id": ac.id, "account_name": ac.name, "character_num": ac.character_num}
        account_list.append(temp)
    send_data = {
        'action': "receive_account_list",
        'account_list': account_list
    }
    self.transmit(send_data)
