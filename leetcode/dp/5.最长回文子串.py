# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

# // 来源：力扣（LeetCode）
# // 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# // 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# dp
# 时间复杂度:o(n2)
# 空间复杂度：O(n2)
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False]*n for _ in range(n)]

    max_len = 1
    start = 0
    # 对角线初始化
    for i in range(n):
        dp[i][i] = True

    # 按列填从上到下
    for j in range(1, n):
        for i in range(0, j):
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False

            if dp[i][j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start = i
    return s[start:start + max_len]

# 时间复杂度：O(N^2)
# 空间复杂度：O(1)，只使用到常数个临时变量，与字符串长度无关。 
def longestPalindrome(s: str) -> str:
    size = len(s)
    if size < 2:
        return s

    # 至少是 1
    max_len = 1
    res = s[0]

    for i in range(1, size-1):
        palindrome_odd, odd_len = center_spread(s, size, i, i)
        palindrome_even, even_len = center_spread(s, size, i, i + 1)

        # 当前找到的最长回文子串
        cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
        if len(cur_max_sub) > max_len:
            max_len = len(cur_max_sub)
            res = cur_max_sub

    return res

def center_spread(s, size, left, right):
    """
    left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
    right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
    """
    i = left
    j = right

    while i >= 0 and j < size and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1:j], j - i - 1



