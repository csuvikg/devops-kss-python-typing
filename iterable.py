from typing import Iterable


class StringIter:
    def __init__(self, string):
        self._string = string

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i < len(self._string):
            x = self._string[self._i]
            self._i += 1
            return x
        else:
            raise StopIteration


test = StringIter('test')

for i in iter(test):
    print(i)

print(isinstance(test, Iterable))
