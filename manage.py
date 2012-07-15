#!/usr/bin/env python
import os
from os.path import abspath, dirname, join
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justthereadme.settings")

    from django.core.management import execute_from_command_line

    sys.path.insert(0, abspath(join(dirname(__file__), "justthereadme")))

    execute_from_command_line(sys.argv)
