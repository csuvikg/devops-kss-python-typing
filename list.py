from typing import List, Set


def sum(nums: List[int] | Set[int]) -> int:
    _sum = 0
    for i in nums:
        _sum += i
    return _sum


print(sum({1, 2, 3}))
