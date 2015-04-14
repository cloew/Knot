from knot.loader.token.knot_list_parser import KnotListParser
from knot.loader.token.value.value_factory import ValueFactory

class ValueListArg:
    """ Represents an argument that is a list of scoped values """
    REQUIRES_TEXT = True
        
    def build(self, piece, section, children, config, scope):
        """ Return the scope values """
        return [ValueFactory.buildScopeValue(valueText).getValue(scope) for valueText in KnotListParser().parse(piece)]