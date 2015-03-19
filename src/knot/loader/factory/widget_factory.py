from .knot_config_factory import KnotConfigFactory

from knot.widget import Widget

from knot.core.painters.container_painter import ContainerPainter
from knot.core.painters.text_painter import TextPainter

widgets = {'div':{'painter':ContainerPainter},
           'text':{'painter':TextPainter}}

def BuildWidget(widgetType, content, positioning=None, sizing=None):
    """ Build the Widget based on its given type """
    widgetConfig = widgets[widgetType]
    painter = widgetConfig['painter'](content)
    if sizing is None and painter.DEFAULT_SIZING_CLS is not None:
        sizing = painter.DEFAULT_SIZING_CLS()
    return Widget(painter, positioning=positioning, sizing=sizing)
    
WidgetFactory = KnotConfigFactory(widgets, BuildWidget)