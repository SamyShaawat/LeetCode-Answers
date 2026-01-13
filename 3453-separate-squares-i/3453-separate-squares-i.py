class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def area_above(h):
            """Computes the total area of squares above y = h."""
            total_area = 0
            for x, y, l in squares:
                if y + l > h:  # If part of the square is above
                    height_above = (y + l) - max(y, h)
                    total_area += height_above * l  # Width is always l
            return total_area
        
        # Find min and max y-ranges
        min_y = min(y for _, y, _ in squares)
        max_y = max(y + l for _, y, l in squares)

        # Binary search for balanced y
        left, right = min_y, max_y
        epsilon = 1e-5

        while right - left > epsilon:
            mid = (left + right) / 2
            area_above_mid = area_above(mid)
            total_area = area_above(min_y)  # Total area of all squares
            area_below_mid = total_area - area_above_mid
            
            if area_above_mid > area_below_mid:
                left = mid  # Move up
            else:
                right = mid  # Move down

        return round(left, 5)