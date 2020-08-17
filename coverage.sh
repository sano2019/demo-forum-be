#!/bin/bash
cd projectile/

coverage run --source='.' manage.py test --settings projectile.settings_test

coverage html
cd htmlcov

echo "Navigate to http://hashimoto.willandskill.eu:8080"
python -m http.server 8080

rm -Ir ../htmlcov/