# 金矿问题
# w 工人数量
# n 可选金矿数量
# p[] 金矿所需的工人数
# g[] 金矿储量

# 1.问题边界（递归的终点）
# 2.最优子结构
# 3.状态转移方程

# 问题边界：F(n, w) = 0 if n == 0 or w == 0
# F(n, w) = F(n-1, w) if n>=1, w<当前金矿所需的人数  即w个人数不够挖不了n个金矿，只能挖n-1个
# F(n, w) = max(F(n-1, w), F(n-1, w-p[p-1]) + g[n-1])
# 当w人数够挖n个金矿时，有2种选择：1.依旧不挖当前的金矿，w个人还是挖前n-1个金矿F(n-1, w)
#                                2.挖当前的金矿g[n-1]，剩下的人挖n-1个金矿F(n-1, w-p[p-1])
#                               取两者最大值

# 动态规划 自顶向下(X)
# 时间复杂度o(2^n)
# 递归做了重复的计算
def getBestGoldingMining1(w, n, p:list, g:list):
    if w == 0 or n == 0:
        return 0
    if w < p[n-1]:
        return getBestGoldingMining(w, n-1, p, g)
    else:
        return max(getBestGoldingMining(w, n-1, p, g), 
                   getBestGoldingMining(w-p[n-1], n-1, p, g) + g[n-1])

# 动态规划 自底向上
# 时间复杂度o(n*w)
# 空间复杂度o(n*w)
import numpy as np
def getBestGoldingMining2(w, n, p:list, g:list):
    # 创建表格
    resTab = np.zeros(((len(g)+1), w+1), dtype=np.int)
    # 填二维表格
    for i in range(1, len(g)+1):
        for j in range(1, w+1):
            if j < p[i-1]:
                resTab[i, j] = resTab[i-1, j]
            else:
                resTab[i, j] = max(resTab[i-1, j], resTab[i-1, j-p[i-1]] + g[i-1])
    return resTab[len(g), w]

# 动态规划 自底向上
# 时间复杂度o(n*w)
# 空间复杂度o(w)
def getBestGoldingMining3(w, n, p:list, g:list):
    # 创建一维表格
    resArr = np.zeros(w+1, dtype=np.int)
    # 填充一维数组：第i行（新行）覆盖第i-1行（旧行）
    for i in range(1, len(length)):
        # 注意：从右往左 更新数据 为了保证计算时用到的旧数据没有被新数据覆盖
        for j in range(w, 0, -1):
            if j >= p[i-1]:
                resArr[j] = max(resArr[j], resArr[j-p[i-1]] + g[i-1])
    return reaArr[w]


if __name__ == "__main__":
    w = 10
    p = [5, 5, 3, 4, 3]
    g = [400, 500, 200, 300, 350]
    print(getBestGoldingMining1(w, len(g), p, g))