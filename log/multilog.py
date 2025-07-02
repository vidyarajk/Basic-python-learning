import logging
# create a logger for module 1
logger1=logging.getLogger("module 1")
logger1.setLevel(logging.DEBUG)

# create a logger for module 2
logger2=logging.getLogger("module 2")
logger2.setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger1.debug("debug message")
logger2.warning("wqarning message")