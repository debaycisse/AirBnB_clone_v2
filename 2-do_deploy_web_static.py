#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import env, put, run
import os

env.hosts = ['34.229.55.139', '54.90.32.207']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers

    Args:
        archive_path (str): Path to the archive to be deployed

    Returns:
        bool: True if all operations are successful, False otherwise
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Get the filename without extension
        file_name = archive_path.split("/")[-1].split(".")[0]

        # Uncompress the archive to /data/web_static/releases/<filename> on the web server
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(file_name))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file_name))
        return True
    except Exception as e:
        return False
