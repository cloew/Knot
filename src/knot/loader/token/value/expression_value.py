from .value_factory import ValueFactory
from knot.scope.scoped_expression import ScopedExpression

from kao_decorators import proxy_for

class ExpressionValue:
    """ Represents a Value that should be calculated from a Python expression """
    
    def __init__(self, valueText):
        """ Initialize the Expression Value Token """
        self.valueTokens = []
        self.text = ' '.join([self.handle(piece) for piece in valueText.strip().split()])
            
    def handle(self, piece):
        """ Handle the piece by storing the value token and return the proper placeholder string """
        text = piece
        valueToken = ValueFactory.buildScopeValue(piece)
        if valueToken is not None:
            self.valueTokens.append(valueToken)
            text = '{}'
        return text
        
    def getValue(self, scope):
        """ Return the actual value of the given token """
        return ScopedExpression(self.text, [token.getValue(scope) for token in self.valueTokens])