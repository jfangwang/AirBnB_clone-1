#/usr/bin/python3
# Fab File first try
from fabric.api import *
from datetime import datetime


def do_pack():
    """Creating a tgz file archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(date)
    if os.path.isdir("versions"):
        pass
    else:
        try:
            local("mkdir versions")
        except:
            return None
    try:
        local("tar -cvzf {}.tgz".format(file_name))
    except:
        return None
    return file_name
        
