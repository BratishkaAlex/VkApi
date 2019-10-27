import email
import imaplib

from framework.custom_waites.mail_was_sent import MailWasSent
from framework.models.web_driver_wait import DriverWait
from resources import mail_config, config


def delete_all_emails(mail_model):
    with imaplib.IMAP4_SSL(mail_config.HOST, mail_config.PORT) as mail:
        mail.login(mail_model.login, mail_model.password)
        mail.select("Inbox")
        typ, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        for num in id_list:
            mail.store(num, '+FLAGS', '\\Deleted')
        mail.expunge()


def get_first_message(mail_model):
    with imaplib.IMAP4_SSL(mail_config.HOST, mail_config.PORT) as mail:
        mail.login(mail_model.login, mail_model.password)
        mail.select("Inbox")
        typ, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        if len(id_list) > 0:
            result, data = mail.fetch(id_list[0], "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            return get_text_block(email_message)
        else:
            raise RuntimeError("There is no emails in box")


def get_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload(decode=True)
    elif maintype == 'text':
        return email_message_instance.get_payload()


def is_mail_sent(mail_model):
    try:
        get_first_message(mail_model)
        return True
    except RuntimeError:
        return False


def wait_while_email_received(mail):
    DriverWait(config.TIMEOUT_FOR_EMAIL, 1).wait.until(
        MailWasSent(mail))
