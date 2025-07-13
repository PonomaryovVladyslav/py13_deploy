import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i^m-t@4p9rb%pr_m1*qv$3zb%3$y5iyp$^ay1nodp(r8g1e*81'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['3.120.147.160', 'a-level-deploy.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'NAME': os.environ.get('DB_NAME'),
    },
}