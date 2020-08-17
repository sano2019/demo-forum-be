# Backend #

## Getting started with backend

This project is built with Django 2 using Python 3.x.

If you're using Visual Studio Code, make sure to install the Python
extension and that you select a Python 3.x interpreter.

### Preparation for new developer

Following assumes you have the project downloaded on a folder named {PROJECT_NAME} under your home folder on Hashimoto. Port 8000 below can be swapped out to any port that is usable at that specific time:

    cd ~/{PROJECT_NAME}/ && virtualenv -p python3 {PROJECT_NAME}-env
    source ~/{PROJECT_NAME}/{PROJECT_NAME}-env/bin/activate && cd ~/{PROJECT_NAME}/ && pip install -r requirements.txt
    cd ~/{PROJECT_NAME}/projectile/ && python manage.py runserver 0:8000

## django-reversion

We use [django-reversion] for audit logging. This mostly happens
automatically, but there are a couple of things to consider:

* When adding a new model [register it with
  django-reversion][reversion-register] if it needs to be auditable.

* If a view changes an auditable model, make sure it inherits from
  `revision.views.RevisionMixin`

* If you register an existing model, you need to run `./manage.py
  createinitialrevisions` in order to create the initial version of
  all existing models.

## Project Settings

We're using [Black](https://github.com/ambv/black) for automatic code
formatting and [flake8](https://pypi.org/project/flake8/) for linting.

If you're using Visual Studio Code, add these lines to your workspace
settings (i.e. `.vscode/settings.json`):

    "editor.formatOnPaste": false,
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false

For troubleshooting, check the [formatting][vs-py-fmt] and
[linting][vs-py-lint] sections of the Python extension docs.

[vs-py-fmt]: https://code.visualstudio.com/docs/python/editing#_formatting
[vs-py-lint]: https://code.visualstudio.com/docs/python/linting
[reversion]: https://github.com/etianen/django-reversion
[reversion-register]: https://django-reversion.readthedocs.io/en/stable/api.html#registering-models

## Hosting server settings

Following applications need to be manually installed on any new hosting 
environment:

    sudo apt install libpango1.0-0 libcairo2 libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-common gettext npm
    sudo npm install -g locize-cli

Following code needs to be run on a new hosting server:

    cd ~
    mkdir logs
    cd logs
    touch info.log
    mkdir nginx
    touch nginx/access.log
    touch nginx/error.log
    mkdir uwsgi
    touch uwsgi/uwsgi.log


## Render UML Diagram

`python projectile/manage.py graph_models -a -o models.png`


## Restore database

```
pg_dump -Fc django -U django -h localhost > live_backup.sql

pg_restore -Fc django.sql -U django -h localhost -d django --no-owner --clean --verbose --no-acl
```