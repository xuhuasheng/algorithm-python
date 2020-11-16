# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

#  

# 例如，给定三角形：

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

#  

# 说明：

# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# dp 注意三角形两边界
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [0] * (m)
        dp[0] = triangle[0][0]
        for i in range(1, m):
            # 注意要从右往左覆盖，保证无后效性
            for j in range(i, -1, -1):
                if j == i:
                    dp[j] = triangle[i][j] + dp[j-1]
                elif j == 0:
                    dp[j] = triangle[i][j] + dp[j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
        return min(dp)

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i+1):
                if j==0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
        return min(dp[-1])