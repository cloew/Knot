from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from kao_factory.Source.json_source import JsonSource

from kao_resources import ResourceDirectory

from functools import partial
from smart_defaults import smart_defaults, EvenIfNone

class KnotAppConfig:
    """ Represents the configuration for a knot application """
    
    @classmethod
    def load(cls, filename):
        """ Load the Knot App Config from the given file """
        global configParameters
        config = partial(cls, filename)
        source = JsonSource(filename)
        data = source.data
        return Factory(config, configParameters).load(data)
    
    @smart_defaults
    def __init__(self, baseDirectory, knotFilename, rootDirectory=None, title=EvenIfNone("Knot Application")):
        """ Initialize the Knot App Config """
        self.rootDirectory = self.getRootDirectory(baseDirectory, rootDirectory)
        self.knotFilename = self.rootDirectory.getProperPath(knotFilename) if knotFilename is not None else None
        self.title = title
        
    def getRootDirectory(self, baseDirectory, rootDirectory):
        """ Return the Root Directory for the application """
        configResourceDir = ResourceDirectory(baseDirectory)
        if rootDirectory is None:
            return configResourceDir
        else:
            return ResourceDirectory(configResourceDir.getProperPath(rootDirectory))
                    
configParameters = [PrimitiveParameter("knotFilename"),
                    PrimitiveParameter("rootDirectory", optional=True),
                    PrimitiveParameter("title", optional=True)]