import os
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger('vow_logger')
logger.setLevel(logging.INFO)
dir = os.environ.get('LOG_DIR', "/tmp/")
if logger.handlers is not None:
    if not os.path.isdir(dir):  # type: ignore
        os.makedirs(dir)  # type: ignore
    logFileHandler = logging.FileHandler(
        dir + '/' + 'tmp.log')
    # see https://github.com/python/mypy/issues/6233
    logConsoleHandler = logging.StreamHandler()  # type: ignore
    logHandlers = [logConsoleHandler, logFileHandler]
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
    for handler in logHandlers:
        handler.setFormatter(formatter)  # type: ignore
        logger.addHandler(handler)  # type: ignore
