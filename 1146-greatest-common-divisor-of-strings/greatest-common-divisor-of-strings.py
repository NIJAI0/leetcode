class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1+str2==str2+str1):
            a= len(str1)
            b= len(str2)
            while b!=0:
                r=b
                b=a%b
                a=r
            return str1[:a]
        else:
            return ""