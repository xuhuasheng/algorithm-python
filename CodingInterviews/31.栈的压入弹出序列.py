# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

# 规律：如果下一个弹出的数字刚好是栈顶数字，那么直接弹出。
# 如果下一个弹出的数字不在栈顶，则把压栈序列中还没有入栈的数值压入辅助站，直到把下一个需要弹出的数字压入栈顶为止。
# 如果所有数字都压入栈，仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列。


# 用辅助栈模拟整个流程
def isPopOrder(pushList, popList):
    if len(pushList) != len(popList):
        return False
    stack = Stack()
    pushIdx = 0
    # 遍历取值popList
    for i in range(len(popList)):
        # 弹出的数字 
        num = popList[i]    
        # 如果栈是空的(第一次) 或者 弹出的数字 不在栈顶 
        if stack.isEmpty() or stack.peek() != num:
            exisitFlag = False
            # 向后面找 弹出的数字num 
            while pushIdx <= len(pushList)-1:
                # 在找到之前都入栈
                if pushList[pushIdx] != num:
                    stack.push(pushList[pushIdx])
                    pushIdx += 1
                # 找到了，先入栈再出栈
                else:
                    exisitFlag = True
                    stack.push(pushList[pushIdx])
                    stack.pop()
                    pushIdx += 1
                    break  
            # 找完了 没找到
            if exisitFlag is False:
                return False
        # 栈非空 且 num等于栈顶 则出栈
        else:
            stack.pop()
    # 遍历一遍下来没有提前return False
    return True

class Stack:
    def __init__(self):
        self.__list = []
    def isEmpty(self):
        return self.__list == []
    def push(self, data):
        self.__list.append(data)
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.__list.pop()
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.__list[-1]

if __name__ == "__main__":
    pushList = [1,2,3,4,5]
    popList1 = [4,5,3,2,1]
    popList2 = [4,3,5,1,2]
    print(isPopOrder(pushList, popList2))