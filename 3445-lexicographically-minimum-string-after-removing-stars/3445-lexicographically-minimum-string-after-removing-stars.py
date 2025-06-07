class Solution:
    def clearStars(self, s: str) -> str:
        d = defaultdict(list)
        for i, c in enumerate(s):
            if c == "*":
                mn = min(d)
                d[mn].pop()
                if not d[mn]:
                    del d[mn]
            else:
                d[c].append(i)
        ans = [(i, c) for c in d for i in d[c]]
        return "".join(c for i, c in sorted(ans))