class Solution:
    def robotWithString(self, s: str) -> str:
        s = list(s[::-1])
        t = []
        paper = []

        for c in sorted(set(s)):
            while t and t[-1] <= c:
                paper.append(t.pop())  

            while c in s:
                while s[-1] != c:
                    t.append(s.pop()) 

                paper.append(s.pop())  

        return "".join(paper)
        