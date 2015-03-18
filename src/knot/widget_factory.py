from .widget import Widget

from .core.painters.container_painter import ContainerPainter
from .core.painters.text_painter import TextPainter

widgets = {'div':{'painter':ContainerPainter},
           'text':{'painter':TextPainter}}


def BuildWidget(widgetType, content, sizing=None):
    """ Build the Widget based on its given type """
    widgetConfig = widgets[widgetType]
    painter = widgetConfig['painter'](content)
    if sizing is None and painter.DEFAULT_SIZING_CLS is not None:
        sizing = painter.DEFAULT_SIZING_CLS()
    return Widget(painter, sizing=sizing)
    
def HasWidgetType(widgetType):
    """ Return if the factory can build this Widget Type """
    return widgetType in widgets