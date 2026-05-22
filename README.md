# Koios JSON Logger
This is a logger for the Koios framework, that logs information in the JSON format.

## Installation & Usage
To use this module, simply put this project under `./koios/app/logging_json`. That's it!. No need to modify any code.
Make sure the folder name is correct. The best way to make sure is to clone the project as such:
```bash
cd <your_koios_folder>/app
git clone https://github.com/northernsec/koios_logging_json logging_json
```

## Configuration
This logger is configured through the `.env` file.

| Variable | Description | Default Value |
|---|---|---|
|  **KOIOS_LOG_PATH** | Path for log storage. **NOTE:** This path is relative to the docker container. If you want to read the logs from outside the container, you should map a volume in the `docker-compose.yml` file, or write to the mapped application folder (default behavior) | logs  |
| **KOIOS_LOG_LEVEL** | Minimum level for alerts to log (DEBUG\|INFO\|WARNING\|ERROR\|CRITICAL) | INFO |

## Log Files
In the log directory, the logger creates the following files:

| Log File | Usage |
|---|---|
| **koios.log** | Logs alerts from the Koios framework. In practice, this means any logs created by a `django` or `koios` logger. |
| **applets.log** | Logs alerts for any applet. In practice, this means any logs created by any logger that are not the above. |

## Log Format
These are some examples of logs you can expect in `koios.log`:
**Note:** the log has been indented for readability, but is not indented by default. You can use `jq` to help you indent, search, and slice the logs.
```json
{
    "applet": "my_applet",
    "level": "WARNING",
    "pathname": "/usr/src/app/koios/urls.py",
    "lineno": 37,
    "logger": "koios",
    "message": "No URLs file found for my_applet",
    "time": "2026-05-22T09:04:04.181726+00:00"
}
{
    "request": "<socket.socket fd=6, family=2, type=1, proto=0, laddr=('172.18.0.3', 8000), raddr=('172.18.0.1', 40320)>",
    "server_time": "22/May/2026 09:05:16",
    "status_code": 302,
    "level": "INFO",
    "pathname": "/usr/local/lib/python3.11/site-packages/django/core/servers/basehttp.py",
    "lineno": 213,
    "logger": "django.server",
    "message": "\"GET / HTTP/1.1\" 302 0",
    "time": "2026-05-22T09:05:16.542564+00:00"
}
```

You'll see that some keys are recurrent in every log, like the **level**, **pathname**, **lineno**, and **message** among others. Other keys may be unique to certain log entries, and can add additional information.
Extra information can be added when logging, like the example below:
```python
logger.error(
    f"Dependency missing while importing {applet}.urls: {e.name}",
    extra={'error': e, 'applet': applet}
)
```
