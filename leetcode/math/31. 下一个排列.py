# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        border = 0
        # 找到逆序区的边界
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                border = i
                break
        # 置换
        if border!=0:
            head = nums[border-1]
            for i in range(n-1, border-1, -1):
                if nums[i] > head:
                    nums[i], nums[border-1] = nums[border-1], nums[i]
                    break
        # 尾部翻转
        i = border
        j = n-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
