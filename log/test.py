from logger import logging
def add(a,b):
    logging.debug("this is an addition operation")
    return a+b
logging.debug("addition function is called")
res=add(10,3)
print(res)