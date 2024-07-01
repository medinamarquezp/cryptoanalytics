import logging as log

log_level = log.DEBUG
log_format = '%(asctime)s - %(levelname)s - %(filename)s [%(lineno)d] (%(funcName)s): %(message)s'

log.basicConfig(level=log_level, format=log_format)
