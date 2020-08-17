from django.core import mail

from common.helpers.logger import LoggingHelper


def send_email_helper(
    logger, to_email, subject, body, bcc=[], attachment=None
):
    msg = mail.EmailMultiAlternatives(subject=subject, to=[to_email], bcc=bcc)
    msg.attach_alternative(body, "text/html")
    if attachment:
        msg.attach_file(attachment)
    msg.send()
    log_msg = ['Email sent to: {}'.format(to_email)]
    log_msg.append(', Subject: {}'.format(subject))
    log_msg.append('Body: {}'.format(body))
    if attachment:
        log_msg.append('Attachment: {}'.format(attachment))
    LoggingHelper.create_log(logger=logger, messages=log_msg, level='INFO')
