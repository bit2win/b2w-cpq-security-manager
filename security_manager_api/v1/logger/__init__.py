import logging
import os
from typing import sys

from .custom_formatter import CustomFormatter


def get_logger(name: str, log_level=None, stream_handler=None) -> logging.Logger:
    # create logger
    logger = logging.getLogger(name)
    # create console handler and set level
    if log_level is not None:
        handler = logging.StreamHandler(stream_handler)
    else:
        handler = logging.StreamHandler(sys.stdout)

    if log_level is not None:
        logger.setLevel(log_level)
        handler.setLevel(log_level)
    else:
        logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
        handler.setLevel(os.getenv("LOG_LEVEL", "INFO"))

    # add custom formatter to handler
    handler.setFormatter(CustomFormatter())
    # add handler to logger
    logger.addHandler(handler)
    # avoid log propagation to stdout logger
    logger.propagate = False

    # MAKE IT CONFIGURABLE TO USE ONLY IN TEST
    # logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

    return logger
