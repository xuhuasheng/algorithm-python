# 大数相加：存进数组，对应位相加
def bigNumberSum(bigNum1:str, bigNum2:str):
    maxLength = len(bigNum1) if len(bigNum1) > len(bigNum2) else len(bigNum2)
    numArr1 = [0] * (maxLength+1)
    numArr2 = [0] * (maxLength+1)
    index = 0
    # 反向存入，便于后续从左往右遍历相加
    for i in range(len(bigNum1)-1, -1, -1):
        numArr1[index] = int(bigNum1[i])
        index += 1
    index = 0
    for i in range(len(bigNum2)-1, -1, -1):
        numArr2[index] = int(bigNum2[i])
        index += 1
    # 从左往右遍历 从低位开始对应位相加
    resArr = [0] * (maxLength+1)
    for i in range(len(resArr)):
        temp = numArr1[i] + numArr2[i] + resArr[i]
        # 进位
        if temp > 9:
            temp = temp - 10
            resArr[i+1] = 1
        resArr[i] = temp
    resStr = ""
    firstZeros = True
    for i in range(len(resArr)-1, -1, -1):
        if firstZeros:
            if resArr[i] == 0:
                continue
            firstZeros = False
        resStr += str(resArr[i])
    return resStr

if __name__ == "__main__":
    print(bigNumberSum("785541566842", "7859815668942"))