def get_account_list(self, data):
    send_data = {
        'action': "receive_account_list",
        'account_list': [
            {"account_id": 0, "account_name": ""}
        ]
    }
    self.transmit(send_data)