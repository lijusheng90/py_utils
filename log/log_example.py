import logging
import os


def get_log_level(ENV_LOG_LEVEL):
    log_level = os.environ.get(ENV_LOG_LEVEL, 'info').lower()

    if log_level == 'debug':
        return logging.DEBUG
    elif log_level == 'info':
        return logging.INFO
    elif log_level == 'warning' or log_level == 'warn':
        return logging.WARNING
    elif log_level == 'error':
        return logging.ERROR
    else:
        return logging.INFO


def get_log_format(ENV_LOG_FORMAT):
    default_log_format = "%(asctime)s %(levelname)s %(filename)s:%(lineno)d thread(%(thread)d) %(message)s"
    return os.environ.get(ENV_LOG_FORMAT, default_log_format)


if __name__ == '__main__':
    log_format = get_log_format("xxx_LOG_FORMAT")
    log_level = get_log_level("xxx_LOG_FORMAT")
    logging.basicConfig(format=log_format, level=log_level)

    logger = logging.getLogger(__name__)
    logger.info("i'm info")
    logger.warning("i'm warning")
    logger.debug("i'm debug")
    logger.error("i'm error")

    xxxx_log_level = os.environ.get("XXX_LOG_LEVEL", "DEBUG")
    logging.getLogger('test_logger').setLevel(logging.getLevelName(xxxx_log_level))
    logger = logging.getLogger("test_logger")
    logger.info("i'm info")
    logger.warning("i'm warning")
    logger.debug("i'm debug")
    logger.error("i'm error")
