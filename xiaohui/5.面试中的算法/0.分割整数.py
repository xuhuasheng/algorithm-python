def splitNum(num):
    digtList = []
    temp = num
    digtNum = 0
    # 计算位数
    while temp > 0:
        temp = temp // 
        digtNum += 1
    # 从高分位到低分为
    temp = num
    div = 10**(digtNum-1)
    while temp > 0:
        digt = temp // div
        digtList.append(digt)
        temp = temp % div
        div = div // 10
    # 从低分位到高分位
    # digtList_reverse = []
    # temp = num
    # while temp > 0:
    #     lowDigt = temp % 10
    #     temp = temp // 10
    #     digtList_reverse.append(lowDigt)
    return digtList

def splitNum2(num):
    s = str(num)
    slist = list(s)
    return list(map(int, slist))


def getNum(arr):
    Num = 0
    multi = 1
    for i in range(len(arr)-1, -1, -1):
        Num += arr[i] * multi
        multi = multi * 10
    return Num

        

def getNum2(arr):
    Num = 0
    for i in arr:
        Num = 10*Num + i
    return Num

    
if __name__ == "__main__":
    arr = splitNum(330)
    num = getNum(arr)
    print(arr)
    print(num)