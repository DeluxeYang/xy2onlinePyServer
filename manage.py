#!/usr/bin/env python
import os
import sys
from threading import Thread

import django
django.setup()

from game.game_server import XY2GameServer
from xy2onlineServer.settings import Network_Port


def game_server_thread():
    game_server = XY2GameServer(local_address=("localhost", int(Network_Port)))
    game_server.launch()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xy2onlineServer.settings')
    try:
        from django.core.management import execute_from_command_line

        server = Thread(target=game_server_thread)
        server.daemon = True
        server.start()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



