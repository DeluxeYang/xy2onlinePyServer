from PodSixNet.Connection import connection
from PodSixNet.Connection import ConnectionListener


class MyNetworkListener(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        self.players = {}

    def Network(self, data):
        pass

    def Network_connected(self, data):
        pass

    def Network_myaction(self, data):
        print("myaction:", data)


host, port = "localhost", 8002
gui = MyNetworkListener(host, int(port))
gui.Send({"action": "myaction"})
while 1:
    gui.Pump()
    connection.Pump()