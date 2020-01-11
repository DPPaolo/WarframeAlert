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
        LogHandler.log.debug(time.strftime('%x %X') + " - " + text)

    @staticmethod
    def err(text):
        LogHandler.log.error(time.strftime('%x %X') + " - " + text)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LogHandler_test(metaclass=Singleton):
    logger = None

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(threadName)s - %(message)s",
            handlers=[
                logging.StreamHandler()
            ])

        self.logger = logging.getLogger(__name__)

    @staticmethod
    def __get_call_info():
        import inspect
        stack = inspect.stack()

        # stack[1] gives previous function ('info' in our case)
        # stack[2] gives before previous function and so on

        fn = stack[2][1]
        ln = stack[2][2]
        func = stack[2][3]

        return fn, func, ln

    def info(self, message, *args):
        message = "{} - {} at line {}: {}".format(*self.__get_call_info(), message)
        self.logger.info(message, *args)