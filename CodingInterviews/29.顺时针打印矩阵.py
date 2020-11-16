# 题目：输入一个矩阵，安装从外到里顺时针的实现依次打印出每一个数字

import numpy as np
def printMatrixClockwisely(mat):
    mat = np.array(mat)
    rows, cols = mat.shape
    ridx_min = 0
    ridx_max = rows-1
    cidx_min = 0
    cidx_max = cols-1
    r = 0
    c = 0
    prtList = []
    # 大循环（一圈）和循环（四条边）都判断是否边界越界，且边界逐渐缩小
    while cidx_min <= cidx_max and ridx_min <= ridx_max:
        # 左上到右上
        if cidx_min <= cidx_max:
            for i in range(cidx_min, cidx_max+1):
                c = i
                prtList.append(mat[r,c])
            ridx_min += 1
        else:
            break
        # 右上到右下
        if ridx_min <= ridx_max:
            for i in range(ridx_min, ridx_max+1):
                r = i
                prtList.append(mat[r,c])
            cidx_max -= 1
        else:
            break
        # 右下到左下
        if cidx_min <= cidx_max:
            for i in range(cidx_max, cidx_min-1, -1):
                c = i
                prtList.append(mat[r,c])
            ridx_max -= 1
        else:
            break
        # 左下到左上
        if ridx_min <= ridx_max:
            for i in range(ridx_max, ridx_min-1, -1):
                r = i
                prtList.append(mat[r,c])
            cidx_min += 1
        else:
            break
    print(prtList)

# 递归 一圈一圈打印
def printMatrixClockwisely2(mat):
    if mat is None:
        return
    mat = np.array(mat)
    rows, cols = mat.shape
    if rows <= 0 or cols <= 0:
        return
    start = 0
    while cols > start *2 and rows > start *2:
        printCircle(mat, cols,rows,start)
        start += 1
    
def printCircle(mat, cols,rows,start):
    endx = cols-1-start
    endy = rows-1-start
    for i in range(start, endx+1):
        print(mat[start,i], end=",")
    if start < endy:
        for i in range(start+1, endx+1):
            print(mat[i,endx],end=",")
    if start < endx and start < endy:
        for i in range(endx-1, start-1, -1):
            print(mat[endy,i],end=",")
    if start < endx and start < endy-1:
        for i in range(endy-1, start, -1):
            print(mat[i,start],end=",")

class Solution:
    # matrix类型为二维列表，需要返回列表
    #知识点：完成信息的索引与去除，按照顺时针，每打印一圈的同时删除一圈，再进入下一层循环
    def printMatrix(self, matrix):
        # write code here
        list = []
        while matrix:
            list += (matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    list.append(row.pop())
            if matrix and matrix[0]:
                list += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    list.append(row.pop(0))
        return list

if __name__ == "__main__":
    arr = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
    printMatrixClockwisely(arr)
    printMatrixClockwisely2(arr)
