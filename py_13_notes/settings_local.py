
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-el7#rn&ajm+lw6+9ztj7j85ba=r^zdq9_19wfytd*m8i+(r3j='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'py13user',
        'PASSWORD': 'mypass',
        'NAME': 'py13db',
        'TEST': {
            'NAME': 'py13db_test',
        },
    },
}