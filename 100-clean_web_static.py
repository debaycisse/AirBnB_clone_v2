#!/usr/bin/python3
"""This script uses the Fabric's module and its
functions to delete out-of-date archives"""
from datetime import datetime
from fabric.api import env, sudo, cd, local


def do_clean(number=0):
    """This function deletes outdated archive files"""
    files_and_date = {}
    now = datetime.now()
    
