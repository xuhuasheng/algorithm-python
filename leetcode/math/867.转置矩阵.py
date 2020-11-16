# 给定一个矩阵 A， 返回 A 的转置矩阵。
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#  
# 示例 1：

# 输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
# 示例 2：

# 输入：[[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/transpose-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        T = [[0 for j in range(m)] for i in range(n)]
        for i in range(m):
            for j in range(n):
                T[j][i] = A[i][j]
        return T

# class Solution {
# public:
#     vector<vector<int>> transpose(vector<vector<int>>& A) {
#         int m = A.size();
#         int n = A[0].size();
#         vector<vector<int>> T(n, vector<int>(m));
#         for (int i=0; i<m; ++i) {
#             for (int j=0; j<n; ++j) {
#                 T[j][i] = A[i][j];
#             }
#         }
#         return T;
#     }
# };