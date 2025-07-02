import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),#This creates a handler that writes all log messages to the file called app1.log.
        logging.StreamHandler() #This creates a handler that writes log messages to the console (stdout).
    ]
)

logger=logging.getLogger("AritAhPP")


def add(a,b):
    result=a+b
    logger.debug(f"addition of {a} and {b} is,{result}")
    return result
def sub(a,b):
    result=a-b
    logger.debug(f"sustraction of {a} and {b} is,{result}")
    return result
def mul(a,b):
    result=a*b
    logger.debug(f"multiplication of {a} and {b} is,{result}")
    return result
def div(a,b):
    try:
        result=a/b
        logger.debug(f"division of {a} and {b} is,{result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero error")
        return None
    
add(10,15)
sub(2,10)
mul(4,5)
div(3,10)