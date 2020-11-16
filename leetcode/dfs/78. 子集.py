# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode-cn.com/problems/subsets/solution/hui-su-si-xiang-tuan-mie-pai-lie-zu-he-zi-ji-wen-t/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, begin, track, res):
            # 不管什么情况都保存到res
            res.append(track[:])
            for i in range(begin, len(nums)):
                # 做选择
                track.append(nums[i])
                # 回溯
                dfs(nums, i+1, track, res)
                # 撤销选择
                track.pop()

        res = []
        track = []
        dfs(nums, 0, track, res)
        return res