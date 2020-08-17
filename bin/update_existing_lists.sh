#!/bin/bash

source ~/env/bin/activate
cd ~/project

# Usage:
# * * * * * ~/project/bin/update_existing_lists.sh live > ~/logs/crontab.log 2>&1

python projectile/manage.py update_existing_lists --settings=projectile.settings_live
