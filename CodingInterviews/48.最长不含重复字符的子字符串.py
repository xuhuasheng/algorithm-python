# 请从字符串中找出一个最长的不包含重复字符的子字符串，
# 计算该最长子字符串的长度。假设字符串中只包含’a’~'z’的字符。
# 例如，在字符串"arabcacfr"中，最长的不含重复字符的子字符串就是"acfr"，长度为4。

# https://blog.csdn.net/mabozi08/article/details/88933697
# 思路：用动态规划来做。首先定义f(i)表示以第i个字符结尾的不包含重复字符的子字符串的最长长度。

# 如果第i个字符之前没有出现过，那么f(i)=f（i-1)+1。

# 如果第i个字符之前出现过，讲该字符与上次出现的字符串中的位置的距离记为d，分两种情况：

#     d<=f(i-1)，说明第i个字符之前出现的字符在当前子字符串内，则f(i)=d

#     d>f(i-1），说明之前出现的字符在当前子字符串外，f(i)=f(i-1)+1

# 时间复杂度o(n)
# 空间复杂度o(1)=o(26)
def longestSubstringWithoutDuplication(s:str):
    cnt = 0
    maxcnt = 0
    position = {}
    for i in range(len(s)):
        # 如果从未出现过
        if s[i] not in position:
            cnt += 1
        # 出现过
        else:
            # 两次出现的距离
            d = i - position[s[i]]
            if d > cnt:
                # 没关系，继续加一
                cnt += 1
            else:
                # 从头计数
                cnt = d
        # 记录字母出现的位置
        position[s[i]] = i
        # 更新最大的
        if cnt > maxcnt:
            maxcnt  = cnt  
    return maxcnt

if __name__ == "__main__":
    print(longestSubstringWithoutDuplication("pwwkew"))


# class Solution {
# public:
#     int lengthOfLongestSubstring(string s) {
#         int n = s.size();
#         if (n==0) return 0;
#         int cnt = 0;
#         int ans = 0;
#         unordered_map<char, int> log;
#         for (int i=0; i<s.size(); i++) {
#             if (log.find(s[i]) == log.end()) {
#                 cnt += 1;
#                 log.insert(pair<char, int> (s[i], i));
#                 //log.insert({s[i], i});
#             } else {
#                 int d = i - log[s[i]];
#                 if (d > cnt)
#                     cnt += 1;
#                 else
#                     cnt = d;
#             }
#             log[s[i]] = i;
#             ans = max(ans, cnt);
#         }
#         return ans;

#     }
# };
    
