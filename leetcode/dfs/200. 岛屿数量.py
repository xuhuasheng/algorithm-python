# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

#  

# 示例 1:

# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
# 示例 2:

# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y, grid, visited):
            visited[x][y] = True
            for i in dir:
                new_x = x + i[0]
                new_y = y + i[1]
                if 0 <= new_x < len(grid) and 0 <= new_y <len(grid[0]):
                    if not visited[new_x][new_y] and grid[new_x][new_y] == '1':
                        dfs(new_x, new_y, grid, visited)

        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        visited = [ [False for j in range(n)] for i in range(m)]
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j, grid, visited)
        return cnt