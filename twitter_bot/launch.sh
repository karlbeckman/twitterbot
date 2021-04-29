#!/bin/bash

TIME_STATE=false;
TWEETED=false;
while true; do 
    if $TIME_STATE; then 
        echo "Correct time..."
        if ! $TWEETED; then
            ./main.py
            TWEETED=true
            echo "...tweeted!"
        else
            echo "...already tweeted. "
        fi
    else
        echo "Not right time..."
    fi 

    if [ $(date +"%H") -eq "07" ]; then
        TIME_STATE=true;
    fi
    sleep 10;

done;