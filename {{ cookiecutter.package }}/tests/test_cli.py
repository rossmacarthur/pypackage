from click.testing import CliRunner

from {{ cookiecutter.slug }} import __version__, cli


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert result.output == '{{ cookiecutter.package }} {version}'.format(version=__version__)
