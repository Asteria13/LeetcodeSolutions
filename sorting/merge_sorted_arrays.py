"""
合并两个有序数组

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n
"""


class Solution:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.n = len(nums2)
        self.m = self.n - len(nums1)

    def merge(self):
        ptr = self.m + self.n - 1
        ptr1 = self.m - 1
        ptr2 = self.n - 1

        while ptr >= 0 and ptr2 >= 0:
            if ptr1 < 0:
                self.nums1[ptr] = self.nums2[ptr2]
                ptr2 -= 1

            else:
                if self.nums1[ptr1] > self.nums2[ptr2]:
                    self.nums1[ptr] = self.nums1[ptr1]
                    ptr1 -= 1
                else:
                    self.nums1[ptr] = self.nums2[ptr2]
                    ptr2 -= 1

            ptr -= 1

        return self.nums1