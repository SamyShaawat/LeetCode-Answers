class Solution(object):
    def countOfSubstrings(self, word: str, k: int) -> int:
        def isVowel(c):
            return c in {'a', 'e', 'i', 'o', 'u'}

        def atLeastK(word, k):
            n = len(word)
            ans = 0
            consonants = 0
            left = 0
            vowel_map = {}

            for right in range(n):
                if isVowel(word[right]):
                    vowel_map[word[right]] = vowel_map.get(word[right], 0) + 1
                else:
                    consonants += 1

                while len(vowel_map) == 5 and consonants >= k:
                    ans += n - right
                    if isVowel(word[left]):
                        vowel_map[word[left]] -= 1
                        if vowel_map[word[left]] == 0:
                            del vowel_map[word[left]]
                    else:
                        consonants -= 1
                    left += 1

            return ans

        return atLeastK(word, k) - atLeastK(word, k + 1)