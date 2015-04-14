from knot.core.mods.set_styling import SetStyling

class StyleToken:
    """ Represents a tokenized Style dictionary """
    
    def __init__(self, section, children):
        """ Initialize with the section for the style """
        attribute, self.styling = section[0].split(maxsplit=1)
        
    def build(self, config, scope):
        """ Build this type from the config """
        return SetStyling(self.styling)
        
    def __repr__(self):
        return "<StyleToken:{0}>".format(self.styling)