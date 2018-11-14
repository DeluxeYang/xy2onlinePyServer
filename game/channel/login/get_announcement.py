def get_announcement(self, data):
    send_data = {
        'action': "receive_announcement",
        'text': "我是一个公告"
    }
    self.transmit(send_data)