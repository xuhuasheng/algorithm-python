# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。

# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

# 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
# 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

# 在任何情况下，若函数不能进行有效的转换时，请返回 0 。

# 提示：

# 本题中的空白字符只包括空格字符 ' ' 。
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
#  

# 示例 1:

# 输入: "42"
# 输出: 42
# 示例 2:

# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 示例 3:

# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 示例 4:

# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
# 示例 5:

# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
#      因此返回 INT_MIN (−231) 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-to-integer-atoi
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 法1
# 直接遍历法
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        res = 0
        i = 0
        positive = True
        # 1.跳过前面的空格
        while s[i] == ' ':
            i += 1
        # 2.判断正负号
        if s[i] == '-':
            positive = False
        if s[i] == '+' or s[i] == '-':
            i += 1
        # 3.读取有效数字
        while i < len(s) and s[i].isdigit():
            r = int(s[i])
            # 判断是否正数溢出，INT_MAX逆运算，INT_MIN也适用
            if (res > INT_MAX//10) or (res == INT_MAX//10 and r>7):
                return INT_MAX if positive else INT_MIN
            # 数字推入：左移历史数据 + 当前数字
            res = res * 10 + r
            i += 1
        return res if positive else -res

# 法2
# https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/
# 自动机
# 确定有限状态机（deterministic finite automaton, DFA）
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        # 初始状态
        self.state = 'start'
        # 有限状态机的表
        self.table = {
            #            ' '        '+/-'    'digit'      'other'
            'start':     ['start', 'signed', 'in_number', 'end'],
            'signed':    ['end',   'end',    'in_number', 'end'],
            'in_number': ['end',   'end',    'in_number', 'end'],
            'end':       ['end',   'end',    'end',       'end'],
        }
        # 有限状态机维护的数据
        self.sign = 1
        self.ans = 0
        
    def condition_idx(self, c):
        # 根据条件返回对应列索引
        if c.isspace():
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c):
        # 更新状态 <- 当前状态 和 当前条件
        self.state = self.table[self.state][self.condition_idx(c)]
        # 根据最新状态，维护数据
        if self.state == 'in_number':
            # 推入数字
            self.ans = self.ans * 10 + int(c)
            # 溢出处理
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

