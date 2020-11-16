# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

# 请你实现这个将字符串进行指定行数变换的函数：

# string convert(string s, int numRows);
# 示例 1:

# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:

# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:

# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# 可以理解为在一个以行为单位的list里做来回的字母累积
# LDR
# EOEII
# ECIHN
# TSG

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 按行来回累积再拼接
# time:  o(n)
# space: o(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 特例
        if numRows == 1:
            return s
        rowList = ["" for _ in range(numRows)]
        curRow = 0
        goingDown = False
        for c in s:
            rowList[curRow] += c 
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow -= 1
        return "".join(rowList)

# 暴力填二维矩阵
# time:  o(n2)
# space: o(n2)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # 确定行列
        n = len(s)
        nSingle = 2*numRows-2
        if n % nSingle <= numRows:
            numCols = (numRows-1) * (n//nSingle) + 1
        else:
            numCols = (numRows-1) * (n//nSingle) + 1 + (n%nSingle-numRows)
        # 定义存储矩阵
        arr = [[-1 for j in range(numCols)] for i in range(numRows)]
        # 填表
        curRow, curCol = 0, 0
        for i, c in enumerate(s):
            N = (i+1) // nSingle
            M = (i+1) % nSingle 
            if M == 0:
                curCol = N * (numRows-1) - 1
                curRow = 1
            elif 1 <= M <= numRows:
                curCol = N * (numRows-1)
                curRow = M - 1
            elif M > numRows:
                curCol = N * (numRows-1) + (M-numRows)
                curRow = numRows - (M-numRows) - 1
            arr[curRow][curCol] = c
        # 输出
        res = ""
        for i in range(numRows):
            for j in range(numCols):
                if arr[i][j] != -1:
                    res += (arr[i][j])
        return res
