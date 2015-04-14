from .config_helper import ConvertConfigsToDictionary

class PackageConfig:
    """ Represents the configuration for a knot package """
    
    def __init__(self, widgetConfigs, modConfigs, positioningConfigs, sizingConfigs, serviceConfigs):
        """ Initialize the widget config with its widgets, positioning policies and sizing policies """
        self.widgetConfigs = ConvertConfigsToDictionary(widgetConfigs)
        self.modConfigs = ConvertConfigsToDictionary(modConfigs)
        self.positioningConfigs = ConvertConfigsToDictionary(positioningConfigs)
        self.sizingConfigs = ConvertConfigsToDictionary(sizingConfigs)
        self.serviceConfigs = ConvertConfigsToDictionary(serviceConfigs)
        
    def setPackageFilename(self, filename):
        """ Set the package filename """
        self.filename = filename
        for name in self.widgetConfigs:
            self.widgetConfigs[name].setPackageFilename(filename)