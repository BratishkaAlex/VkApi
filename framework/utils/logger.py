import logging
import logging.config

from resources import config

logging.basicConfig(level=config.LOGGING_LEVEL, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


def info(message):
    logging.info(message)


def warning(message):
    logging.warning(message)


def error(message):
    logging.error(message)


def debug(message):
    logging.debug(message)


def step(message, counter):
    logging.info("<<<<<<<<Step %d>>>>>>>>>>>>.\n%s\n" % (counter, message))
