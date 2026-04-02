import json_log_formatter

from koios.config import Config

LOG_ROOT  = Config().log_path
LOG_LEVEL = Config().log_level

class JSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        extra.update(
            {"level":    record.levelname,
             "pathname": record.pathname,
             "lineno":   record.lineno,
             "logger":   record.name}
        )
        return super().json_record(message, extra, record)


LOGGING_CONF = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "[{levelname}] {name} {asctime}: {message}",
            "style": "{",
            "datefmt":   "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "()": "logging_json.logs.JSONFormatter",
        },
    },
    "handlers": {
        # File handler for Django
        "koios_file": {
            "class":     "logging.FileHandler",
            "filename":  LOG_ROOT / "koios.log",
            "formatter": "json",
            "level":     "DEBUG",
        },
        # File handler for applets
        "applet_file": {
            "class":     "logging.FileHandler",
            "filename":  LOG_ROOT / "applets.log",
            "formatter": "json",
            "level":     "DEBUG",
        },
        # Console logging
        "stdout": {
            "class":     "logging.StreamHandler",
            "formatter": "console",
            "level":     "INFO",
        },
    },
    "loggers": {
        "django": {
            "level": LOG_LEVEL,
            "handlers": [
                "koios_file",
                "stdout",
            ],
            "propagate": False,
        },
        "koios": {
            "level": LOG_LEVEL,
            "handlers": [
                "koios_file",
                "stdout",
            ],
            "propagate": False,
        },
        "": {
            "level": LOG_LEVEL,
            "handlers": [
                "applet_file",
                "stdout",
            ],
            "propagate": False,
        }
    }
}
