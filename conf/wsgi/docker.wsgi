import os
import sys
import site

# The home directory of the user
USERHOME_DIR = '/project'

# Django directory, where manage.py resides
PROJECT_DIR = os.path.join(USERHOME_DIR, 'projectile')

# Site-packages under virtualenv directory
SITEPACK_DIR = os.path.join(USERHOME_DIR, '/usr/local/lib/python3.8/site-packages')
site.addsitedir(SITEPACK_DIR)

sys.path.append(PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'projectile.settings_live'
os.environ["CELERY_LOADER"] = "django"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
