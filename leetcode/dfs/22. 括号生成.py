# // 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# //  

# // 示例：

# // 输入：n = 3
# // 输出：[
# //        "((()))",
# //        "(()())",
# //        "(())()",
# //        "()(())",
# //        "()()()"
# //      ]

# // 来源：力扣（LeetCode）
# // 链接：https://leetcode-cn.com/problems/generate-parentheses
# // 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# // 题解 https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/he-fa-kuo-hao-sheng-cheng
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #  记录所有合法的括号组合
        res = []
        # 回溯过程中的路径
        track = []
        # 可用的左括号数量为 left 个，可用的右括号数量为 rgiht 个
        # dfs 函数一定要定义在内部
        def dfs(left, right, track, res):
            # 若左括号剩下的多，说明不合法
            if right < left: return
            # 数量小于 0 肯定是不合法的
            if left < 0 or right < 0: return
            # 当所有括号都恰好用完时，得到一个合法的括号组合
            if left==0 and right==0:
                res.append(''.join(track))
                return
            # 尝试放一个左括号
            track.append('(') # 选择
            dfs(left-1, right, track, res)
            track.pop() # 撤消选择

            # 尝试放一个右括号
            track.append(')') # 选择
            dfs(left, right-1, track, res)
            track.pop() # 撤消选择

        dfs(n, n, track, res)
        return res
