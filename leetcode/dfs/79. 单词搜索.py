# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

#  

# 示例:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# https://leetcode-cn.com/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/
class Solution:
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]

        # 遍历地图，对每一个点进行dfs
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, 0, board, word, visited):
                    return True
        return False

    def dfs(self, x, y, index, board, word, visited):
        # 递归终止条件
        if index == len(word)-1:
            return word[index] == board[x][y]
        
        # 如果匹配
        if word[index] == board[x][y]:
            # 设置占位
            visited[x][y] = True
            # 下一步递归
            for i in range(4):
                new_x = x + self.dir[i][0]
                new_y = y + self.dir[i][1]
                # 如果下一步合法
                if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]) and not visited[new_x][new_y]:
                    if self.dfs(new_x, new_y, index+1, board, word, visited):
                        # 后续递归成功
                        return True
            # 当前位置匹配，但是下一步及其后续不匹配
            # 撤销当前位置的占位
            visited[x][y] = False
        return False

