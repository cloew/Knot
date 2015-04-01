
def GetScopeFor(widget, currentScope=None):
    """ Return the scope for the given widget or the current scope """
    if hasattr(widget, 'controller') and hasattr(widget.controller, 'HasKnotScope') and widget.controller.HasKnotScope:
        return widget.controller
    else:
        return currentScope