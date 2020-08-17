#!/bin/bash
su django << 'EOF'

source ~/env/bin/activate
cd ~/project

# Usage:
# * * * * * bash ~/project/bin/update_translations_from_locize.sh live > ~/logs/crontab.log 2>&1
# This should be run as root to be able to restart the uwsgi

python3 projectile/manage.py update_locize_translations --settings=projectile.settings_staging

EOF

service uwsgi stop
service uwsgi start
