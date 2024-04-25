import json
import logging
import traceback

from loguru import logger


class InterceptHandler(logging.Handler):
    """Intercepter Class"""

    @staticmethod
    def format_exception(exc_info):
        """Formats multiple exec into a single entity"""
        return "".join(traceback.format_exception(*exc_info))

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        """Create a dictionary from the log record"""
        log_record = {
            "name": record.name,
            "level": record.levelname,
            "message": record.getMessage(),
            "pathname": record.pathname,
            "lineno": record.lineno,
            "funcName": record.funcName,
            "exc_info": (
                self.format_exception(record.exc_info) if record.exc_info else None
            ),
        }

        # Convert the dictionary to a JSON string
        json_log_record = json.dumps(log_record)

        # Log using loguru with the JSON string
        logger_opt = logger.opt(depth=7, exception=record.exc_info)
        logger_opt.log(record.levelname, json_log_record)
