#!/usr/bin/env python3

import sys
import time
from config import args, _
from helpers import get_logger
from easy_daemon.daemon import Daemon

# ----------------------------------------------------------------------------------------------------------------------


class ExecApplication:
    """

    Daemonized application

    """
    def __init__(self, exec_logger):
        self.logger = exec_logger

    def run(self):
        """

        Run application

        """
        while True:
            self.logger.info(_('daemon worked'))
            time.sleep(5)


# ----------------------------------------------------------------------------------------------------------------------


class ExecDaemon(Daemon):
    """

    Daemon

    """
    def run(self):
        """

        Run process

        """
        exec_daemon = ExecApplication(self.logger)
        exec_daemon.run()

########################################################################################################################
#                                                    Entry point                                                       #
########################################################################################################################


DEBUG = False
LOG_FORMAT = '%(levelname)-10s|%(asctime)s|%(process)d|%(thread)d| %(name)s --- %(message)s (%(filename)s:%(lineno)d)'

if __name__ == "__main__":

    try:
        logger = get_logger('simple', LOG_FORMAT, '/tmp/simple.log')
        if DEBUG:
            exec_application = ExecApplication(logger)
            exec_application.run()
        else:
            daemon = ExecDaemon(args.get('pid_file', '/tmp/simple.pid'), logger)
            if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                    daemon.start()
                elif 'stop' == sys.argv[1]:
                    daemon.stop()
                elif 'restart' == sys.argv[1]:
                    daemon.restart()
                else:
                    print("Unknown command")
                    sys.exit(2)
                sys.exit(0)
            else:
                print("usage: %s start|stop|restart" % sys.argv[0])
                sys.exit(2)
    except PermissionError:
        print('there is not permissions to open log file')
        exit(1)
