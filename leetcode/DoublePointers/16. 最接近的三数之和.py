# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

#  

# 示例：

# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        # 排序
        nums.sort()
        for i in range(n):
            # 双指针
            left = i+1
            right = n-1
            while left < right:
                # 更新res
                sum = nums[i] + nums[left] + nums[right]
                if abs(target-sum) < abs(target-res):
                    res = sum
                # 更新指针
                if (sum < target):
                    left += 1
                elif sum > target:
                    right -=1
                else:
                    return res  # sum == target
        return res