#!/usr/bin/env python

import os
import shutil

from os.path import join


DIRECTORY = os.path.realpath(os.path.curdir)


def package_dir(*path):
    return os.path.join(DIRECTORY, *path)


def remove_file_or_directory(path):
    path = package_dir(path)

    try:
        os.remove(path)
    except OSError:
        shutil.rmtree(path)


def is_eq(setting, value):
    return setting == value


def remove_if_no(path, setting):
    if is_eq(setting, 'no'):
        remove_file_or_directory(path)


def remove_if_ne(path, setting, value):
    if not is_eq(setting, value):
        remove_file_or_directory(path)


def copy(filename, *path):
    source = package_dir(join('_source', filename))
    destination = package_dir(join(*path))
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copy(source, destination)


def main():
    # Remove these files if the setting is equal to the given value.
    remove_if_ne('README.rst', '{{ cookiecutter.readme_markup_language }}', 'reStructuredText')
    remove_if_ne('README.md', '{{ cookiecutter.readme_markup_language }}', 'Markdown')

    # Remove these files if the setting is equal to 'no'.
    remove_if_no('LICENSE', '{{ cookiecutter.license_file }}')
    remove_if_no('docs', '{{ cookiecutter.sphinx_documentation }}')
    remove_if_no('Makefile', '{{ cookiecutter.makefile }}')
    remove_if_no('CONTRIBUTING.rst', '{{ cookiecutter.contributing_file }}')
    remove_if_no('RELEASES.rst', '{{ cookiecutter.releases_file }}')

    # Convert these settings to Python booleans, it makes life easier.
    src = is_eq('{{ cookiecutter.package_directory }}', 'src')
    package = is_eq('{{ cookiecutter.package_style }}', 'package')
    module = is_eq('{{ cookiecutter.package_style }}', 'module')
    cli = is_eq('{{ cookiecutter.command_line_interface }}', 'yes')

    # src/package.py
    if src and module:
        copy('__init__.py', 'src', '{{ cookiecutter.slug }}.py')
        copy('test_core.py', 'tests', 'test_{{ cookiecutter.slug }}.py')

        if cli:
            copy('cli.py', 'src', '{{ cookiecutter.slug }}_cli.py')
            copy('test_cli.py', 'tests', 'test_{{ cookiecutter.slug }}_cli.py')

    # src/package/__init__.py
    elif src and package:
        copy('__init__.py', 'src', '{{ cookiecutter.slug }}', '__init__.py')
        copy('core.py', 'src', '{{ cookiecutter.slug }}', 'core.py')
        copy('test_core.py', 'tests', 'test_core.py')

        if cli:
            copy('cli.py', 'src', '{{ cookiecutter.slug }}', 'cli.py')
            copy('test_cli.py', 'tests', 'test_cli.py')

    # package.py
    elif module:
        copy('__init__.py', '{{ cookiecutter.slug }}.py')

        if cli:
            copy('cli.py', '{{ cookiecutter.slug }}_cli.py')
            copy('test_cli.py', 'test_{{ cookiecutter.slug }}_cli.py')

    # package/__init__.py
    elif package:
        copy('__init__.py', '{{ cookiecutter.slug }}', '__init__.py')
        copy('core.py', '{{ cookiecutter.slug }}', 'core.py')
        copy('test_core.py', 'tests', 'test_core.py')

        if cli:
            copy('cli.py', '{{ cookiecutter.slug }}', 'cli.py')
            copy('test_cli.py', 'tests', 'test_cli.py')

    remove_file_or_directory('_source')


if __name__ == '__main__':
    main()
