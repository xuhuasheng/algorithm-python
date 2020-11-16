# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true
# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 法1：字符串解法
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        strList = list(str(x))
        strList_ = list(reversed(strList))  # reversed返回的是逆序的迭代器，需要用list转化
        return strList == strList_
        
        # return str(x) == str(x)[::-1]

# 法2：数学解法，求翻转数
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        num = x
        rev = 0
        while num:
            rev = rev * 10 + num % 10
            num = num // 10
        return num == rev

solve = Solution()
ans = solve.isPalindrome(121)
print(ans)