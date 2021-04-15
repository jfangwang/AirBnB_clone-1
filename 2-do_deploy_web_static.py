#!/usr/bin/python3
# distribute archive file
from fabric.api import local
from fabric.api import put
from fabric.api import env
from fabric.api import run
from datetime import datetime

env.hosts = [""]


def do_deploy(archive_path):
    """deploy"""
    if os.path.isfile(archive_path)
