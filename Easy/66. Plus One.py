
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num=num+1
        arr = list(map(int, str(num)))
        return (arr)
        
if __name__ == "__main__":
    digits = [9,9]
    s = Solution()
    print(s.plusOne(digits))  # Output: [1, 0, 0]