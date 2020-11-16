# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

# 示例：

# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:

# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/range-sum-query-immutable
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# dp 空间换时间
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        if self.n == 0: return
        self.dp = [0] * self.n
        self.dp[0] = self.nums[0]
        for i in range(1, self.n):
            self.dp[i] = self.dp[i-1] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j]-self.dp[i] + self.nums[i]

# class NumArray {
# private:
#     int* sum;
# public:
#     NumArray(vector<int>& nums) {
#         //sum[i] 为 nums[0 : i-1]的和
#         sum = new int[nums.size() + 1];
#         sum[0] = 0;
#         for(int i = 1; i <= nums.size(); i++)
#             sum[i] = sum[i - 1] + nums[i - 1];
#     }
#     ~NumArray(){
#         delete[] sum;
#     }
#     int sumRange(int i, int j) {
#         return sum[j + 1] - sum[i];
#     }
# };