from kao_fn import FunctionMetadata

def HasBindingAt(obj, argName):
    """ Return if the obj has a binding at the given name """
    return hasattr(obj.__class__, argName) and hasattr(GetBindingAt(obj, argName), "applyKnotBinding")

def GetBindingAt(obj, argName):
    """ Return the binding """
    return getattr(obj.__class__, argName)
    
def apply_knot_bindings(fn):
    """ Apply the required processings for the knot bindings """
    metadata = FunctionMetadata(fn)
    
    def applyBinding(*args, **kwargs):
        self = args[0]
        argToBinding = {arg:GetBindingAt(self, arg.argName) for arg in metadata.args if HasBindingAt(self, arg.argName)}
        for arg in argToBinding:
            argToBinding[arg].applyKnotBinding(self, arg.getValue(args, kwargs))
        
        return fn(*args, **kwargs)
    return applyBinding