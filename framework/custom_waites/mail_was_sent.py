from framework.utils.mail_utils import MailUtils


class mail_was_sent:
    def __init__(self, mail):
        self.__mail = mail

    def __call__(self, driver):
        return MailUtils.is_mail_sent(self.__mail)
