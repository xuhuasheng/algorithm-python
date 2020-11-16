# 字符串的全排列
# 输入一个字符串,按字典序('0'<'9'<'A'<'Z'<'a'<'z')(从左往右比大小)
# 打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 输入描述:
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

def permutation(arr, start, end):
    # 所有都固定了，完成一种排列，输出
    if start == end:
        print(''.join(list(map(str, arr))))
        return
    for i in range(start, end+1):
        # 每一个数字都依次交换到第一个。并固定
        arr[start], arr[i] = arr[i], arr[start]
        # 固定第一个，解决子问题：后面的数字的全排列
        permutation(arr, start+1,end)
        # 完成一轮后，交换回来还原
        arr[start], arr[i] = arr[i], arr[start]

# 有重复的
def permutation1(str,start,end):

    if(start==end):
        for s in str:
            print(s,end='')
        print('')
        return

    for i in range(start,end+1):
        if not isrepeat(str,start,i):
            continue
        str[start],str[i]=str[i],str[start]
        permutation1(str,start+1,end)
        str[start], str[i] = str[i], str[start]

def isrepeat(str,start,i):
    bcan=True
    #第i个字符与第j个字符交换时，要求[i,j)中没有与第j个字符相等的数
    for j in range(start, i):
        if str[start]==str[i]:
            bcan=False
            break
    return bcan

import numpy as np
if __name__ == "__main__":
    ls = [1,2,3,4]
    ls2 = "abcd"
    ls2 = list(ls2)
    arr = sorted(ls2)
    permutation(arr, 0, len(arr)-1)