# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, depth, size, track, used, res):
            # dfs终止条件 搜到底了，保存栈结果
            if depth == size:
                # 这里要注意！！list append的是引用，是同一个地址（指向同一个内存空间）
                # 需要用track[:]返回一个深拷贝的副本，再append到res上，否则全是[]
                res.append(track[:])
                return
            # 从选择列表中 遍历选择
            for i in range(len(nums)):
                # // 防止重复
                if not used[i]:
                    # 做选择 入栈搜索
                    track.append(nums[i])
                    used[i] = True
                    # 进行dfs 此时深度+1
                    dfs(nums, depth+1, size, track, used, res)
                    # 撤销选择 弹栈 恢复 回溯
                    track.pop()
                    used[i] = False

        res = []        # 结果数组
        track = []      # 深度搜索的栈
        used = [False for _ in range(len(nums))]    # 访问痕迹
                
        dfs(nums, 0, len(nums), track, used, res)
        return res