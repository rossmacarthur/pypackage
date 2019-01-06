#!/usr/bin/env python

import os
import shutil


DIRECTORY = os.path.realpath(os.path.curdir)


def remove_directory(*path):
    shutil.rmtree(os.path.join(DIRECTORY, *path))


def remove_file(*path):
    os.remove(os.path.join(DIRECTORY, *path))


def main():
    pass
    {%- if cookiecutter.sphinx_documentation == 'no' %}
    remove_directory('docs')
    {%- endif %}
    {%- if cookiecutter.command_line_interface == 'no' %}
    remove_file('src', '{{ cookiecutter.slug }}', 'cli.py')
    remove_file('tests', 'test_cli.py')
    {%- endif %}


if __name__ == '__main__':
    main()

