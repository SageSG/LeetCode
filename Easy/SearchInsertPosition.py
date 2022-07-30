class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        position = 0

        for index, number in enumerate(nums):
            
            if target > number: 
                print(target, number)
                position += 1
            
            else:
                break

        
        return position

test = Solution.searchInsert(Solution, [1,3,5,6], 7)

print(test)