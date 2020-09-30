import logging
import syslog

log_format="%(asctime)s:%(levelname)s:%(filename)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format, #filename="app.log"
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler("app.log")
                    ]
                    )

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.fatal("Fatal errror")

try:
    x = 0
    y = 1 / x
except Exception as exc:
    logging.critical(exc, exc_info=True)