#!/bin/bash
echo "Bluetooth Time & Date Update Automation Script STARTED"
echo "(Make sure you updated the active directories in this script)"
source "./dev/bin/activate"
python3 ./time_write.py
