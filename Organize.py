#!/usr/bin/env/python
# coding=utf-8
from __future__ import unicode_literals
from __future__ import print_function

from ModuleLocator import module_path


def txt_to_list(path_to_txt):
    l = []

    with open(path_to_txt, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            # If line is not empty
            if stripped_line:
                l.append(stripped_line)

    return l


def get_matches(list1, list2):
    return set(list1).intersection(list2)


def get_missing(list1, list2):
    """
    Return the items in list1 which are missing in list2
    :rtype: list
    :param list1: list 1
    :param list2: list 2
    :return: List of items in list1 which are missing in list2
    """
    return list(set(list1) - set(list2))


def list_to_file(list1, path_to_file):
    with open(path_to_file, 'w') as f:
        for item in list1:
            print(item, file=f)


def organize():
    # Get physical path to this module
    path_to_this = module_path()

    # Create path to cubes
    path_to_cube = '{mp}/cubes'.format(mp=path_to_this)

    # Define paths
    path_to_current_cube = '{p}/cube_current.txt'.format(p=path_to_cube)
    path_to_vintage_cube = '{p}/cube_vintage.txt'.format(p=path_to_cube)
    path_to_matches = '{p}/cube_matches.txt'.format(p=path_to_cube)
    path_to_fillers = '{p}/cube_fillers.txt'.format(p=path_to_cube)
    path_to_missing = '{p}/cube_missing.txt'.format(p=path_to_cube)

    # Get current status
    current_cube = txt_to_list(path_to_current_cube)
    vintage_cube = txt_to_list(path_to_vintage_cube)

    # Find differences
    matches = get_matches(current_cube, vintage_cube)
    fillers = get_missing(current_cube, vintage_cube)
    missing = get_missing(vintage_cube, current_cube)

    # Save differences
    list_to_file(matches, path_to_matches)
    list_to_file(fillers, path_to_fillers)
    list_to_file(missing, path_to_missing)


if __name__ == '__main__':
    organize()
