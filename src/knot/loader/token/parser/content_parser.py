
class ContentParser:
    """ Returns the content from a Knot Scope Section """
    
    def find(self, section):
        """ Find the content in the given section """
        return section[0].strip()