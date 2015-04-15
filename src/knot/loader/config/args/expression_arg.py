from knot.loader.token.value.expression_value import ExpressionValue

class ExpressionArg:
    """ Represents an argument that is a Python Expression """
    REQUIRES_TEXT = True
        
    def build(self, piece, section, children, config, scope):
        """ Return the scoped expression """
        return ExpressionValue(piece).getValue(scope)