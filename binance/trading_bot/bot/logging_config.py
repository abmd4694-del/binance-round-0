import logging
import sys
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_file="trading_bot.log", log_level=logging.INFO):
    """
    Configures logging to both console and a file.
    """
    # Create a custom logger
    logger = logging.getLogger("trading_bot")
    logger.setLevel(log_level)
    
    # Avoid adding handlers multiple times if function is called repeatedly
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)

    c_handler.setLevel(log_level)
    f_handler.setLevel(log_level)

    # Create formatters and add it to handlers
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger
