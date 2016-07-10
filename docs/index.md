# Overview

TODO

## Table of Contents

  * [Changelog]

## Installation

You will need `git`, `python 2.7+` and `pip` to install this project and its
dependencies.

Clone the repository and change directory:

    $ git clone git@github.com:<project_name>.git
    $ cd <project_name>

Create a virtualenv and install dependencies:

    $ pip install -U virtualenv
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt

You MUST **review** the appropriate environment specific
configuration in the local settings module:

    (venv)$ cp lineo_testapp/settings/local_sample.py lineo_testapp/settings/local.py
    (venv)$ $EDITOR lineo_testapp/settings/local.py

Migrate the database and collect static files:

    (venv)$ ./manage.py migrate

    # If `DEBUG=False`.
    (venv)$ ./manage.py collectstatic

## Usage

Use standard django command for run the project:

    (venv)$ ./manage.py runserver

You can also use [django-extensions] command:

    (venv)$ ./manage.py runserver_plus

## HTML Docs

Docs are written in [Markdown]. You can use [MkDocs] to preview your
documentation as you are writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[Changelog]: changelog.md
[django-extensions]: http://django-extensions.readthedocs.io/en/latest/
[Markdown]: http://daringfireball.net/projects/markdown/
[MkDocs]: http://mkdocs.org
