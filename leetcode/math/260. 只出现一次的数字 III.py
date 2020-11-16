# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

# 示例 :

# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
# 注意：

# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 1.全体异或
        tmp = 0
        for i in nums:
            tmp ^= i 
        # 2.异或结果的某一位差异
        pulse = 1
        while tmp & pulse == 0:
            pulse <<= 1
        # 3.按该位的不同 分拨
        p1 = []
        p2 = []
        for i in nums:
            if i & pulse:
                p1.append(i)
            else:
                p2.append(i)
        # 4.对这两拨分别进行异或
        ans1, ans2 = 0, 0
        for i in p1:
            ans1 ^= i 
        for i in p2:
            ans2 ^= i 
        return [ans1, ans2]