"""
Setup file for {{ cookiecutter.name }}.
"""

import io
import os
import re
{% if cookiecutter.package_style == 'module' %}
from setuptools import setup
{%- elif cookiecutter.package_style == 'package' %}
from setuptools import find_packages, setup
{%- endif %}


def get_metadata():
    """
    Return metadata for {{ cookiecutter.name }}.
    """
    here = os.path.abspath(os.path.dirname(__file__))

  {%- if cookiecutter.package_directory == 'src' and cookiecutter.package_style == 'module' %}
    init_path = os.path.join(here, 'src', '{{ cookiecutter.slug }}.py')
  {%- elif cookiecutter.package_directory == 'src' and cookiecutter.package_style == 'package' %}
    init_path = os.path.join(here, 'src', '{{ cookiecutter.slug }}', '__init__.py')
  {%- elif cookiecutter.package_style == 'module' %}
    init_path = os.path.join(here, '{{ cookiecutter.slug }}.py')
  {%- elif cookiecutter.package_style == 'package' %}
    init_path = os.path.join(here, '{{ cookiecutter.slug }}', '__init__.py')
  {%- endif %}

  {%- if cookiecutter.readme_markup_language == 'reStructuredText' %}
    readme_path = os.path.join(here, 'README.rst')
  {%- elif cookiecutter.readme_markup_language == 'Markdown' %}
    readme_path = os.path.join(here, 'README.md')
  {%- endif %}

    with io.open(init_path, encoding='utf-8') as f:
        about_text = f.read()

    metadata = {
        key: re.search(r'__' + key + r"__ = '(.*?)'", about_text).group(1)
        for key in ('title', 'version', 'url', 'author', 'author_email', 'license', 'description')
    }
    metadata['name'] = metadata.pop('title')

    with io.open(readme_path, encoding='utf-8') as f:
        metadata['long_description'] = f.read()

      {%- if cookiecutter.readme_markup_language == 'Markdown' %}
        metadata['long_description_content_type'] = 'text/markdown'
      {%- endif %}

    return metadata


metadata = get_metadata()

# Primary requirements
install_requires = [
{%- if cookiecutter.command_line_interface == 'yes' %}
    'click >=7.0'
{%- endif %}
]
{%- if cookiecutter.command_line_interface == 'yes' %}
entry_points = {
    'console_scripts': [
      {%- if cookiecutter.package_style == 'module' %}
        '{{ cookiecutter.package }}-cli={{ cookiecutter.slug }}_cli:cli'
      {%- elif cookiecutter.package_style == 'package' %}
        '{{ cookiecutter.package }}-cli={{ cookiecutter.slug }}.cli:cli'
      {%- endif %}
    ]
}
{%- endif %}

# Development requirements
lint_requires = [
    'flake8 >=3.7.0',
    'flake8-comprehensions',
    'flake8-docstrings',
    'flake8-isort',
    'flake8-mutable',
    'flake8-pep3101',
    'flake8-quotes',
    'pep8-naming'
]
test_requires = [
    'pytest',
    'pytest-cov',
]

setup(
    # Options
    install_requires=install_requires,
    extras_require={
        'dev.lint': lint_requires,
        'dev.test': test_requires
    },
    python_requires='>=3.4',

  {%- if cookiecutter.package_directory == 'src' %}
    package_dir={'': 'src'},
  {%- endif -%}

  {%- if cookiecutter.package_style == 'module' %}
    {%- if cookiecutter.command_line_interface == 'yes' %}
    py_modules=['{{ cookiecutter.slug }}', '{{ cookiecutter.slug }}_cli'],
    {%- else %}
    py_modules=['{{ cookiecutter.slug }}'],
    {%- endif %}
  {%- elif cookiecutter.package_style == 'package' %}
    {%- if cookiecutter.package_directory == 'src' %}
    packages=find_packages('src'),
    {%- else %}
    packages=find_packages(exclude=['docs', 'tests']),
    {%- endif %}
  {%- endif %}

  {%- if cookiecutter.command_line_interface == 'yes' %}
    entry_points=entry_points,
  {%- endif %}

    # Metadata
    download_url='{url}/archive/{version}.tar.gz'.format(**metadata),
    project_urls={
        'Issue Tracker': '{url}/issues'.format(**metadata)
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    **metadata
)
