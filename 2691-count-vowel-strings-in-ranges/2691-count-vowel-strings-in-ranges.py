class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * (n + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            prefix[i + 1] = prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] += 1

        res = []
        for q in queries:
            res.append(prefix[q[1] + 1] - prefix[q[0]])

        return res