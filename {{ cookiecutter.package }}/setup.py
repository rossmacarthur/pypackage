import io
import os
import re

from setuptools import setup


def read(*path):
    """
    Cross-platform Python 2/3 file reading.
    """
    filename = os.path.join(os.path.dirname(__file__), *path)

    with io.open(filename, encoding='utf8') as f:
        return f.read()


def find_version():
    """
    Regex search __init__.py so that we do not have to import.
    """
    text = read('{{ cookiecutter.slug }}', '__init__.py')
    match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', text, re.M)

    if match:
        return match.group(1)

    raise RuntimeError('Unable to find version string.')


version = find_version()

url = 'https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.slug }}'

long_description = read('README.rst')

install_requirements = [
{%- if cookiecutter.command_line_interface == 'yes' %}
    'click>=6.6'
{%- endif %}
]

lint_requirements = [
    'flake8',
    'flake8-isort',
    'flake8-quotes',
    'mccabe',
    'pep8-naming'
]

test_requirements = [
    'pytest',
    'pytest-cov'
]

package_requirements = [
    'twine'
]

{%- if cookiecutter.command_line_interface == 'yes' %}

entry_points = {
    'console_scripts': [
        '{{ cookiecutter.package }}-cli={{ cookiecutter.slug }}.cli:cli'
    ]
}
{%- endif %}

setup(
    name='{{ cookiecutter.package }}',
    packages=['{{ cookiecutter.slug }}'],
    version=version,
    install_requires=install_requirements,
    extras_require={'linting': lint_requirements,
                    'testing': test_requirements,
                    'packaging': package_requirements},
    python_requires='>=3.4',
{%- if cookiecutter.command_line_interface == 'yes' %}
    entry_points=entry_points,
{%- endif %}

    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    license='MIT',
    keywords='{{ cookiecutter.slug }}',
    url=url,
    download_url='{url}/archive/{version}.tar.gz'.format(url=url, version=version),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
