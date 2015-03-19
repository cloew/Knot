
class WidgetTypeParser:
    """ Returns the widget type from a Knot Scope Section """
    
    def find(self, section):
        """ FInd the widget type in the given section """
        firstLine = section[0]
        pieces = firstLine.split()
        if len(pieces) == 1:
            return pieces[0].strip()
        else:
            return 0