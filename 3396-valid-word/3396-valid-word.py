class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False 
        if n >= 3:
            if not word.isalnum():
                return False
            for char in word:
                if char.isalpha():
                    if char in vowels:
                        has_vowel = True
                    else:
                        has_consonant = True 
                
            return has_vowel and has_consonant


        else:
            return False