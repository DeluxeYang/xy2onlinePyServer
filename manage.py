#!/usr/bin/env python
import os
import sys
from threading import Thread

import django
django.setup()

from server.server import MyServer


def server_thread():

    myserver = MyServer(localaddr=("localhost", int(8002)))
    print("server_start")
    myserver.Launch()


if __name__ == '__main__':
    server = Thread(target=server_thread)
    server.daemon = True
    server.start()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xy2onlineServer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



