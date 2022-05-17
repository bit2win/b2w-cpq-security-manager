import logging


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    blue = "\x1b[34m"
    green = "\x1b[32m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = (
        "{color}"
        + "%(levelname)s"
        + reset
        + ":"
        + "\t"
        + "%(asctime)s - %(name)s: %(message)s "
        + "("
        + "{color}"
        + "%(pathname)s:%(lineno)d"
        + reset
        + ")"
    )

    FORMATS = {
        logging.DEBUG: format.format(color=blue),
        logging.INFO: format.format(color=green),
        logging.WARNING: format.format(color=yellow),
        logging.ERROR: format.format(color=red),
        logging.CRITICAL: format.format(color=bold_red),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
