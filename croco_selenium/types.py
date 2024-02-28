from typing import Union, NewType, Literal, Type, TypedDict, Any

XPATH = Union[NewType('XPATH', str), str]
MethodType = Literal['instance', 'static', 'class', 'function']
IgnoredExceptions = Union[Type[Exception], tuple[Type[Exception]]]
Cookies = Union[list[dict[str, Any]], dict[str, Any], str]


class Proxy(TypedDict):
    host: str
    port: int
    username: str
    password: str
