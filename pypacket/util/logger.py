import logging
import os
from time import localtime, strftime
from pypacket.util.colors import Colors


class Logger:
    """A utility logger class for purposes of logging things to console as
    well as to file via the Python logging utility.
    """

    SYS_PREFIX = '[SYS] '
    ERR_PREFIX = '[ERR] '
    WRN_PREFIX = '[WRN] '
    REC_PREFIX = '[REC] '
    HTML_PREFIX = '[JSON] '
    #LOG_DIRECTORY = 'logs'
    LOG_DIRECTORY = '/var/log/pypacket'

    def __init__(self):
        """Sets up the logger, via calling setup()."""
        self.__setup()

    def log_info(self, log_message):
        """Logs an info message to console, file.

        Args:
            log_message: The string message to log.
        """
        self.__log_any(Colors.BLUE, self.SYS_PREFIX, log_message)
        logging.info(log_message)

    def log_html(self, log_message):
        """Logs a html message to console, file.

        Args:
            log_message: The string message to log.
        """
        json_message = '{'
        try:
            x = aprslib.parse(log_message)
            t = time()
            json_message = json_message + '"time":"' + str(ctime(t)) + '"'
            try:
                json_message += ',"from":"' + str(x["from"]) + '"'
            except:
                json_message += ',"from":"error"'
            try:
                json_message += ',"to":"' + str(x["to"]) + '"'
            except:
                json_message += ',"to":"error"'
            try:
                json_message += ',"longitude":"' + str(x["longitude"]) + '"'
            except:
                json_message += ',"longitude":"error"'
            try:
                json_message += ',"latitude":"' + str(x["latitude"]) + '"'
            except:
                json_message += ',"latitude":"error"'
            try:
                json_message += ',"comment":"' + str(x["comment"]).replace("\"", "\\\"") + '"'
            except:
                json_message += ',"comment":"error"'
            try:
                json_message += ',"via":"' + str(x["via"]) + '"'
            except:
                json_message += ',"via":"error"'
            try:
                json_message += ',"symbol":"' + str(x["symbol"]) + '"'
            except:
                json_message += ',"symbol":"error"'
            try:
                json_message += ',"raw":"' + str(x["raw"]).replace("\\", "\\\\").replace("\"", "\\\"") + '"'
            except:
                json_message += ',"raw":"error"'
            try:
                json_message += ',"path":"' + str(x["path"]) + '"'
            except:
                json_message += ',"path":"error"'
            json_message += ',"source":"RF"'
            log_message = json_message + '}'
        except:
            log_message = 'An exception occurred'
        json_message = json_message + '}'

        self.__log_any(Colors.BLUE, self.HTML_PREFIX, log_message)
        logging.info('[JSON] ' + log_message)

    def log_error(self, log_message):
        """Logs an error message to console, file.

        Args:
            log_message: The string message to log.
        """
        self.__log_any(Colors.RED, self.ERR_PREFIX, log_message)
        logging.error(log_message)

    def log_warn(self, log_message):
        """Logs a warning message to console, file.

        Args:
            log_message: The string message to log.
        """
        self.__log_any(Colors.YELLOW, self.WRN_PREFIX, log_message)
        logging.warning(log_message)

    def log_packet(self, raw_message, friendly_message):
        """Logs a raw packet message to file, friendly to console.
        Intended to log raw, decoded APRS packets to file with a user-readable
        version to the CLI.

        Args:
            raw_message: The raw string message to log to file.
            friendly_message: The user friendly message to log to CLI.
        """
        self.__log_any(Colors.RESET, '', friendly_message)
        logging.info(raw_message)

    def __log_any(self, color, prefix, log_message):
        """Logs any message to system console.

        Args:
            color: The color escape sequence to use.
            prefix: A string prefix such as [INFO].
            log_message: The string friendly_message to log.
        """
        print(color + prefix + Colors.RESET + log_message)

    def __setup(self):
        """Sets up the logger. First checks to see if the log directory exists.
        If the directory does not exist, it creates it.

        Then, configures the Python logger with our chosen format and a file
        name based upon the date / time when the logger instance is initialized.
        """
        if not os.path.exists(self.LOG_DIRECTORY):
            os.makedirs(self.LOG_DIRECTORY)

        log_format = '[%(asctime)-15s] [%(levelname)s] %(message)s'
        log_file_name = self.LOG_DIRECTORY + '/pypacket_' + strftime("%Y_%m_%d_%H_%M_%S", localtime()) + '.log'
        logging.basicConfig(filename=log_file_name, format=log_format, level=logging.INFO)
