class Solution:
    def maxScore(self, s: str) -> int:
        one_count = s.count('1')
        zero_count = 0
        score = 0
        for i in range(len(s)-1):
            if s[i] == '1':
                one_count -=1
            else:
                zero_count +=1
            score = max(score, one_count+zero_count)

            print(score)
        return score

        