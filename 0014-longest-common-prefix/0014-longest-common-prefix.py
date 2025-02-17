class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i, char in enumerate(strs[0]):
            # print(i,char)
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return res
            res += char
        return res