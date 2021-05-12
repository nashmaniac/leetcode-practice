from typing import List


class Solution:
    def coin_change(self, coins, targets):
        value_matrix = [
            [0 for i in range(0, targets + 1)] for x in range(0, len(coins))
        ]
        coins = sorted(coins)
        for i in range(1, len(coins)):
            value_matrix[i][0] = 1
        for i in range(0, targets + 1):
            value_matrix[0][i] = 1 if (i % coins[0] == 0) else 0

        print(value_matrix)

        for i in range(1, len(coins)):
            for j in range(1, targets + 1):
                if coins[i] > targets:
                    current_cost = value_matrix[i - 1][j]
                else:
                    current_cost = value_matrix[i - 1][j] + value_matrix[i-1][targets - coins[i]]

                value_matrix[i][j] = current_cost

        print('', end=' ')
        print(list(range(0, targets + 1)))
        print()
        for index, i in enumerate(value_matrix):
            print(coins[index], i)
        return value_matrix[len(coins) - 1][targets]


test_cases = [
    [[1, 3, 5], 5]
]

for t in test_cases:
    s = Solution().coin_change(t[0], t[1])
    print(t, s)
