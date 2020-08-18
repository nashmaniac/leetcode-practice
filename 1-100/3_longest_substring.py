class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters_seen = []
        max_count = 0
        count = 0
        for i in s:
            if i not in characters_seen:
                count += 1
                characters_seen.append(i)
            else:
                count = 1
                characters_seen = [i]
            if count > max_count:
                max_count = count
        return max_count


s = Solution().lengthOfLongestSubstring("dvdf")
print(s)