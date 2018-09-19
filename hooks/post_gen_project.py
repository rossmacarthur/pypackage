#!/usr/bin/env python

import os


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(*path):
    os.remove(os.path.join(PROJECT_DIRECTORY, *path))


def main():
    if '{{ cookiecutter.command_line_interface }}' == 'no':
        remove_file('{{ cookiecutter.slug }}', 'cli.py')


if __name__ == '__main__':
    main()
