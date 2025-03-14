"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。


思路，从左上角开始比较查找，复杂度O(m+n)
"""

class Solution:
    def search_matrix_II(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        x, y = 0, n - 1

        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1

        return False