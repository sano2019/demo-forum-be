import os
import sys
import site

# The home directory of the user
USERHOME_DIR = '/home/django'

# Django directory, where manage.py resides
PROJECT_DIR = os.path.join(USERHOME_DIR, 'project/projectile')

# Site-packages under virtualenv directory
SITEPACK_DIR = os.path.join(USERHOME_DIR, 'env/lib/python3.6/site-packages')
site.addsitedir(SITEPACK_DIR)

sys.path.append(PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'projectile.settings_live'
os.environ["CELERY_LOADER"] = "django"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
