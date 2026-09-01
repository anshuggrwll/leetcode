from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expectedNums=[]
        for i in nums:
            if val != i:
                expectedNums.append(i)

        nums[:len(expectedNums)]=expectedNums  
        k=len(expectedNums)
        return k
        

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    s = Solution()
    print(s.removeElement(nums, val))  # Output: 2