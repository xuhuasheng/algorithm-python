# 给定一个未排序的整数数组，找出最长连续序列的长度。

# 要求算法的时间复杂度为 O(n)。

# 示例:

# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Time: O(n) Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set去重
        st = set(nums)
        maxLen = 0
        # 遍历set
        for num in st:
            # 如果不和前面的连续
            if num-1 not in st:
                curLen = 1
                # 一直查看是否跟后面的连续
                while (num+1) in st:
                    num += 1
                    curLen += 1
                # 维护max值
                maxLen = max(maxLen, curLen)
        return maxLen