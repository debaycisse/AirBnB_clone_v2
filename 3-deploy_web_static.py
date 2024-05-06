#!/usr/bin/python3
"""This module uses the Fabric module's functions to create a script
that packs or bundles application files together and uploads them to
a set of servers"""

from os import path
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """This function calls the two functions, one of which packs or
    bundles static web files together while the other uploads them
    to the servers"""

    path_returned = do_pack()
    if not path.exists(path_returned):
        return False
    result = do_deploy(path_returned)
    return result
