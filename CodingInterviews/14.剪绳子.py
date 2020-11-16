# 给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），
# 每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

# 动态规划
# 1.求一个问题的最优解
# 2.整体问题的最优解依赖各个子问题的最优解
# 3.子问题存在相互重叠的更小的子问题
# 4.自上而下地分析，自底向上的求解，把子问题的最优解存储下来

# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(4) = f(1) * f(3)
#         f(2) * f(2)
#         f(3) * f(1)
# f(5) = f(1) * f(4)
#       f(2) * f(3)
#       f(3) * f(3)
#       f(4) * f(1)
def cutting(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    fn = [0] * (length+1)
    fn[0] = 0
    fn[1] = 1
    fn[2] = 2
    fn[3] = 3
    for i in range(4, length+1):
        max = 0
        for j in range(1, i//2+1):
            temp = fn[j] * fn[i-j]
            if max < temp:
                max = temp
            fn[i] = max
    return fn[length]

if __name__ == "__main__":
    print(cutting(8))

