import logging
import sys
from logging.handlers import TimedRotatingFileHandler
import os
FORMATTER = logging.Formatter("%(asctime)s - %(name)-20s - %(lineno)d - %(levelname)-8s - %(message)s")


def get_logger(logger_name, log_file_path):

    def configure_handlers():
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(FORMATTER)
        logger.addHandler(console_handler)

        file_handler = TimedRotatingFileHandler(log_file_path, when='midnight')
        file_handler.setFormatter(FORMATTER)
        logger.addHandler(file_handler)

    def create_log_file():
        log_dir = os.path.dirname(log_file_path)
        if len(log_dir) != 0:
            os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)

    create_log_file()
    configure_handlers()

    return logger
