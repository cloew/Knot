from knot import KnotService, use_knot_services

from kao_decorators import proxy_for

import os

@proxy_for('window', ['title'])
class Window:
    """ Service to provide interaction with the main window """
    
    @use_knot_services
    def __init__(self, app=KnotService):
        """ Initialize the Window Service with the app service """
        self.window = app.window 