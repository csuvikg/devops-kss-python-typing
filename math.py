Number = int | float | complex


class Math:
    _x: Number
    _y: Number

    def __init__(self, x: Number, y: Number) -> None:
        self._x: Number = x
        self._y: Number = y

    def add(self) -> Number:
        return self._x + self._y

    def multiply(self) -> Number:
        return self._x * self._y


m = Math(2, 3.14)
print(m.add())
print(m.multiply())
