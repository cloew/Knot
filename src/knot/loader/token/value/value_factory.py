from .global_value import GlobalValue

class ValueFactory:
    """ Factory to construct the proper Value Object for a given text """
    VALUE_CLASSES = [GlobalValue]
    
    def build(self, valueText):
        """ Build the value object for the given text """
        for cls in self.VALUE_CLASSES:
            if cls.isValidFor(valueText):
                return cls(valueText)
        else:
            return None
            
ValueFactory = ValueFactory()