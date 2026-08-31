from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # unique=set(nums)
        expectedNums = []
        for i in nums:
            if i not in expectedNums:
                expectedNums.append(i)
        print(expectedNums)
        nums[:len(expectedNums)] = expectedNums
        k=len(expectedNums) 
        return(k)

if __name__ == "__main__":
    nums = [1,1,2]
    s = Solution()
    print(s.removeDuplicates(nums))  # Output: 2    
        