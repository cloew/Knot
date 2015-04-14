from knot.loader.token.value.value_factory import ValueFactory

class ValueArg:
    """ Represents an argument that is a scoped value """
    REQUIRES_TEXT = True
        
    def build(self, piece, section, children, config, scope):
        """ Return the scope value """
        return ValueFactory.buildScopeValue(piece).getValue(scope)