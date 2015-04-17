from knot.sides import LEFT, RIGHT, TOP, BOTTOM

def qwidget_dimension(fn):
    """ Decorate a fn so that it is only called when the underlying qwidget exists """
    def checkQWidget(self):
        if self.widget._qwidget is None:
            return 0
        else:
            return fn(self)
    return checkQWidget

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
    @qwidget_dimension
    def height(self):
        """ Return the widget's height """
        return self.widget._qwidget.height()
        
    @property
    @qwidget_dimension
    def width(self):
        """ Return the widget's width """
        return self.widget._qwidget.width()
        
    @property
    @qwidget_dimension
    def left(self):
        """ Return the widget's left x coordinate """
        return self.widget._qwidget.x()

    @left.setter
    def left(self, value):
        if self.widget.canMove():
            self.widget._qwidget.move(value, self.top)
            self.showChanges()
        
    @property
    def right(self):
        """ Return the widget's right x coordinate """
        return self.left + self.width

    @right.setter
    def right(self, value):
        self.left = value-self.width
        
    @property
    @qwidget_dimension
    def top(self):
        """ Return the widget's top y coordinate """
        return self.widget._qwidget.y()

    @top.setter
    def top(self, value):
        if self.widget.canMove():
            self.widget._qwidget.move(self.left, value)
            self.showChanges()
        
    @property
    def bottom(self):
        """ Return the widget's bottom y coordinate """
        return self.top + self.height

    @bottom.setter
    def bottom(self, value):
        self.top = value-self.height
        
    def getSidePosition(self, side):
        """ Return the pixel position of the given side """
        return getattr(self, self.SIDE_TO_VAR_NAME[side])
        
    def setSidePosition(self, side, value):
        """ Set the pixel position of the given side """
        setattr(self, self.SIDE_TO_VAR_NAME[side], value)
        
    def showChanges(self):
        """ Show changes to the underlying qwidget """
        if self.widget.visible:
            self.widget.show()