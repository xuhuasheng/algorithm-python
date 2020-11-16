# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置。

def firstNotRepeatingChar(s):
    dic = {}
    # 出现次数保存至字典hash表
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    # 从头遍历，字典第一个次数为1的输出
    for i in range(len(s)):
        if dic[s[i]] == 1:
            return s[i]
    return -1

if __name__ == "__main__":
    s="abaccdeff"
    print(firstNotRepeatingChar(s))