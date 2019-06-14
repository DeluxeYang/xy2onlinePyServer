from __future__ import print_function

import sys
from time import sleep, localtime
from random import randint
from weakref import WeakKeyDictionary

from game.network.server import Server
from game.channel.player_channel import PlayerChannel
from xy2onlineServer.settings import Network_Port


class XY2GameServer(Server):
    channel_class = PlayerChannel
    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        重写实现单例
        :return: 单例
        """
        if cls.__instance is None:
            cls.__instance = super(XY2GameServer, cls).__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        self.id = 0
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print('XY2 Server launched')

    def on_connected(self, channel, address):
        print("New Player" + str(channel.address))
        self.players[channel] = True
        channel.transmit({
            "action": "connected",
        })

    def broadcast(self, data, except_myself):
        for player in self.players:
            print(player)
            print(player.account)
            if player.account.account != except_myself:
                player.transmit(data)

    def launch(self):
        while True:
            self.pump()
            sleep(0.1)


game_server = XY2GameServer(local_address=("localhost", int(Network_Port)))
