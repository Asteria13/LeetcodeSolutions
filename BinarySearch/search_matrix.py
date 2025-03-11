"""
搜索二维矩阵

给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
"""

def search_matrix(matrix, target):
    m, n = matrix.shape
    # 先确定target所在行

    up = 0
    down = m - 1
    while up <= down:
        mid = (up + down) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            up = mid + 1
        else:
            down = mid - 1

    x = up - 1
    l, r = 1, n - 1
    while l <= r:
        mid = (l + r) // 2
        if matrix[x][mid] == target:
            return True
        elif matrix[x][mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False
