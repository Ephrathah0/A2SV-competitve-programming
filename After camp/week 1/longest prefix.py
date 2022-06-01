class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = ""
        for i in range(len(first)):
            for s in strs:
                outOfBounds = (i == len(s))
                if outOfBounds or first[i] != s[i]:
                    return res
            res += first[i]
        return res
