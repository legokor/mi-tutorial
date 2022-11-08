from typing import Optional, Union


def f(x: int, y: Union[float, int], z: Optional[str] = None) -> float:
    return x * y * 3
