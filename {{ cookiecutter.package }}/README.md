# {{ cookiecutter.package }}

{{ cookiecutter.description }}

## Getting started

Install this package with

```bash
pip install {{ cookiecutter.package }}
```

## Usage

You can use it like this

```python
import {{ cookiecutter.slug }}

# TODO: demonstrate example
```
{% if cookiecutter.license_file == 'yes' %}
## License

This project is licensed under the MIT License. See the [LICENSE] file.

[LICENSE]: LICENSE
{% endif -%}
