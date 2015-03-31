from .package_config import PackageConfig
from .policy_config import PolicyConfig
from .widget_config import WidgetConfig

from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

widgetParameters = [PrimitiveParameter("name"),
                    PrimitiveParameter("painter"),
                    PrimitiveParameter("controller", optional=True)]
                     
WidgetConfigFactory = Factory(WidgetConfig, widgetParameters)

policyParameters = [PrimitiveParameter("name"),
                    PrimitiveParameter("class")]
                     
PolicyConfigFactory = Factory(PolicyConfig, policyParameters)

packageParameters = [ComplexParameter("widgets", WidgetConfigFactory.loadAll, optional=True, default=[]),
                     ComplexParameter("positioning", PolicyConfigFactory.loadAll, optional=True, default=[]),
                     ComplexParameter("sizing", PolicyConfigFactory.loadAll, optional=True, default=[])]

PackageConfigFactory = Factory(PackageConfig, packageParameters)