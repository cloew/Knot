from .knot_application import KnotApplication
from .service_provider import ServiceProvider
from .scope.has_scope import has_scope

from smart_defaults import smart_defaults

use_knot_services = smart_defaults
KnotService = ServiceProvider()