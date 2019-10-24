from framework.utils.mail_utils import is_mail_sent


class MailWasSent:
    def __init__(self, mail):
        self.__mail = mail

    def __call__(self, driver):
        return is_mail_sent(self.__mail)
