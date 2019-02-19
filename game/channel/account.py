class Account:
    def __init__(self, account):
        self.account = account
        self.role_num = 0
        self.roles = []

    def accept_role(self, role):
        self.roles.append(role)
        self.__setattr__(role.id, role)
