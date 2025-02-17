class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        hashmap = Counter(tiles)
        def backTrack():
            res = 0
            for key in hashmap:
                if hashmap[key] > 0:
                    hashmap[key] -=1
                    res +=1
                    res += backTrack()
                    hashmap[key] +=1
            return res
        return backTrack()
            
        