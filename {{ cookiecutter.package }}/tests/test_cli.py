from click.testing import CliRunner

from {{ cookiecutter.slug }} import __version__
from {{ cookiecutter.slug }}.cli import cli


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert result.output == '{{ cookiecutter.package }} {version}\n'.format(version=__version__)
