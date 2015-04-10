from .controller_value import ControllerValue
from .global_value import GlobalValue
from .percent_value import PercentValue
from .pixel_value import PixelValue
from .scope_value import ScopeValue
from .string_value import StringValue

class ValueFactory:
    """ Factory to construct the proper Value Object for a given text """
    VALUE_CLASSES = [ControllerValue, GlobalValue, PercentValue, PixelValue, ScopeValue, StringValue]
    SCOPE_VALUE_CLASSES = [ControllerValue, ScopeValue]
    
    def build(self, valueText):
        """ Build the value object for the given text """
        for cls in self.VALUE_CLASSES:
            if cls.isValidFor(valueText):
                return cls(valueText)
        else:
            return None
    
    def buildScopeValues(self, valueText):
        """ Build the value object's only from the scope """
        for cls in self.SCOPE_VALUE_CLASSES:
            if cls.isValidFor(valueText):
                return cls(valueText)
        else:
            return None
            
ValueFactory = ValueFactory()