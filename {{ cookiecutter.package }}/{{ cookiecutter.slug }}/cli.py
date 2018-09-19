"""
Console script for {{ cookiecutter.name }}.
"""

import click


CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}
VERSION_PROG_NAME = '{{ cookiecutter.package }}'
VERSION_MESSAGE = '%(prog)s %(version)s'


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(None, '-v', '--version', prog_name=VERSION_PROG_NAME, message=VERSION_MESSAGE)
def cli():
    """
    {{ cookiecutter.description }}
    """
    pass
