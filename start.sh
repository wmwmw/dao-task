#!/bin/bash

case "$1" in
"bash")
    docker-compose -f docker-compose.yml run host /bin/bash
    ;;

"shell")
    docker-compose -f docker-compose.yml run host python3 manage.py shell
    ;;

"migrate")
    docker-compose -f docker-compose.yml run host python3 manage.py migrate
    ;;

"makemigrations")
    docker-compose -f docker-compose.yml run host python3 manage.py makemigrations "${@:2}"
    ;;

*)
    docker-compose -f docker-compose.yml build
    docker-compose -f docker-compose.yml up
    ;;
esac
