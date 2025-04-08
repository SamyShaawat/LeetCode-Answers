class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        output = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:  
                    output.append(f"{h}:{m:02d}")  
        return output