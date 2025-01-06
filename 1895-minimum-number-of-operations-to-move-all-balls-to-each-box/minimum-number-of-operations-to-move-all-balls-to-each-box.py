class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = [0]
        c = int(boxes[0])
        for i in range(1,len(boxes)):
            l.append(c+l[i-1])
            c += int(boxes[i])
        c = int(boxes[-1])
        print(l)
        prev = 0
        for i in range(len(boxes)-2,-1,-1):
            q = c + prev
            l[i] += q 
            c += int(boxes[i])

            prev = q
        print(l)
        return l
