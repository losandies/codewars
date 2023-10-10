import math


def remove_smallest(numbers):
    if numbers == []:
        return []

    minimum = min(numbers)
    nums = [x for x in numbers if numbers.index(x) != numbers.index(minimum)]
    print(nums)


remove_smallest([5, 1, 2, 1, 3, 4])
