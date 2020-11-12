"""Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

from typing import List

nums_ex1 = [1, 2, 3, 1]
nums_ex2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums_ex3 = [3, 3]
nums_ex4 = [3, 1]
nums_ex5 = [12]


def contains_duplicate_sol1(nums: List[int]) -> bool:
    """
    Very expensive solution for big list.

    In this case we move throw nums 2 times so complexity - O(n^2)
    :param nums:
    :return:
    """
    _len = len(nums)
    if _len <= 1:
        return False
    for i in range(0, _len):
        for j in range(0, _len):
            if i != j and nums[i] == nums[j]:
                return True

    return False


def contains_duplicate_sol2(nums: List[int]) -> bool:
    """
    Runtime: 112 ms
    Memory Usage: 18.9 MB

    :param nums:
    :return:
    """
    _len = len(nums)

    if _len <= 1:
        return False

    nums.sort()  # O(N Log N)
    for i in range(0, _len):
        if i < _len - 1 and nums[i] == nums[i + 1]:
            return True

    return False


if __name__ == '__main__':
    sol1 = contains_duplicate_sol1(nums_ex2)
    sol2 = contains_duplicate_sol2(nums_ex2)

