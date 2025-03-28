class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
        
        # Create a list of tuples (query value, original index) and sort it
        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()
        
        # Min heap to store (value, row, column), starting from the top-left cell
        min_heap = [(grid[0][0], 0, 0)]
        
        # Set to keep track of visited cells
        visit = set([(0, 0)])
        
        # Result array to store the number of points for each query
        res = [0] * len(queries)
        
        points = 0  # Counter for the number of points collected
        
        # Process each query in increasing order
        for limit, index in q:
            # Expand the region while the smallest value in the heap is less than the query limit
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)  # Get the cell with the smallest value
                points += 1  # Increment the number of reachable points
                
                # Get the neighboring cells (down, up, right, left)
                neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                
                for nr, nc in neighbors:
                    # Check if the neighbor is within bounds and not visited yet
                    if (
                        0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in visit
                    ):
                        # Add the neighbor to the heap and mark it as visited
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visit.add((nr, nc))
            
            # Store the total number of points that can be reached for this query
            res[index] = points
        
        return res  # Return the results for all queries