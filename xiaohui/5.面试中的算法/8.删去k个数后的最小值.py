# 题目：给出一个整数，从该整数中去掉k个数，
# 要求剩下的数字形成的新整数尽可能小

# 思路：每次删一个，从左往右，删除大于右面数字的那一位数
# 贪心算法：依次求局部最优解，最终得到全局最优解

# 时间复杂度o(n)
# 空间复杂度o(n)
def removeKDigits(num, k):
    # 使用栈保留暂存的数
    stack = Stack()
    for i in num:
        while (not stack.isEmpty()) and stack.peek() > i and k > 0:
            stack.pop() # 出栈 删除比右边大的数
            k -= 1      # 删除计数减一
        stack.push(i)   # 常规入栈
    # 依次出栈 转化为整数
    multi = 1
    res = 0
    while not stack.isEmpty():
        res += int(stack.pop()) * multi
        multi = multi * 10
    # 转化为字符串
    return str(res)

class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        return self.__list == []
    def push(self, data):
        return self.__list.append(data)
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    print(removeKDigits("541270936", 3))