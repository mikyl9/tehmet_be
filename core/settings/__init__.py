"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `developement`.
To change settings file:
`DJANGO_ENV=local python manage.py runserver`
"""

from os import environ

from split_settings.tools import include

ENV = environ.get("DJANGO_ENV") or "local"

base_settings = [
    "components/*.py",
    # select your environment file
    "environments/{0}.py".format(ENV),
]

# Include settings:
include(*base_settings)
