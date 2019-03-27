{{ cookiecutter.package }}
{{ '=' * (cookiecutter.package | length) }}

{{ cookiecutter.description }}

Getting started
---------------

Install this package with

::

    pip install {{ cookiecutter.package }}

Usage
-----

You can use it like this

::

    import {{ cookiecutter.slug }}

    # TODO: demonstrate example
{% if cookiecutter.license_file == 'yes' %}
License
-------

This project is licensed under the MIT License.
{% endif -%}
