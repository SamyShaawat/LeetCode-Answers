class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for char in s:
            map1.append(s.index(char))
            # print(s.index(char))
        # print(map1)
        for char in t:
            map2.append(t.index(char))
            # print(t.index(char))
        # print(map2)
        if map1 == map2:
            return True
        return False
                