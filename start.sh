#!/bin/bash

if [ ! -f .env ]; then
    echo ".env not populated, running install first..."
    ./install.sh
fi

auditorium run demo.py