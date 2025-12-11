class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        dict_x = dict()
        dict_y = dict()

        for building in buildings:

            if(building[0] not in dict_x):
                dict_x[building[0]] = SortedList([building[1]])
            else:
                dict_x[building[0]].add(building[1])

            if(building[1] not in dict_y):
                dict_y[building[1]] = SortedList([building[0]])
            else:
                dict_y[building[1]].add(building[0])
        
        ans = 0        
        for building in buildings:
            x = building[0]
            y = building[1]

            if(dict_x[x][0] != y and dict_x[x][-1] != y and dict_y[y][0] != x and dict_y[y][-1] != x):
                ans += 1
        
        return ans