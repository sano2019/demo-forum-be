import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import Language

logger = logging.getLogger('default')


class Command(BaseCommand):
    help = "This command updates translations from Locize and runs compile messages"

    def handle(self, *args, **kwargs):
        logger.info('Running management command: update_locize_translations')

        project_id = settings.LOCIZE_PROJECT_ID
        languages = Language.objects.all()
        language_codes = list(languages.values_list('code', flat=True))
        base_path = settings.LOCALE_PATHS[0]
        path = os.path.join(base_path, language_codes[0])

        for language_code in language_codes:
            path = os.path.join(base_path, language_code, "LC_MESSAGES")
            base_command = "locize download --format po"
            namespace = "admin"
            print("Running locize download")
            command = "{} --project-id {} --path {} --language {} --namespace {}".format(
                base_command, project_id, path, language_code, namespace
            )
            os.system(
                command
            )
            os.system("mv {0}/admin.po {0}/django.po".format(path))
            print("Running manage.py compilemessages")
            os.system(
                "python3 {}/manage.py compilemessages".format(
                    settings.BASE_DIR
                )
            )
