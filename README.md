This project is a template for python based lambda functions.

Tools and Concepts
==================

Executing
---------

The source files live in src.

These have to be executed as a module rather than a script so they can find other modules in src.

So that you don't have to be in source, add src to the PYTHONPATH. E.g

    PYTHONPATH=src python -m ocoen.example

to make this work with pipenv add the PYTHONPATH to the .env file

Dependency Management
---------------------

Dependencies are managed using [Pipenv](https://pipenv.readthedocs.io/en/latest/) because it provides some
nice management concepts.

Note, it's important to set `PIPENV_IGNORE_VIRTUALENVS=1` unless pipenv is installed globally since you don't want
to reuse the virtual env with pip env.


pipenv --venv tells you the location of the virtual env, likely useful for latter packaging

Building
--------

To build the lambda distro:

    rm  -rf build dist.zip
    pipenv run pip install --target build -r <(pipenv lock -r)
    cp -r src/* build/
    (cd build && zip -r ../dist.zip *)
