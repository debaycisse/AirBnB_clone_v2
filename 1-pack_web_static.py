#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of the AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    This function generates a .tgz archive from the contents
    of the web_static folder

    Returns:
        Path to the archive if generated successfully, None otherwise
    """
    try:
        # Create a folder named versions if it doesn't
        # exist using Fabric's own function
        local("mkdir -p versions")

        # Get the current date and time
        now = datetime.now()

        # Format the current date and time as required
        date_time = now.strftime("%Y%m%d%H%M%S")

        # Formats the name of the archive file to reflect
        archive_name = "web_static_" + date_time + ".tgz"

        # Compress the contents of the web_static folder into the archive
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the path to the generated archive
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
