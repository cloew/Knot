from knot import KnotService

from kao_decorators import proxy_for

@proxy_for('window', ['title'])
class Window:
    """ Service to provide interaction with the main window """
    app = KnotService('app')
    
    def __init__(self):
        """ Initialize the Window Service with the app service """
        self.window = self.app.window 