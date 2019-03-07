# easy_daemon

![Python Logo](http://www.python.org/images/python-logo.gif)

Very simple base daemon class. Just override method 'run'.

Example
-------

    #!/usr/bin/env python3

    import sys
    import time
    import logging
    from easy_daemon.daemon import Daemon


    class ExecDaemon(Daemon):
        def run(self):
            while True:
                self.logger.info('daemon worked')
                time.sleep(5)


    if __name__ == "__main__":
        logger = logging.getLogger('very_simple')
        handler = logging.FileHandler('/tmp/very_simple.log', encoding='utf8')
        form = '%(levelname)-10s|%(asctime)s|%(process)d --- %(message)s (%(filename)s:%(lineno)d)'
        handler.setFormatter(logging.Formatter(form))
        logger.addHandler(handler)
        logger.setLevel(level=logging.INFO)
        daemon = ExecDaemon('/tmp/very_simple.pid', logger)
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
