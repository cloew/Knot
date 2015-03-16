from .widget import Widget

from .core.painters.left_to_right_painter import LeftToRightPainter
from .core.painters.text_painter import TextPainter

widgets = {'div':{'painter':LeftToRightPainter},
           'text':{'painter':TextPainter}}


def BuildWidget(widgetType, content):
    """ Build the Widget based on its given type """
    widgetConfig = widgets[widgetType]
    painter = widgetConfig['painter'](content)
    return Widget(painter)