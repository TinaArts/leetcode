"""Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element
appears only once and returns the new length.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]

"""

from typing import List

nums_ex1 = [1, 1, 2]
nums_ex2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def remove_duplicates_sol1(nums: List[int]) -> List[int]:
    """
    Memory expensive solution solution.
    Runtime: 5012 ms
    Memory Usage: 15.6 MB

    In this case we move throw new_nums 3 times so complexity can be O(n^3)
    :param nums:
    :return:
    """
    new_nums = list(nums)
    for key, val in enumerate(new_nums):  # O(n)
        if nums.count(val) > 1:  # O(n)
            nums.remove(val)  # O(n)

    return nums


def remove_duplicates_sol2(nums: List[int]) -> List[int]:
    """
    Runtime: 788 ms
    Memory Usage: 15.6 MB

    :param nums:
    :return:
    """
    new_nums = list(nums)
    len_new_nums = len(new_nums) - 1
    _next = None

    for key, num in enumerate(new_nums):
        if key < len_new_nums:
            _next = new_nums[key + 1]
        else:
            _next = None

        if num == _next:
            nums.remove(num)

    return nums


def remove_duplicates_sol3(nums: List[int]) -> List[int]:
    """
    Runtime: 88 ms
    Memory Usage: 15.7 MB

    :param nums:
    :return:
    """

    i = 0
    uniq_val = None

    while i < len(nums):
        if i == 0:
            uniq_val = nums[i]
        else:
            if nums[i] == uniq_val:
                del nums[i]
                i -= 1
            else:
                uniq_val = nums[i]
        i += 1

    return nums


def remove_duplicates_sol_from_leetcode(nums: List[int]) -> int:
    """
    The best solution from leetcode

    Runtime: 76 ms
    Memory Usage: 15.7 MB
    :param nums:
    :return:
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    return j + 1


if __name__ == '__main__':
    sol1 = remove_duplicates_sol1(nums_ex2)
    sol2 = remove_duplicates_sol2(nums_ex2)
    sol3 = remove_duplicates_sol3(nums_ex2)

