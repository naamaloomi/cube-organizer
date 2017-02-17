#!/usr/bin/env/python
# coding=utf-8
from __future__ import unicode_literals

import sys

from os import path


def _module_is_frozen():
    return hasattr(sys, 'frozen')


def module_path():
    encoding = sys.getfilesystemencoding() or 'utf-8'
    if _module_is_frozen():
        return path.dirname(unicode(sys.executable, encoding))
    return path.dirname(unicode(__file__, encoding))
