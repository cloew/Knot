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
        self.widget._qwidget.show()
        
    @property
    def right(self):
        """ Return the widget's right x coordinate """
        return self.left + self.width

    @right.setter
    def right(self, value):
        self.widget._qwidget.move(value-self.width, self.top)
        self.widget._qwidget.show()
        
    @property
    def top(self):
        """ Return the widget's top y coordinate """
        return self.widget._qwidget.y()

    @top.setter
    def top(self, value):
        self.widget._qwidget.move(self.left, value)
        self.widget._qwidget.show()
        
    @property
    def bottom(self):
        """ Return the widget's bottom y coordinate """
        return self.widget._qwidget.y() + self.height

    @bottom.setter
    def bottom(self, value):
        self.widget._qwidget.move(value-self.height, self.top)
        self.widget._qwidget.show()
        
    def getSidePosition(self, side):
        """ Return the pixel position of the given side """
        return getattr(self, self.SIDE_TO_VAR_NAME[side])
        # if side is LEFT:
            # return self.left
        # elif side is RIGHT:
            # return self.right
        # elif side is TOP:
            # return self.top
        # elif side is BOTTOM:
            # return self.bottom
        
    def setSidePosition(self, side, value):
        """ Set the pixel position of the given side """
        setattr(self, self.SIDE_TO_VAR_NAME[side], value)
        # if side is LEFT:
            # self.left = value
        # elif side is RIGHT:
            # self.right = value
        # elif side is TOP:
            # self.top = value
        # elif side is BOTTOM:
            # self.bottom = value