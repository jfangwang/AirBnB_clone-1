#!/usr/bin/python3
# Fab File first try
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Creating a tgz file archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    if os.path.isdir("versions"):
        pass
    else:
        try:
            local("mkdir versions")
        except:
            return None
    try:
        local("tar -cvzf {} web_static".format(file_name))
    except:
        return None
    return file_name
