from typing import List

import math


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        number_string = ''
        for index, i in enumerate(str):
            if i == '-' or i == '+':
                number_string += i
            elif i.isdigit():
                char = i
                j = index
                while char.isdigit():
                    number_string += char
                    j += 1
                    if not j < len(str):
                        break
                    char = str[j]
                number_string = number_string.strip()
                try:

                    if int(number_string)>int(math.pow(2, 31)-1):
                        return int(math.pow(2, 31)-1)
                    elif int(number_string) < -int(math.pow(2, 31)):
                        return -int(math.pow(2, 31))
                    else:
                        return int(number_string)
                except Exception as exc:
                    return 0
            else:
                return 0
        return 0


test_cases = [
    "+-2",
    # "-91283472332",
    # "words and 987",
    # "   -42",
    # "42"
]

for t in test_cases:
    s = Solution().myAtoi(t)
    print(t, s)
