
class PackageConfig:
    """ Represents the configuration for a knot package """
    
    def __init__(self, widgetConfigs, positioningConfigs, sizingConfigs):
        """ Initialize the widget config with its widgets, positioning policies and sizing policies """
        self.widgetConfigs = widgetConfigs
        self.positioningConfigs = positioningConfigs
        self.sizingConfigs = sizingConfigs