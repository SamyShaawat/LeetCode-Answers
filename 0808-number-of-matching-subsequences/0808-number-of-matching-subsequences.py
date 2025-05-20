class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word: str) -> bool:
            # index to track the position in s where we last found a matched character
            current_position = -1
            for char in word:
                # find the character in s starting from the next position after current_position
                current_position = s.find(char, current_position + 1)
                if current_position == -1:
                    # char not found in s after current_position, so word is not a subsequence
                    return False
            return True

        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1

        return count
