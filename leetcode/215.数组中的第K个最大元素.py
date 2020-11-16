# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr, start, end):
            pivot = arr[start]
            mark = start
            for i in range(start+1, end+1):
                if arr[i] < pivot:
                    mark += 1
                    arr[i], arr[mark] = arr[mark], arr[i]
            arr[mark], arr[start] = arr[start], arr[mark]
            return mark

        start = 0
        end = len(nums)-1
        idx = partition(nums, start, end)
        while idx != (len(nums)+1-k) - 1:
            if idx > (len(nums)+1-k) - 1:
                end = idx-1
                idx = partition(nums, start, end)
            else:
                start = idx + 1
                idx = partition(nums, start, end)
        return nums[idx]

# class Solution {
# public:
#     int findKthLargest(vector<int>& nums, int k) {
#         int start = 0;
#         int end = nums.size()-1;
#         int idx = partition(nums, start, end);
#         while (idx != nums.size()-k) {
#             if (idx < nums.size()-k)
#                 start = idx + 1;
#             else
#                 end = idx - 1;
#             idx = partition(nums, start, end);
#         }
#         return nums[idx];
#     }
#     int partition(vector<int>& nums, int start, int end) {
#         int pivot = nums[start];
#         int mark = start;
#         for (int i=start+1; i<=end; ++i) {
#             if (nums[i] < pivot) {
#                 mark ++;
#                 int temp = nums[i];
#                 nums[i] = nums[mark];
#                 nums[mark] = temp;
#             }
#         }
#         nums[start] = nums[mark];
#         nums[mark] = pivot;
#         return mark;
#     }
# };