
class ScopedExpression:
    """ Represents a Python expression to execute in a given scope """
    
    def __init__(self, expression, values):
        """ Initialize with the template and values """
        self.expression = expression.format(*[self.getVarName(i) for i, value in enumerate(values)])
        self.values = values
        
    def get(self):
        """ Return the current value """
        return eval(self.expression, {"__builtins__":None}, {self.getVarName(i):value.get() for i, value in enumerate(self.values)})
        
    def getVarName(self, index):
        """ Return the var name for the given index """
        return "arg{0}".format(index)