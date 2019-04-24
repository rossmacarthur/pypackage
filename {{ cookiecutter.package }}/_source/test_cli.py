from click.testing import CliRunner

from {{ cookiecutter.slug }} import __version__
{%- if cookiecutter.package_style == 'module' %}
from {{ cookiecutter.slug }}_cli import cli
{%- elif cookiecutter.package_style == 'package' %}
from {{ cookiecutter.slug }}.cli import cli
{%- endif %}


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert result.output == '{{ cookiecutter.package }} {version}\n'.format(version=__version__)
