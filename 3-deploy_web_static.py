#!/usr/bin/python3
# Run task 1 and 2 with fab files
import os.path
from fabric.api import local
from datetime import datetime
import os.path
from fabric.api import local
from fabric.api import put
from fabric.api import env
from fabric.api import run
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


def do_deploy(archive_path):
    """deploy"""
    if not os.path.isfile(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]

    if put(archive_path, "tmp/{}".format(file_name)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}".format(file_name)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
           format(file_name, file_name)).failed:
        return False
    if run("rm /tmp/{}".format(file_name)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/"
           "releases/{}/".format(file_name, file_name)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file_name)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_name)).failed:
        return False
    return True


def deploy():
    """deploy for real"""
    if do_pack() is None:
        return Fasle
    return do_deploy(do_pack)