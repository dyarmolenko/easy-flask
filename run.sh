#! /bin/bash

if [ $FLASK_ENV = "development" ]; then
    flask run
fi