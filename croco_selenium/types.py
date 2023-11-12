from typing import Union, NewType, Literal, Type, TypedDict

XPATH = Union[NewType('XPATH', str), str]
MethodType = Literal['object', 'static', 'class']
IgnoredExceptions = Union[Type[Exception], tuple[Type[Exception]]]


class Proxy(TypedDict):
    host: str
    port: int
    username: str
    password: str
