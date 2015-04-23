from .widget_builder import WidgetBuilder
from .passthrough_widget_builder import PassthroughWidgetBuilder
from .semantic_widget_builder import SemanticWidgetBuilder

WIDGET_TYPE = "widget"
PASSTHROUGH_TYPE = "passthrough"
SEMANTIC_TYPE = "semantic"

TypeToBuilder = {WIDGET_TYPE:WidgetBuilder,
                 PASSTHROUGH_TYPE:PassthroughWidgetBuilder,
                 SEMANTIC_TYPE:SemanticWidgetBuilder}

def getBuilder(type, name, painterClassname):
    """ Return a builder for the given type """
    return TypeToBuilder[type](name, painterClassname=painterClassname)