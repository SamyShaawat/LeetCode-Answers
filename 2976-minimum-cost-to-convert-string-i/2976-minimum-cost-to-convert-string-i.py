class Solution:
    def minimumCost(self, source: str, target: str, orig: List[str], chan: List[str], cost: List[int]) -> int:
        def idx(c): return ord(c) - ord('a')
        n,tochg = idx('z') +1, Counter([(s,t) for s,t in zip(source,target) if s!=t])
        floyd   = [[0 if j==i else inf for j in range(n)] for i in range(n)]
        for o,c,s in zip(orig,chan,cost):
            floyd[idx(o)][idx(c)] = min(s, floyd[idx(o)][idx(c)])
        for k,i,j in product(range(n),range(n),range(n)):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
        ans = sum(floyd[idx(s)][idx(t)]*tochg[(s,t)] for (s,t) in tochg.keys())
        return  ans  if  ans < 1e12  else -1
        