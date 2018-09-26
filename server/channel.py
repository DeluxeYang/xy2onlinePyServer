from PodSixNet.Channel import Channel
from base.models import Account


class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        pass

    def Network_myaction(self, data):
        account = Account.objects.get(name="Deluxe")
        # print("name", account.name, "num", account.character_num)
        self.Send({"action": "myaction", "name": account.name, "character_num": account.character_num})