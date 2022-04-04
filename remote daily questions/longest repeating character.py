class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum = 0
        ans = 0
        c = collections.Counter()

        for i in range(len(s)):
            c[s[i]] += 1
            maximum = max(maximum, c[s[i]])
            if ans - maximum < k:
                ans += 1
            else:
                c[s[i - ans]] -= 1

				
        return ans
