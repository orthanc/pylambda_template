This project is a template for python based lambda functions.

Tools and Concepts
==================

Dependency Management
---------------------

Dependencies are managed using [Pipenv](https://pipenv.readthedocs.io/en/latest/) because it provides some
nice management concepts.

Note, it's important to set `PIPENV_IGNORE_VIRTUALENVS=1` unless pipenv is installed globally since you don't want
to reuse the virtual env with pip env.


pipenv --venv tells you the location of the virtual env, likely useful for latter packaging
