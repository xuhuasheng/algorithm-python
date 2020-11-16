# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

# 不占用额外内存空间能否做到？

#  

# 示例 1:

# 给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:

# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 

# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-matrix-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            matrix[i].reverse()
        return matrix

# class Solution {
# public:
#     void rotate(vector<vector<int>>& matrix) {
#         int m = matrix.size();
#         int n = matrix[0].size();
#         for (int i=0; i<m; ++i) {
#             for (int j=i+1; j<n; ++j) {
#                 int temp = matrix[i][j];
#                 matrix[i][j] = matrix[j][i];
#                 matrix[j][i] = temp;
#             }
#         }
#         for (int i=0; i<m; ++i) {
#             int left = 0;
#             int right = n-1;
#             while (left < right) {
#                 int temp = matrix[i][left];
#                 matrix[i][left] = matrix[i][right];
#                 matrix[i][right] = temp;
#                 left++;
#                 right--;
#             }
#         }
#     }
# };


        
        