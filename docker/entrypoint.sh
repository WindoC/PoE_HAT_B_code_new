#!/bin/bash
set -e

# add logic to change the env without to re-create the container
if [ -f /.env ] ; then
    source /.env >/dev/null 2>&1
fi

APP=$1
ARGS=${@:2}

if [ "$APP" == "" ] ; then
    APP=MAIN
fi

CMD=
case $APP in

    MAIN)
        CMD="python3 main.py"
        ;;
    
esac

# the command
case $APP in

    MAIN)
        exec $CMD $ARGS
        ;;
    
    *)
        exec $@
        ;;
    
esac
