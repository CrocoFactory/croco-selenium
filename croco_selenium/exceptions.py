from typing import Any


class InvalidMethodType(TypeError):
    """Raised when a provided method type is not represented as Literal['object', 'static', 'class']"""

    def __init__(self, value: Any):
        super().__init__(f"Method type is not represented as Literal['object', 'static', 'class']. Provided value is "
                         f"{value}")
