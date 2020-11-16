# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

# 示例:

# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：

# X X X X
# X X X X
# X X X X
# X O X X
# 解释:

# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/surrounded-regions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 反向操作，找边界点‘O’ 并dfs置换为‘#’，再全局遍历替换'O'->'X', '#'->''O。
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y, board):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == 'X' or board[x][y] == '#':
                return
            board[x][y] = '#'
            for i in dir:
                new_x = x + i[0]
                new_y = y + i[1]
                dfs(new_x, new_y, board)
        
        if board == []:
            return None

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                isEdge = (i==0 or j==0 or i==m-1 or j==n-1)
                if isEdge and board[i][j] == 'O':
                    dfs(i, j, board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'