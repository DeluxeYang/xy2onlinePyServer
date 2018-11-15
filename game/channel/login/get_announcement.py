from base.models.announcement import Announcement

def get_announcement(self, data):
    announcement = Announcement.objects.get()
    send_data = {
        'action': "receive_announcement",
        'title': announcement.title,
        'content': announcement.content,
        'date': announcement.date
    }
    self.transmit(send_data)