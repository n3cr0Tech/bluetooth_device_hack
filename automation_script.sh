#!/bin/bash
echo "Bluetooth Time & Date Update Automation Script STARTED"
echo "(Make sure you updated the active directories in this script)"
source "./bluetooth_project/dev/bin/activate"
python3 bluetooth_project/write_time.py