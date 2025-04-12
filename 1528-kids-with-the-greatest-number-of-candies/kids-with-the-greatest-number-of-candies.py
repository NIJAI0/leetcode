from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)  # Find the current maximum candies any kid has
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result
