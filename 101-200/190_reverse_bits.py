class Solution:
    def reverseBits(self, n: int) -> int:
        string_rep = str(n)
        rev_string = ''
        for i in range(len(string_rep)-1, -1, -1):
            rev_string += string_rep[i]
        return int(rev_string)


s = Solution().reverseBits(1)
print(s)