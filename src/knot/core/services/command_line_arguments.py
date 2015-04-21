from kao_decorators import proxy_for

import sys

@proxy_for('_args', ['__getitem__', '__iter__', '__len__'])
class CommandLineArguments:
    """ Service to provide access to the command line arguments """
    
    @property
    def _args(self):
        """ Return the arguments """
        return sys.argv