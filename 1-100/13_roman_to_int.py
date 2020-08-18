class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000
        )
        p = 0
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if value_map[s[i]] >= p:
                ans += value_map[s[i]]
            else:
                ans -= value_map[s[i]]
            p = value_map[s[i]]
        return ans



test_cases = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV', 'DCXXI']
for t in test_cases:
    s = Solution().romanToInt(t)
    print(t, s)
