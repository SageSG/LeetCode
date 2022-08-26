"""Check if first string and second string is the same"""
from collections import Counter
from re import A

class Solution:
    def solution(self, words1: str, words2: str):
        if(len(words1) != len(words2)):
            return False
        
        temp = Counter(words1)
        temp2 = Counter(words2)
        if (temp == temp2):
            return True
        
        print(temp, temp2)
        return False

# Solution.solution(Solution, 'zbk', 'zkb')


"""Get 2nd max value from list"""
class Solution2:
    def solution(self, input1: int, input2: list[int]):
        if (len(input2)==0):
            print('-1')
            return -1

        input2.sort(reverse=True)
        if input2[1] < input2[0]:
            return input2[1]
       
        return -1
        

# print(Solution2.solution(Solution2, 3, [2,2,2]))
global arraylist
arraylist = []

# Python3 program to print postorder
# traversal from preorder and inorder
# traversals
 
# A utility function to search x in
# arr[] of size n
def search(arr, x, n):
      
    for i in range(n):
        if (arr[i] == x):
            return i
 
    return -1
 
global arrayList
arrayList = []
def printPostOrder(In, pre, n):
     
    root = search(In, pre[0], n)
 
    if (root != 0):
        printPostOrder(In, pre[1:n], root)
 
    if (root != n - 1):
        printPostOrder(In[root + 1 : n],
                      pre[root + 1 : n],
                      n - root - 1)
 
    arrayList.append(pre[0])
 
printPostOrder([ 4, 2, 5, 1, 3, 6 ], [ 1, 2, 4, 5, 3, 6 ], 6)
print(arrayList)



