import doctest
from datetime import datetime

import {{ cookiecutter.slug }}


# Project configuration
project = '{{ cookiecutter.name }}'
copyright = '%d, %s' % (datetime.now().year, {{ cookiecutter.slug }}.__author__)
author = {{ cookiecutter.slug }}.__author__
version = {{ cookiecutter.slug }}.__version__
release = {{ cookiecutter.slug }}.__version__

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
master_doc = 'index'
autodoc_member_order = 'bysource'
napoleon_include_init_with_doc = True

# HTML configuration
html_theme = 'alabaster'
html_theme_options = {
    'fixed_sidebar': True,
    'logo_name': True,
    'github_user': '{{ cookiecutter.author_github_username }}',
    'github_repo': '{{ cookiecutter.package }}'
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html'
    ]
}
html_static_path = ['static']
