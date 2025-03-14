"""
长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""

"""
思路：
i) 二分查找，时间复杂度O(nlogn)
另外创建一个数组 sums 记录数组nums前i个元素的和，因为nums元素非负，所以sums是一个单调增的数列，确定了使用二分查找的可能性

ii) 滑动窗口, 时间复杂度O(n)


"""

import bisect


class Solution:

    def __init__(self, nums, target, method):
        self.nums = nums
        self.target = target
        self.method = method
        self.length = len(nums)

    def binary_search(self):
        sums = [0]
        cur_length = self.length + 1

        for i in range(self.length):
            sums.append(sums[-1] + self.nums[i])

        for i in range(1, self.length + 1):
            s = self.target + sums[i - 1]
            bound = bisect.bisect_left(sums, s)
            if bound != len(sums):
                cur_length = min(cur_length, bound - (i - 1))

        return 0 if cur_length == self.length + 1 else cur_length

    def slide_window(self):
        if sum(self.nums) < self.target:
            return 0

        cur_length = self.length + 1

        start = 0
        end = 0
        cur_value = 0

        while end < self.length:
            cur_value += self.nums[end]
            while cur_value >= self.target:
                cur_length = min(cur_length, end - start + 1)
                cur_value -= self.nums[start]
                start += 1
            end += 1

        return cur_length
