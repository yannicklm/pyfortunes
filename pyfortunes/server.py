""" An XML RPC server for a fortune database

"""

import os
import argparse
from SimpleXMLRPCServer import SimpleXMLRPCServer

class FortunesServer(SimpleXMLRPCServer):
    """
    Initialiazed with a fortune directory.

    Can do stuff like:
     - print a fortune at random
     - add a new fortune
     - list fortune categories
    """
    def __init__(self, directory, port=8080):
        self.directory = directory
        SimpleXMLRPCServer.__init__(self, ("0.0.0.0", port))
        self.register_function(self.add_fortune)
        self.register_function(self.get_categories)

    def add_fortune(self, category, text):
        print "Adding", category, text
        return True

    def get_categories(self):
        return ["misc", "jokes", "movies"]

    def get_fortunes_zip(self):
        """ Returns an url where to download the whole fortunes
        collection

        """
        return ""



def run_server(directory, port):
    """ Runs a fortunes server

    """
    server = FortunesServer(directory, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fortune_directory")
    parser.add_argument("--port",
        help="Port to listen to. Defaults to 8080",
        type=int)
    parser.set_defaults(
        port='8080')
    args = parser.parse_args()
    fortune_directory = args.fortune_directory
    fortune_directory = os.path.abspath(fortune_directory)
    if not os.path.isdir(fortune_directory):
        raise Exception("'%s' is not a directory!" % fortune_directory)
    run_server(fortune_directory, args.port)

if __name__ == "__main__":
    main()


