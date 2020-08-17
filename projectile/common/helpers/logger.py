import logging

from django.utils import timezone


class LoggingHelper:
    def create_log(logger, messages=[], level='ERROR'):
        now = timezone.now()
        log = ['--------------------']
        log.append('{} logged at:'.format(level))
        log.append(str(now))
        for msg in messages:
            log.append(msg)
        log_msg = '\n'.join(log)
        log_level = getattr(logging, level.upper())
        logger.log(log_level, log_msg)
