
class PackageConfig:
    """ Represents the configuration for a knot package """
    
    def __init__(self, widgetConfigs, positioningConfigs, sizingConfigs, serviceConfigs):
        """ Initialize the widget config with its widgets, positioning policies and sizing policies """
        self.widgetConfigs = self.convertConfigsToDictionary(widgetConfigs)
        self.positioningConfigs = self.convertConfigsToDictionary(positioningConfigs)
        self.sizingConfigs = self.convertConfigsToDictionary(sizingConfigs)
        self.serviceConfigs = self.convertConfigsToDictionary(serviceConfigs)
        
    def setPackageFilename(self, filename):
        """ Set the package filename """
        self.filename = filename
        for name in self.widgetConfigs:
            self.widgetConfigs[name].setPackageFilename(filename)
        
    def convertConfigsToDictionary(self, configs):
        return {config.name:config for config in configs}