"""
颜色分类

给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。


三色旗问题，可以用单指针、双指针的方法做

"""





class Solution:

    def singlePointer(self, nums):
        """
            单指针解法：对数组进行两次遍历，第一次将所有的0移到最前面，第二次从0之后第一个下标开始，将1全部交换

            时间复杂度O(1)
        """
        n = len(nums)

        ptr = 0
        # 第一次遍历
        for i in range(n):
            if nums[i] == 0:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1

        for j in range(ptr, n):
            if nums[j] == 1:
                nums[ptr], nums[j] = nums[j], nums[ptr]
                ptr += 1

        return nums

    def doublePointerI(self, nums):
        """
        双指针解法II: 仅使用一次解法



        :param nums:
        :return:
        """

        n = len(nums)

        p0, p1 = 0, 0

        for i in range(n):
            # 如果找到1，将p1和i进行交换，并将p1向前移动一个位置
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1

            # 如果找到0，将p0和i位置的数交换；如果此时p0 < p1，还需要将交换后i上的数字和p1上的交换
            # p0, p1各向前移动一个位置
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:
                    nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1

        return nums

    def doublePointerII(self, nums):
        """
        双指标解法II
        和解法I类似，解法I用p0交换0, p1交换1,都是从前向后搜索排序
        解法II用p0交换0，用p2交换2，其中p2从后向前搜索
        :param nums:
        :return:
        """

        n = len(nums)
        p0 = 0
        p2 = n - 1
        i = 0

        while i <= p2:
            # 如果找到0, 将p0对应值交换，p0向后移动
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

            # 如果找到2, 将p2对应值交换，并且一直向前，直到i对应的数字不是0为止
            while nums[i] == 2 and i <= p2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            i += 1

        return nums

    def specialSolution(self, nums):
        """
        很非常规的解法，和排序没有半点关系，把nums中0, 1, 2的个数统计出来，再重新排列一遍
        :param nums:
        :return:
        """

        count0, count1, count2 = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            else:
                count2 += 2

        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0 + count1):
            nums[i] = 1
        for i in range(count0 + count1, len(nums)):
            nums[i] = 2

        return nums