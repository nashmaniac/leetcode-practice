from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)-1

        for i in range(0, int(length/2)+1):
            for j in range(i, length-i):
                p1 = matrix[i][j]
                p2 = matrix[j][length-i]
                p3 = matrix[length-i][length-j]
                p4 = matrix[length-j][i]

                # print(p1, p2, p3, p4, end=' ')

                matrix[i][j] = p4
                matrix[j][length-i] = p1
                matrix[length-i][length-j] = p2
                matrix[length-j][i] = p3

                # print(matrix)


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

for i in matrix:
    print(i)

s = Solution().rotate(matrix)

for i in matrix:
    print(i)