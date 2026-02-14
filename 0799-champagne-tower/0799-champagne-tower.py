class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We start with all the liquid in the single glass at the top (row 0)
        currentRow = [float(poured)]
        
        for r in range(query_row + 1):
            # The next row always has one more glass than the current row
            nextRow = [0.0] * (r + 2)
            anyOverflow = False

            for c in range(r + 1):
                # If the glass has more than 1 unit, it overflows
                if currentRow[c] > 1.0:
                    excess = currentRow[c] - 1.0
                    splitFlow = excess / 2.0
                    
                    nextRow[c] += splitFlow
                    nextRow[c + 1] += splitFlow
                    
                    currentRow[c] = 1.0  # The glass remains full
                    anyOverflow = True
            
            # Optimization: If no glass in this row overflowed,
            # rows below will stay empty.
            if not anyOverflow and r < query_row:
                return currentRow[query_glass] if r == query_row else 0.0

            if r != query_row:
                currentRow = nextRow
        
        return currentRow[query_glass]