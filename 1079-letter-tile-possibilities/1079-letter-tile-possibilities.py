class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        hashmap = Counter(tiles)  # Count the occurrences of each tile
        
        def backTrack():
            res = 0  # Store the number of unique sequences formed
            
            for key in hashmap:  # Iterate through all unique tiles
                if hashmap[key] > 0:  # Check if the tile is available for use
                    hashmap[key] -= 1  # Use the tile (decrease its count)
                    res += 1  # Count this new sequence
                    res += backTrack()  # Explore further sequences using recursion
                    hashmap[key] += 1  # Restore the tile count (backtracking)
            
            return res  # Return the total count of sequences
        
        return backTrack()  # Start the recursive function
            
        