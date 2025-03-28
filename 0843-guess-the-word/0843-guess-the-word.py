# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        while words:
            # Randomly select a word to guess
            selected_word = random.choice(words)
            
            # Get how many characters matched
            matches = master.guess(selected_word)
            
            # If all characters match, we break
            if matches == len(selected_word):
                break
            
            # Filter words with the same number of matches
            words = [word for word in words if sum(a == b for a, b in zip(word, selected_word)) == matches]

        