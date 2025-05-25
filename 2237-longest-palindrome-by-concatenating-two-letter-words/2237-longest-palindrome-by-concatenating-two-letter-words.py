class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        total_length = 0
        center_used = False

        for word, count in word_count.items():
            if word[0] == word[1]:
                # Use pairs like "aa", "bb", etc.
                pairs = count // 2
                total_length += pairs * 4
                if count % 2 == 1:
                    center_used = True
            else:
                reversed_word = word[::-1]
                if word < reversed_word:
                    pairs = min(count, word_count[reversed_word])
                    total_length += pairs * 4

        if center_used:
            total_length += 2

        return total_length