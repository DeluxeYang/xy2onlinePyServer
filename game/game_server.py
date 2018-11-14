from __future__ import print_function

import sys
from time import sleep, localtime
from random import randint
from weakref import WeakKeyDictionary

from game.network.server import Server
from game.channel.player_channel import PlayerChannel


class XY2GameServer(Server):
    channel_class = PlayerChannel

    def __init__(self, *args, **kwargs):
        self.id = 0
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print('XY2 Server launched')

    def on_connected(self, player, address):
        print("New Player" + str(player.address))
        self.players[player] = True
        player.transmit({
            "action": "connected",
        })
