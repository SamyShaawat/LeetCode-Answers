class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_map = Counter(answers)
        total_rabbits = 0

        for answer, freq in count_map.items():
            group_size = answer + 1  # each group can have up to (answer + 1) rabbits
            groups_needed = math.ceil(freq / group_size)
            total_rabbits += groups_needed * group_size

        return total_rabbits