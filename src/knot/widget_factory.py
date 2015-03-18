from .widget import Widget

from .core.painters.container_painter import ContainerPainter
from .core.painters.text_painter import TextPainter

widgets = {'div':{'painter':ContainerPainter},
           'text':{'painter':TextPainter}}


def BuildWidget(widgetType, content, sizing=None):
    """ Build the Widget based on its given type """
    widgetConfig = widgets[widgetType]
    painter = widgetConfig['painter'](content)
    return Widget(painter, sizing=sizing)