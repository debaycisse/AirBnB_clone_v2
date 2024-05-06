#!/usr/bin/python3
"""This script uses the Fabric's module and its
functions to delete out-of-date archives"""
from fabric.api import env, sudo, cd, local
import os


env.hosts = ['34.229.55.139', '54.85.88.78']
env.user = 'ubuntu'


def count_archive_files(directory, begin_with, ext):
    """This function counts the number of archive files or any files
    whose name begins with the given name and ends with a given name.

    Args:
        directory - the path to the directory to be looked up.
        begin_with - file must begin with a prefix.
        ext - the extension of the file of interest.

    Returns:
        the total number of items that match up
    """
    count = 0
    for fn in os.listdir(directory):
        if fn.startswith(begin_with) and fn.endswith(ext):
            count += 1
    return count


def list_archives(directory, begin_with, ext):
    """computes and returns a list of archive files that match
    up with a given prefix and extension

    Args:
        directory - the path to the directory to be looked up.
        begin_with - file must begin with a prefix.
        ext - the extension of the file of interest.
    """
    list_of_archives = []
    for fn in os.listdir(directory):
        if fn.startswith(begin_with) and fn.endswith(ext):
            list_of_archives.append(fn)
    list_of_archives.sort()
    return list_of_archives


def do_clean(number=0):
    """This function deletes outdated archive files"""
    num = int(number)
    n_of_files = count_archive_files('versions/', 'web_static', '.tgz')
    l_of_files = list_archives('versions/', 'web_static', '.tgz')
    if num == 0 and n_of_files > num:
        while n_of_files > 1:
            local('rm -f ./versions/{}'.format(l_of_files[0]))
            l_of_files.remove(l_of_files[0])
            n_of_files -= 1
    elif num > 0 and n_of_files > num:
        while n_of_files > num:
            local('rm -f ./versions/{}'.format(l_of_files[0]))
            l_of_files.remove(l_of_files[0])
            n_of_files -= 1

    # Do the same for remote servers here
    with cd("/data/web_static"):
        n_of_files = count_archive_files('releases',
                                         'web_static', '.tgz')
        l_of_files = list_archives('releases',
                                   'web_static', '.tgz')
        if num == 0 and n_of_files > num:
            while n_of_files > 1:
                sudo('rm -f ./releases/{}'.format(l_of_files[0]))
                l_of_files.remove(l_of_files[0])
                n_of_files -= 1
        elif num > 0 and n_of_files > num:
            while n_of_files > num:
                sudo('rm -f ./releases/{}'.format(l_of_files[0]))
                l_of_files.remove(l_of_files[0])
                n_of_files -= 1
