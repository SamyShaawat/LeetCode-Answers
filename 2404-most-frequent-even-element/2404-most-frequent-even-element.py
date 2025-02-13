class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        most_frequency = []
        for num in nums:
            if num % 2 == 0: 
                hashmap[num] += 1
        if (not hashmap):
            return -1
        max_value = max(hashmap.values())
        for key, value in hashmap.items():
            if value == max_value:
                most_frequency.append(key)

        return min(most_frequency)
        