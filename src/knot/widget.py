
class Widget:
    """ Represents a widget within Knot """
    
    def __init__(self, painter):
        """ Initialize the widget with its painters """
        self.painter = painter
        
    def draw(self, parent):
        """ Draw the widget given its parent """
        self.__qwidget = self.painter.draw()
        self.__qwidget.setParent(parent)
        self.__qwidget.show()
        
    @property
    def width(self):
        """ Return the widget's width """
        return self.__qwidget.width()