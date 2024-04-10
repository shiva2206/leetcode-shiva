class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = [0]*len(deck)
        i = 0
        deck.sort()
        c = True
        while i<len(deck):
            for j in range(len(res)):
                if c:
                    if res[j]==0:
                        res[j] = deck[i]
                        i+=1
                        c = False
                else:
                    if res[j]==0:
                        c = True
        return res

