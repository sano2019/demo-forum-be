#!/bin/bash

source ~/env/bin/activate
cd ~/project

# Usage:
# * * * * * ~/project/bin/create_missing_lists.sh live > ~/logs/crontab.log 2>&1

python projectile/manage.py create_missing_lists --settings=projectile.settings_live
