# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#  

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if(not nums or n<3):
            return []

        # 排序-剪枝前提
        nums.sort()
        res=[]
        for i in range(n):
            # 大剪枝
            if(nums[i]>0):
                return res
            # 小剪枝
            if(i>0 and nums[i]==nums[i-1]):
                continue
            # 双指针
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    # 避免重复
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    # 更新指针
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, begin, target, track, res):
            # 一级条件：深度 若不满足则继续dfs
            if len(track) == 3:
                # 二级条件：和 如果满足条件则存储并返回上一层，如果不满足则返回上一层
                if target == 0:
                    res.append(track[:])
            else:
                for i in range(begin, len(nums)):
                    if target-nums[i] < 0: break
                    if i>begin and nums[i] == nums[i-1]: continue
                    track.append(nums[i])
                    dfs(nums, i+1, target-nums[i], track, res)
                    track.pop()

            track = []
            res = []
            nums.sort()
            dfs(nums, 0, 0, track, res)
            return res
