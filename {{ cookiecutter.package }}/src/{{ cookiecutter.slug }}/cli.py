"""
Console script for {{ cookiecutter.name }}.
"""

import click


@click.group(
    context_settings={'help_option_names': ['-h', '--help']}
)
@click.version_option(
    None,
    '-v', '--version',
    prog_name='{{ cookiecutter.package }}',
    message='%(prog)s %(version)s'
)
def cli():
    """
    {{ cookiecutter.description }}
    """
    pass
