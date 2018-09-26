from time import sleep
from PodSixNet.Server import Server
from server.channel import ClientChannel


class MyServer(Server):
    channelClass  = ClientChannel

    def __init__(self, *args, **kwargs):
        self.id = 0
        Server.__init__(self, *args, **kwargs)
        print('Server launched')

    def Connected(self, channel, addr):
        print('new connection:', channel)

    def Launch(self):
        while True:
            self.Pump()
            sleep(0.0001)
