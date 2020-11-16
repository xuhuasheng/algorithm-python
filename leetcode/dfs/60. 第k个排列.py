# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。

# 说明：

# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:

# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:

# 输入: n = 4, k = 9
# 输出: "2314"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutation-sequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(nums, depth, size, track, used, res):
            if depth == size:
                res.append(track[:])
                return

            for i in range(len(nums)):
                # // 防止重复
                if not used[i]:
                    # 做选择 入栈搜索
                    track.append(nums[i])
                    used[i] = True
                    # 进行dfs 此时深度+1
                    dfs(nums, depth+1, size, track, used, res)
                    # 撤销选择 弹栈 恢复 回溯
                    track.pop()
                    used[i] = False

        nums = list(range(1, n+1))
        res = []        # 结果数组
        track = []      # 深度搜索的栈
        used = [False for _ in range(len(nums))]    # 访问痕迹
        
        dfs(nums, 0, len(nums), track, used, res)
        return ''.join(list(map(str, res[k-1])))


# https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n, k, depth, track):
            if depth == n:
                return
            cnt = factorial[n - 1 - depth]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                track.append(i)
                used[i] = True
                dfs(n, k, depth + 1, track)
                # 注意：这里要加 return，后面的数没有必要遍历去尝试了
                return

        if n == 0:
            return ""

        used = [False for _ in range(n + 1)]
        track = []
        # 阶乘查表
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        dfs(n, k, 0, track)
        return ''.join([str(num) for num in track])
