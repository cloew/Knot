from .mod_config import ModConfig
from .package_config import PackageConfig
from .policy_config import PolicyConfig
from .required_mod_config import RequiredModConfig
from .service_config import ServiceConfig
from .widget_config import WidgetConfig, WIDGET_TYPE

from .args.arg_factory import ModArgsConfigFactory

from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

reqModsParameters = [PrimitiveParameter("class")]
                     
ReqModsConfigFactory = Factory(RequiredModConfig, reqModsParameters)

widgetParameters = [PrimitiveParameter("name"),
                    PrimitiveParameter("type", optional=True, default=WIDGET_TYPE),
                    PrimitiveParameter("painter", optional=True),
                    PrimitiveParameter("template", optional=True),
                    PrimitiveParameter("controller", optional=True),
                    ComplexParameter("req-mods", ReqModsConfigFactory.loadAll, optional=True, default=[])]
                     
WidgetConfigFactory = Factory(WidgetConfig, widgetParameters)
WidgetConfigFactory.addParameter(ComplexParameter("childWidgets", WidgetConfigFactory.loadAll, optional=True, default=[]))

modParameters = [PrimitiveParameter("name"),
                 PrimitiveParameter("class"),
                 PrimitiveParameter("token", optional=True),
                 ComplexParameter("args", ModArgsConfigFactory.loadAll, optional=True, default=[])]
                     
ModConfigFactory = Factory(ModConfig, modParameters)

policyParameters = [PrimitiveParameter("name"),
                    PrimitiveParameter("class")]
                     
PolicyConfigFactory = Factory(PolicyConfig, policyParameters)
ServiceConfigFactory = Factory(ServiceConfig, policyParameters)

packageParameters = [ComplexParameter("widgets", WidgetConfigFactory.loadAll, optional=True, default=[]),
                     ComplexParameter("mods", ModConfigFactory.loadAll, optional=True, default=[]),
                     ComplexParameter("positioning", PolicyConfigFactory.loadAll, optional=True, default=[]),
                     ComplexParameter("sizing", PolicyConfigFactory.loadAll, optional=True, default=[]),
                     ComplexParameter("services", ServiceConfigFactory.loadAll, optional=True, default=[])]

PackageConfigFactory = Factory(PackageConfig, packageParameters)