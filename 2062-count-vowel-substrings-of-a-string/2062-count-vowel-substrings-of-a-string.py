class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        res = 0
        n = len(word)
        for left in range(n):
            for right in range(left + 1, n + 1):
                sub = word[left:right]
                if set(sub) == vowels:
                    res += 1
        return res
