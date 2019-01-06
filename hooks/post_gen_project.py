#!/usr/bin/env python

import os


DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(*path):
    os.remove(os.path.join(DIRECTORY, *path))


def main():
    if '{{ cookiecutter.command_line_interface }}' == 'no':
        remove_file('src', '{{ cookiecutter.slug }}', 'cli.py')
        remove_file('tests', 'test_cli.py')


if __name__ == '__main__':
    main()
