class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        # for i in range(low, high+1):
        #     a=i//10
        #     b=i%10
        #     if a==b:
        #         count+=1
        # return count
        for i in range(low, high+1):
            s = str(i)
            if len(s)%2==0:
                mid = len(s)//2
                left = s[:mid]
                right = s[mid:]
                if sum(map(int, left))==sum(map(int, right)):
                    count+=1
        return count
