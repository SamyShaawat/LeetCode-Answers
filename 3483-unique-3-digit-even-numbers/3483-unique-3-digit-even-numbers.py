class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        un = set()
        for perm in permutations(digits,3):
            if perm[0] != 0 and perm[2] %2 == 0:
                number =perm[0] * 100  + perm[1] * 10 + perm[2]
                un.add(number)
        return len(un)