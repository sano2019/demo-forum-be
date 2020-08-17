#!/bin/bash

source ~/env/bin/activate
cd ~/project

# Usage:
# * * * * * ~/project/bin/add_new_users_to_list.sh live > ~/logs/crontab.log 2>&1

python projectile/manage.py add_new_users_to_list --settings=projectile.settings_live
