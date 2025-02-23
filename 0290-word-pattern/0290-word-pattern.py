class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = []
        map2 = []
        for char in pattern:
            map1.append(pattern.index(char))
        # print(map1)
        s = s.split()
        for word in s:
            map2.append(s.index(word))
        # print(map2)
        if map1 == map2:
            return True
        return False

        