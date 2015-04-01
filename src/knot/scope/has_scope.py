
def has_scope(cls):
    """ Add the property to the constructor class that speciifes it should act as the scope current scope """
    cls.HasKnotScope = True
    return cls