from .widget import Widget
from .core.painters.text_painter import TextPainter

widgets = {'text':{'painter':TextPainter}}


def BuildWidget(widgetType, content):
    """ Build the Widget based on its given type """
    widgetConfig = widgets[widgetType]
    painter = widgetConfig['painter'](content)
    return Widget(painter)