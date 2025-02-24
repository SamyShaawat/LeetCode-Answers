class Solution:
    def __init__(self):
        self.bob_path = {}
        self.visited = []
        self.tree = []

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        max_income = float("-inf")
        self.tree = [[] for _ in range(n)]
        self.bob_path = {}
        self.visited = [False] * n
        node_queue = deque([(0, 0, 0)])

        # Form tree with edges
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])

        # Find the path taken by Bob to reach node 0 and the times it takes to get there
        self.find_bob_path(bob, 0)

        # Breadth First Search
        self.visited = [False] * n
        while node_queue:
            source_node, time, income = node_queue.popleft()

            # Alice reaches the node first
            if (
                source_node not in self.bob_path
                or time < self.bob_path[source_node]
            ):
                income += amount[source_node]
            # Alice and Bob reach the node at the same time
            elif time == self.bob_path[source_node]:
                income += amount[source_node] // 2

            # Update max value if current node is a new leaf
            if len(self.tree[source_node]) == 1 and source_node != 0:
                max_income = max(max_income, income)

            # Explore adjacent unvisited vertices
            for adjacent_node in self.tree[source_node]:
                if not self.visited[adjacent_node]:
                    node_queue.append((adjacent_node, time + 1, income))

            # Mark and remove current node
            self.visited[source_node] = True

        return max_income

    # Depth First Search
    def find_bob_path(self, source_node, time):
        # Mark and set time node is reached
        self.bob_path[source_node] = time
        self.visited[source_node] = True

        # Destination for Bob is found
        if source_node == 0:
            return True

        # Traverse through unvisited nodes
        for adjacent_node in self.tree[source_node]:
            if not self.visited[adjacent_node]:
                if self.find_bob_path(adjacent_node, time + 1):
                    return True

        # If node 0 isn't reached, remove current node from path
        self.bob_path.pop(source_node, None)
        return False