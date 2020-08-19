from typing import List


class Solution:
    def get_word(self, s: str) -> str:
        word_list = []
        for i in s:
            if i == '#':
                if word_list:
                    word_list.pop()
            else:
                word_list.append(i)

        st = ''
        for i in word_list:
            st += i
        return st

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.get_word(S) == self.get_word(T)


test_cases = [
    ["ab#c","ad#c"],
    ["ab##", "c#d#"],
    ["a##c", "#a#c"],
    ["a#c", "b"]
]

for t in test_cases:
    s = Solution().backspaceCompare(t[0], t[1])
    print(t, s)
