import logging
import datetime

# Create current date string for log file name
log_now = datetime.datetime.now()
log_now = log_now.strftime('%m_%d_%Y')

LOG_FILENAME = 'Adyen %s.log' % log_now

logger = logging.getLogger(LOG_FILENAME)
logger.setLevel(logging.DEBUG)


# TODO: Make logging optional based on Adyen class instance attribute 'create_log'.
# TODO: Define a clear logging structure.

# fh = logging.FileHandler(LOG_FILENAME)
# formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
# fh.setFormatter(formatter)
# fh.setLevel(logging.DEBUG)
# logger.addHandler(fh)
# logger.info('Adyen Log of %s' % log_now)

def logname():
    return LOG_FILENAME

def getlogger():
    return logger
