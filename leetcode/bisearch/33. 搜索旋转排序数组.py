# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:

# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:

# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0: return -1
        if n == 1: return 0 if nums[0]==target else -1
        left = 0
        right = n-1
        # 确定有序区，根据是否在有序区or无序区， 二分查找更新区间
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            # 如果mid左侧为有序区
            if nums[0] <= nums[mid]:
                # 是否在有序区
                if nums[0] <= target < nums[mid]:
                    right = mid-1
                # 否则在另一边
                else:
                    left = mid + 1
            # 同理
            else:
                if nums[mid] < target <= nums[n-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1