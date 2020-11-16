# 给定一个无序的整数数组，找到其中最长上升子序列的长度。

# 示例:

# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:

# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 时间复杂度O(n2)
# 动态规划：
# 定义dp[n]：表示以nums[n]这个数结尾的最长递增子序列的长度
# 递推公式：dp[i] = max(dp[j]+1)， for j in range(i) and nums[i] > nums[j]
# 初始值：dp[0] = 1
# 最终问题解：max(dp) dp缓存数组里的最大值即为最长上升子序列的长度
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# 时间复杂度：o(nlogn)
# https://blog.csdn.net/qq_41765114/article/details/88415541
# 定义dp[n]：dp[i] 表示长度为 i 的最长递增子序列（LIS）末尾的数
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [0] * len(nums)
        tail = 0
        for num in nums:
            left, right = 0, tail
            # 二分法
            # 搜索区间 [left, right)
            while left < right:
                m = (left + right) // 2
                # 找比num大的最小的元素并替换
                if dp[m] == num:
                    right = m
                elif dp[m] < num: 
                    left = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                elif dp[m] > num: 
                    right = m
            dp[left] = num
            if left == tail: 
                tail += 1
        return tail

import bisect
def lis(nums):
    dp = []
    for i in range(len(nums)):
        idx = bisect.bisect_left(dp, nums[i])
        if idx == len(dp):
            dp.append(nums[i])
        else:
            dp[idx] = nums[i]
    return len(dp)

