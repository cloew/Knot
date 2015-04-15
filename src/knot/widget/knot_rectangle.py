from knot.sides import LEFT, RIGHT, TOP, BOTTOM

class KnotRectangle:
    """ Represents the pixel coordinates and dimension sizes of a Knot Widget """
    SIDE_TO_VAR_NAME = {LEFT: 'left',
                        RIGHT: 'right',
                        TOP: 'top',
                        BOTTOM: 'bottom'}
    
    def __init__(self, widget):
        """ Initialize with the widget to wrap """
        self.widget = widget
        
    @property
    def height(self):
        """ Return the widget's height """
        return self.widget._qwidget.height()
        
    @property
    def width(self):
        """ Return the widget's width """
        return self.widget._qwidget.width()
        
    @property
    def left(self):
        """ Return the widget's left x coordinate """
        return self.widget._qwidget.x()

    @left.setter
    def left(self, value):
        self.widget._qwidget.move(value, self.top)
        self.showChanges()
        
    @property
    def right(self):
        """ Return the widget's right x coordinate """
        return self.left + self.width

    @right.setter
    def right(self, value):
        self.widget._qwidget.move(value-self.width, self.top)
        self.showChanges()
        
    @property
    def top(self):
        """ Return the widget's top y coordinate """
        return self.widget._qwidget.y()

    @top.setter
    def top(self, value):
        self.widget._qwidget.move(self.left, value)
        self.showChanges()
        
    @property
    def bottom(self):
        """ Return the widget's bottom y coordinate """
        return self.widget._qwidget.y() + self.height

    @bottom.setter
    def bottom(self, value):
        self.widget._qwidget.move(value-self.height, self.top)
        self.showChanges()
        
    def getSidePosition(self, side):
        """ Return the pixel position of the given side """
        return getattr(self, self.SIDE_TO_VAR_NAME[side])
        
    def setSidePosition(self, side, value):
        """ Set the pixel position of the given side """
        setattr(self, self.SIDE_TO_VAR_NAME[side], value)
        
    def showChanges(self):
        """ Show changes to the underlying qwidget """
        if self.widget.isVisible:
            self.widget.show()
        