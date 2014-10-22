#!/bin/sh
export DATABASE_URL="sqlite://:memory:"
export DJANGO_SETTINGS_MODULE="usaidmmc.testsettings"
./manage.py test "$@"
