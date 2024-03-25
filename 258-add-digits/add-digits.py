class Solution:
    def addDigits(self, num: int) -> int:
        d = set()
        while num not in d and num>9:
            d.add(num)
            s = 0
            while num>0:
                s = s+ num%10
                num = num//10
            num = s
        if num in d:return -1
        return num        
