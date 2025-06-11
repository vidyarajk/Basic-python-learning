import logging
logging.basicConfig(
    filename="app.log", # <---- This sets up a file for logging output
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)