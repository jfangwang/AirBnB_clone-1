#!/usr/bin/python3
# distribute archive file
import os.path
from fabric.api import put
from fabric.api import env
from fabric.api import run

env.hosts = ["34.75.56.162", "35.237.17.44"]


def do_deploy(archive_path):
    """do_deploy

    Args:
        archive_path (str): archive path

    Returns:
        Boolean: True or False
    """    
    if not os.path.isfile(archive_path):
        return False
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_name)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(file_name)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
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
