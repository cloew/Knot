from .arg_types import CONFIG, EXPRESSION, SCOPE, TEXT, TOKENS, VALUE, VALUE_LIST

from .config_arg import ConfigArg
from .expression_arg import ExpressionArg
from .scope_arg import ScopeArg
from .text_arg import TextArg
from .tokens_arg import TokensArg
from .value_arg import ValueArg
from .value_list_arg import ValueListArg

from kao_factory.factory import Factory
from kao_factory.typed_factory import TypedFactory

modArgFactories = {CONFIG:Factory(ConfigArg, []),
                   EXPRESSION:Factory(ExpressionArg, []),
                   SCOPE:Factory(ScopeArg, []),
                   TEXT:Factory(TextArg, []),
                   TOKENS:Factory(TokensArg, []),
                   VALUE:Factory(ValueArg, []),
                   VALUE_LIST:Factory(ValueListArg, [])}
                     
ModArgsConfigFactory = TypedFactory("type", modArgFactories)