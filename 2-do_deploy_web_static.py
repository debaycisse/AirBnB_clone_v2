#!/usr/bin/python3
"""A Fabric script that distributes an archive to
web srver, using the Fabric modules"""

from fabric.api import env, put, cd, sudo
from os import path

env.hosts = ['34.229.55.139', '54.90.32.207']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """This function uses the Fabric module and its methods
    to distribute an archive to webservers"""

    try:
        if not path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        filename = archive_path.split('/')[-1]
        with cd("/data/web_static/releases"):
            new_folder = filename.split('.')[0]
            sudo("mkdir -p {}".format(new_folder))
            sudo("tar -xzf /tmp/{} --directory={}/".format(
                filename, new_folder))
            sudo("rm -f /tmp/{}".format(filename))
            sudo("rm -f /data/web_static/current")
            sudo("ln -s {} {}".format(
                new_folder, '/data/web_static/current'))
        return True
    except Exception as e:
        return False
