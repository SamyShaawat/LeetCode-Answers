from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}  
        
        for word in nums:
            freq[word] = freq.get(word,0)+1
        # print(freq)
        
        counter = Counter(freq)
        most_common = dict(counter.most_common(k))
        result = []
        for key in most_common:
            result.append(key)
        return result
        