# coding=utf-8
import logging
import time

LOG_FILE = 'log.log'
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"


class LogHandler:
    log = logging.getLogger("root")

    def __init__(self):
        logging.basicConfig(format=FORMAT, filename=LOG_FILE)
        self.log.setLevel(logging.DEBUG)

    @staticmethod
    def debug(text):
        print(text)
        LogHandler.log.debug(time.strftime('%x %X') + " - " + str(text))

    @staticmethod
    def err(text):
        LogHandler.log.error(time.strftime('%x %X') + " - " + str(text))
