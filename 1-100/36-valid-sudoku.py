from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        data = dict()
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                number = board[i][j]
                if number != '.':
                    row_template = '{} in row {}'.format(number, i)
                    column_template = '{} in column {}'.format(number, j)
                    box_template = '{} in box ({}, {})'.format(number, int(i/3), int(j/3))

                    if row_template not in data:
                        data.update(**{
                            row_template: 1
                        })
                    else:
                        return False

                    if column_template not in data:
                        data.update(**{
                            column_template: 1
                        })
                    else:
                        return False

                    if box_template not in data:
                        data.update(**{
                            box_template: 1
                        })
                    else:
                        return False
        return True


test_cases = [
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ],
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
]

for t in test_cases:
    s = Solution().isValidSudoku(t)
    print(t, s)