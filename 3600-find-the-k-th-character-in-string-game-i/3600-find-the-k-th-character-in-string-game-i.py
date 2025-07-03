class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(97+(k-1).bit_count())
        