class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqMap = defaultdict(int)
        for c in word:
            freqMap[c] += 1
        
        frequencies = sorted(freqMap.values())
        minDeletions = float('inf')
        n = len(frequencies)
        
        for i in range(n):
            base = frequencies[i]
            totalDeletions = 0
            
            for j in range(i):
                totalDeletions += frequencies[j]
            
            for j in range(i, n):
                if frequencies[j] > base + k:
                    totalDeletions += frequencies[j] - (base + k)
            
            if totalDeletions < minDeletions:
                minDeletions = totalDeletions
        
        return minDeletions