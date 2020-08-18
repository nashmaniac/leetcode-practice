import math


class Solution:
    def reverse(self, x: int) -> int:
        is_positive = True

        if x<0:
            is_positive = False
        string_representation = str(int(math.fabs(x)))
        reversed_string = ''
        for i in range(len(str(string_representation))-1, -1, -1):
            reversed_string += string_representation[i]
        if not is_positive:
            reversed_string = '-'+reversed_string

        if -math.pow(2, 31) <= int(reversed_string) <= math.pow(2, 31)-1:
            return int(reversed_string)
        else:
            return 0


s = Solution().reverse(-123)
print(s)
