# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

# 示例 1:

# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:

# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:

# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/powx-n
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 时间复杂度：O(logn)，即为递归的层数。
# 空间复杂度：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 时间复杂度：O(logn)，即为对 nn 进行二进制拆分的时间复杂度。
# 空间复杂度：O(1)。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: 
            return 0.0
        if n < 0: 
            x, n = 1 / x, -n
        res = 1
        while n:
            if n & 1: 
                res *= x
            x *= x
            n >>= 1
        return res

