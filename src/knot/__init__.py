from .knot_application import KnotApplication
from .service_provider import ServiceProvider

from .events.signal import Signal
from .scope.apply_bindings import apply_knot_bindings
from .scope.has_scope import has_scope
from .scope.two_way_binding import TwoWayBinding

from smart_defaults import smart_defaults

use_knot_services = smart_defaults
KnotService = ServiceProvider()