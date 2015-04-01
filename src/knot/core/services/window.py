from knot.service_provider import ServiceProvider

from kao_decorators import proxy_for
from smart_defaults import smart_defaults

import os

@proxy_for('window', ['title'])
class Window:
    """ Service to provide interaction with the main window """
    
    @smart_defaults
    def __init__(self, app=ServiceProvider()):
        """ Initialize the Window Service with the app service """
        self.window = app.window 