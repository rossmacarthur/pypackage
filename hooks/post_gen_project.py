#!/usr/bin/env python

import os


if __name__ == '__main__':
    if '{{ cookiecutter.command_line_interface }}' == 'no':
        directory = os.path.realpath(os.path.curdir)
        path = ('src', '{{ cookiecutter.slug }}', 'cli.py')
        os.remove(os.path.join(directory, *path))
