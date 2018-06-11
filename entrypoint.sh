#!/bin/sh

ARG1=$1
shift

case $ARG1 in
    "")
        exec ./manage.py runserver 0.0.0.0:8000;;
    manage|manage.py)
        exec ./manage.py $@;;
    *)
        exec "${ARG1}" $@;;
esac
