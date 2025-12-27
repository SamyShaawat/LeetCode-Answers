class Solution:
    def bestClosingTime(self, customers: str) -> int:
        bestTime = 0
        minPenalty = 0
        prefix = 0
        
        for i in range(len(customers)):
            prefix += -1 if customers[i] == 'Y' else 1
            
            if prefix < minPenalty:
                bestTime = i + 1
                minPenalty = prefix
        
        return bestTime