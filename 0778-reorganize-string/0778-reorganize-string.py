class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)
        n = len(s)

        if max(freq.values()) > (n + 1) // 2:
            return ""

        # Sort characters by frequency (most frequent first)
        chars = sorted(freq.items(), key=lambda x: -x[1])
        res = [''] * n
        i = 0

        for char, count in chars:
            for _ in range(count):
                res[i] = char
                i += 2
                if i >= n:
                    i = 1  # fill odd indices after even

        return ''.join(res)