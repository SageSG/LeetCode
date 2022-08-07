"""Runtime: 103 ms, faster than 46.60% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 59.40% of Python3 online submissions for Palindrome Number."""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        half = len(x)//2

        is_true = True



        for i in range(half):
            if x[i] != x[len(x)-(i+1)]:
                is_true = False

       
                # break
            
            

Solution.isPalindrome(Solution, 121)
