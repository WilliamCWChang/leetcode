from typing import List


def test_leetcode():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution2().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution2().twoSum([3, 2, 4], 6) == [1, 2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = index
            else:
                return [h[n], index]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if num1+num2 == target and index1 != index2:
                    return [index1, index2]
