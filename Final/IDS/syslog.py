## Reference https://gist.github.com/marcelom/4218010

## Tiny Syslog Server in Python.
##
## This is a tiny syslog server that is able to receive UDP based syslog
## entries on a specified port and save them to a file.
## That's it... it does nothing else...
## There are a few configuration parameters.

# LOG_FILE = 'youlogfile.log'
HOST, PORT = "127.0.0.1", 5000

#
# NO USER SERVICEABLE PARTS BELOW HERE...
#

import logging
import socketserver
import sys


class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = bytes.decode(self.request[0].strip(), encoding="utf-8")
        socket = self.request[1]
        print("%s : " % self.client_address[0], str(data.encode("utf-8")))
        logging.info(str(data.encode("utf-8")))


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} log_file_name")
        sys.exit(0)

    try:
        LOG_FILE = sys.argv[1]
        logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")