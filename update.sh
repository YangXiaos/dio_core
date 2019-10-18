#!/bin/sh

echo "$1" | sudo -S python3 setup.py install
echo "$1" | sudo -S chmod 777 * -R
