class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        d = {}
        for i in range(len(score)):
            d[score[i]] = i
        score.sort(reverse = True)
        res = ["0"]*len(score)

        res[d[score[0]]] = "Gold Medal"
        if len(score)>=2: res[d[score[1]]] = "Silver Medal"
        if len(score)>=3:res[d[score[2]]] = "Bronze Medal"

        for i in range(3,len(score)):
            res[d[score[i]]] = str(i+1)

        return res