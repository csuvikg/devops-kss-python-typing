from typing import Iterable
from iterable import StringIter

# def print_iterable(iterable):
#     for i in iterable:
#         print(i)


def print_iterable(iterable: Iterable) -> None:
    for i in iterable:
        print(i)


print_iterable([0, 1, 2])

print_iterable(StringIter('test'))
print_iterable('test')
