"""Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""

from typing import List

nums_ex1 = [1, 2, 3, 4, 5, 6, 7]
k_ex1 = 3
nums_ex2 = [-1, -100, 3, 99]
k_ex2 = 2


def rotate_sol1(nums: List[int], k: int) -> None:
    """
    Runtime: 60 ms
    Memory Usage: 15.5 MB

    :param nums:
    :param k:
    :return:
    """
    left_k = len(nums) - k
    left_part = nums[:left_k]
    del nums[:left_k]
    nums.extend(left_part)


def rotate_sol2(nums: List[int], k: int) -> None:
    """
    Runtime: 124 ms
    Memory Usage: 15.3 MB

    :param nums:
    :param k:
    :return:
    """
    i = 0
    while k > i:
        nums.insert(0, nums[-1])
        del nums[-1]
        i += 1


if __name__ == '__main__':
    rotate_sol1(nums_ex1, k_ex1)
    rotate_sol2(nums_ex1, k_ex1)
