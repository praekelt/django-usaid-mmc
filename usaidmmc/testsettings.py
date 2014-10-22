from usaidmmc.settings import *  # flake8: noqa

SECRET_KEY = 'THIS-IS-FOR-TESTS'

DATABASE_URL='postgres://postgres:@/test_usaidmmc'
DATABASES = {
    'default': dj_database_url.config(default='postgres:///test_usaidmmc'),
}
