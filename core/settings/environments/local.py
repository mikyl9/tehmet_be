import os

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME") or "tehmet",
        "PORT": os.environ.get("DB_PORT") or 5432,
        "HOST": os.environ.get("DB_HOST") or "localhost",
        "USER": os.environ.get("DB_USER") or "postgres",
        "PASSWORD": os.environ.get("DB_PASSWORD") or "1234",
    }
}

ALLOWED_HOSTS = ["*"]
