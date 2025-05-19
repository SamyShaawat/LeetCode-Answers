class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        subseq_end = defaultdict(int)

        for num in nums:
            if not freq[num]:
                continue

            if subseq_end[num - 1]:
                subseq_end[num - 1] -= 1
                subseq_end[num] += 1
            elif freq[num + 1] and freq[num + 2]:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                subseq_end[num + 2] += 1
            else:
                return False

            freq[num] -= 1

        return True
