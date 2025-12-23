#!/usr/bin/env bash

while true; do
    . venv/bin/activate
    echo "Starting Aurisu"
    python kurisu.py
    echo "Bot exited. Restarting in 3 seconds."
    sleep 3
done
