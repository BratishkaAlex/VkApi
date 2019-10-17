import logging
import logging.config

from resources import config


class Logger:
    logging.basicConfig(level=config.Logging_level, filename="log.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def debug(message):
        logging.debug(message)

    @staticmethod
    def step(message, counter):
        logging.info("<<<<<<<<Step %d>>>>>>>>>>>>.\n%s\n" % (counter, message))
