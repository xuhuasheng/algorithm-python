# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：

# 答案中不可以包含重复的四元组。

# 示例：

# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/4sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 此题用dfs超时
# 考虑双指针
class Solution:
    def fourSum(self, nums, target: int):
        def dfs(nums, begin, target, track, res):
            if len(track) == 4:
                if target == 0:
                    res.append(track[:])
                    return
            else:
                for i in range(begin, len(nums)):
                    # 大剪枝
                    if target >=0 and target - nums[i] < 0: 
                        break
                    # 小剪枝
                    if i>begin and nums[i] == nums[i-1]:
                        continue
                    track.append(nums[i])
                    dfs(nums, i+1, target-nums[i], track, res)
                    track.pop()
        # 排序
        nums.sort()
        track = []
        res = []
        dfs(nums, 0, target, track, res)
        return res

nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
s = Solution()
res = s.fourSum(nums, target)
print(res)

# 双指针
# 时间复杂度：O(n^3)，排序的时间复杂度是 O(nlogn)，枚举四元组的时间复杂度是 O(n^3)
# 因此总时间复杂度为 O(n^3+nlogn)
# 空间复杂度：O(logn)，空间复杂度主要取决于排序额外使用的空间。
# 此外排序修改了输入数组 nums，实际情况中不一定允许，
# 因此也可以看成使用了一个额外的数组存储了数组 nums 的副本并排序，空间复杂度为 O(n)。

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        if n<4: return res
        # 排序-前提
        nums.sort()
        # 外循环
        for a in range(0, n-4+1):
            if a>0 and nums[a] == nums[a-1]: continue   #确保nums[a] 改变了
            # 内循环
            for b in range(a+1, n-3+1):
                if b>a+1 and nums[b] == nums[b-1]: continue #确保nums[b] 改变了
                c = b+1
                d = n-1
                # 双指针
                while c < d:
                    if nums[a]+nums[b]+nums[c]+nums[d] == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c<d and nums[c] == nums[c+1]: c += 1  #确保nums[c] 改变了
                        while c<d and nums[d] == nums[d-1]: d -= 1  #确保nums[d] 改变了
                        c += 1
                        d -= 1
                    elif nums[a]+nums[b]+nums[c]+nums[d] < target:
                        c += 1
                    elif nums[a]+nums[b]+nums[c]+nums[d] > target:
                        d -= 1
        return res