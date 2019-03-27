#!/usr/bin/env python

import os
import shutil


DIRECTORY = os.path.realpath(os.path.curdir)


def remove_directory(*path):
    shutil.rmtree(os.path.join(DIRECTORY, *path))


def remove_file(*path):
    os.remove(os.path.join(DIRECTORY, *path))


def main():
  {% if cookiecutter.readme_markup_language != 'reStructuredText' %}
    remove_file('README.rst')
  {% endif %}
  {% if cookiecutter.readme_markup_language != 'Markdown' %}
    remove_file('README.md')
  {% endif %}
  {% if cookiecutter.license_file == 'no' %}
    remove_file('LICENSE')
  {% endif %}
  {% if cookiecutter.sphinx_documentation == 'no' %}
    remove_directory('docs')
  {% endif %}
  {% if cookiecutter.command_line_interface == 'no' %}
    remove_file('src', '{{ cookiecutter.slug }}', 'cli.py')
    remove_file('tests', 'test_cli.py')
  {% endif %}
  {% if cookiecutter.makefile == 'no' %}
    remove_file('Makefile')
  {% endif %}
  {% if cookiecutter.contributing_file == 'no' %}
    remove_file('CONTRIBUTING.rst')
  {% endif %}
  {% if cookiecutter.releases_file == 'no' %}
    remove_file('RELEASES.rst')
  {% endif %}


if __name__ == '__main__':
    main()
