from base.models.announcement import Announcement


def network_get_announcement(self, data):
    announcement = Announcement.objects.get()
    send_data = {
        'action': "receive_announcement",
        'text': str(announcement.content)
    }
    self.transmit(send_data)
