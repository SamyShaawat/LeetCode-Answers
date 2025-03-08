class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        recolor = 0
        res = k
        for r in range(len(blocks)):
            if blocks[r] == "W":
                recolor +=1
            if r - l + 1 == k:
                res = min(res, recolor)
                if blocks[l] == "W":
                    recolor -=1
                l+=1
        return res

