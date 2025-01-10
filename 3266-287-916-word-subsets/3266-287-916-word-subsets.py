class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        target = {}
        result = []
        for word in words2:
            for char in word:
                target[char] = max(target.get(char,0), word.count(char))
        
        for word in words1:
            for char, count in target.items():
                if word.count(char) < count:
                    break
        
            else:
                result.append(word)
        return result