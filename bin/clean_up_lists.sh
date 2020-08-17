#!/bin/bash

source ~/env/bin/activate
cd ~/project

# Usage:
# * * * * * ~/project/bin/clean_up_lists.sh live > ~/logs/crontab.log 2>&1

python projectile/manage.py clean_up_lists --settings=projectile.settings_live
