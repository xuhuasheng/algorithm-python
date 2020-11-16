# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode-cn.com/problems/subsets-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-19/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, begin, track, res):
            res.append(track[:])
            for i in range(begin, len(nums)):
                # 剪枝
                if i>begin and nums[i-1] == nums[i] :
                    continue
                track.append(nums[i])
                dfs(nums, i+1, track, res)
                track.pop()
        
        res = []
        track = []
        # 剪枝前提 排序
        nums.sort()
        dfs(nums, 0, track, res)
        return res