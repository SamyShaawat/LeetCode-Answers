class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        seen = [False] * n
        def bfs(node):
            q = deque()
            seen[node] = True
            q.append(node)
            current_compontent = []
            while len(q)>0:
                current = q.popleft()
                current_compontent.append(current)
                for v in adj_list[current]:
                    if not seen[v]:
                        seen[v] = True 
                        q.append(v)
            for c in combinations(current_compontent, 2):
                u,v =c
                if v not in adj_list[u]:
                    return False
            return True 
        count = 0
        for i in range(n):
            if not seen[i]:
                if bfs(i): 
                    count +=1
        return count 
