"""
三数之和

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""


class Solution:

    # 暴力解， 会超时
    def brute_force(self, nums):
        res = []
        nums.sort()

        i = 0

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                        j -= 1

                if nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return res

    def threeSumV2(self, nums):
        res = []
        nums.sort()

        i = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = len(nums) - 1
            target = -nums[i]

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while j < k and nums[j] + nums[k] > target:
                    k -= 1

                if j == k:
                    break

                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])

        return res