from collections import defaultdict, deque
from itertools import combinations
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list to represent the graph
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)  # Since the graph is undirected

        # Track visited nodes
        seen = [False] * n

        def bfs(node):
            """Performs BFS to find connected components and checks if they are complete."""
            q = deque()
            seen[node] = True  # Mark the starting node as visited
            q.append(node)
            current_compontent = []  # Stores all nodes in the current connected component

            # Standard BFS loop
            while len(q) > 0:
                current = q.popleft()  # Dequeue a node
                current_compontent.append(current)  # Add it to the component list
                for v in adj_list[current]:  # Explore its neighbors
                    if not seen[v]:
                        seen[v] = True  # Mark as visited
                        q.append(v)  # Enqueue for further exploration
            
            # Check if the component forms a complete subgraph (clique)
            for c in combinations(current_compontent, 2):  # Generate all pairs of nodes in the component
                u, v = c
                if v not in adj_list[u]:  # If any pair is not connected, it's not a complete component
                    return False
            return True  # If all pairs are connected, it's a complete component

        count = 0  # Stores the count of complete components
        for i in range(n):  # Iterate over all nodes
            if not seen[i]:  # If the node is not visited, it starts a new component
                if bfs(i):  # Check if the component is complete
                    count += 1  # Increment count if it's a complete component

        return count  # Return the number of complete components
