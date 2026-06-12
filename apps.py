import logging
from django.apps import AppConfig

from logging_json.logs import LOG_ROOT, LOGGING_CONF, IgnoreHealthCheck

# Removes health-check pings, unless they fail.
logging.getLogger("django.server").addFilter(IgnoreHealthCheck())


class LoggingJsonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name        = 'logging_json'
    applet_meta = {
        "nav":          {},
        "url_slug":     "logging",
        "dependencies": {
            'extra_vars': {
                'LOGGING': LOGGING_CONF,
            },
        }
    }
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
