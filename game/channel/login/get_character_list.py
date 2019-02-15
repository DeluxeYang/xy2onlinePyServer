from base.models.role import Character
from base.models.account import Account


def get_character_list(self, data):
    """
    必要参数：account_id
    """
    account_id = data["account_id"]
    self.account = Account.objects.get(id=account_id)  # 初始化 账户
    characters = Character.objects.filter(account=self.account)
    character_list = []
    for c in characters:
        temp = {"character_id": c.id, "character_name": c.name}
        self.characters[c.id] = c  # 初始化 该账户下的所有角色
        character_list.append(temp)
    send_data = {
        'action': "receive_character_list",
        'character_list': character_list
    }
    self.transmit(send_data)