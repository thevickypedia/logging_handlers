import logging
from datetime import datetime
from importlib import reload
from os import mkdir, listdir
from pathlib import PurePath

mkdir('logs') if 'logs' not in listdir() else None  # Creates a repo for logs if not available already.

# Re-compile at module level to define a new set of objects.
# This is to avoid chaos while importing the same module across different program files/languages.
# Reference: https://docs.python.org/3/library/importlib.html#importlib.reload
reload(module=logging)

# Setup a custom format for time, logging level, function name and line number before the log message
# Formatter reference: https://docs.python.org/3/library/logging.html#logging.Formatter
# Format attributes reference: https://docs.python.org/3/library/logging.html#logrecord-attributes
logFormatter = logging.Formatter(
    fmt="%(asctime)s - [%(levelname)s] - %(name)s - %(funcName)s - Line: %(lineno)d - %(message)s",
    datefmt='%b-%d-%Y %H:%M:%S'
)

# Return a logger with the specified name.
# Reference: https://docs.python.org/3/library/logging.html#logging.getLogger
fileLogger = logging.getLogger('FILE')
consoleLogger = logging.getLogger('CONSOLE')
rootLogger = logging.getLogger(PurePath(__file__).stem)  # PurePath(__file__).stem is used to retain only the file name

# Send logging output to a file.
# Reference: https://docs.python.org/3/library/logging.handlers.html#filehandler
fileName = datetime.now().strftime('logs/multi_handlers_%H:%M:%S_%d-%m-%Y.log')  # FileName in dir with current datetime
fileHandler = logging.FileHandler(filename=fileName)
fileHandler.setFormatter(fmt=logFormatter)  # Sets the Formatter for this handler to fmt.
fileLogger.setLevel(level=logging.DEBUG)  # Sets the threshold for this logger to level.
fileLogger.addHandler(hdlr=fileHandler)  # Adds the specified handler to this logger.

# Returns a new instance of StreamHandler class. If stream is specified, the instance will use it for logging output.
# Reference: https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(fmt=logFormatter)  # Sets the Formatter for this handler to fmt.
consoleLogger.setLevel(level=logging.DEBUG)  # Sets the threshold for this logger to level.
consoleLogger.addHandler(hdlr=consoleHandler)  # Adds the specified handler to this logger.

# Returns a new instance of StreamHandler class. If stream is specified, the instance will use it for logging output.
# Reference: https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler
rootHandler = logging.StreamHandler()
rootHandler.setFormatter(fmt=logFormatter)  # Sets the Formatter for this handler to fmt.
rootHandler.setLevel(level=logging.CRITICAL)  # Sets the threshold for this logger to level.
rootLogger.addHandler(hdlr=fileHandler)  # Adds the specified handler to this logger.
rootLogger.addHandler(hdlr=consoleHandler)  # Adds the specified handler to this logger.


def multi_handlers() -> None:
    """Odd numbers are printed in stdout and even numbers are stored in a log file.

    >>> rootLogger
        - Prints the log message in stdout and stores the same in the log file.

    >>> consoleLogger
        - Prints the log message in stdout.

    >>> fileLogger
        - Writes logging output in a file.

    """
    rootLogger.critical('Odd and Even numbers below 20.')  # prints in stdout and stores in log file
    for num in range(0, 20):
        if num % 2:
            consoleLogger.debug(f'{num} is an odd number.')  # prints in stdout
        else:
            fileLogger.debug(f'{num} is an even number.')  # stored in log file
    rootLogger.critical('End of loop.')  # prints in stdout and stores in log file


if __name__ == '__main__':
    multi_handlers()
