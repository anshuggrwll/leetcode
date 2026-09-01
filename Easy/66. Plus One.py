
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=digits[-1]
        if num<9:
            digits[-1]=num+1
        else:
            digits[-1]=1
            digits.append(0)
        return(digits)

if __name__ == "__main__":
    digits = [1, 2, 3]
    s = Solution()
    print(s.plusOne(digits))  # Output: [1, 2, 4]