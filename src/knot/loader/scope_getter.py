from knot.scope.knot_scope import KnotScope

def GetScopeFor(widget, currentScope=None):
    """ Return the scope for the given widget or the current scope """
    if widget is not None and hasattr(widget, 'controller') and hasattr(widget.controller, 'HasKnotScope') and widget.controller.HasKnotScope:
        return KnotScope(widget.controller)
    else:
        return currentScope