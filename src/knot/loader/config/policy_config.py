
class PolicyConfig:
    """ Represents the configuration for a policy """
    
    def __init__(self, name, policyClassname):
        """ Initialize the polict config with its name and the policy classname """
        self.name = name
        self.policyClassname = policyClassname
        
    def __repr__(self):
        """ Return the string representation of the config """
        return "<PolicyConfig({0}, {1})>".format(self.name, self.policyClassname)