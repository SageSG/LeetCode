listofvalues = [1,2,4,3,6]
def solution(A):
    # write your code in Python 3.10
    curr_value = 0
    A = removeDuplicates(A)
    A = sorted(A)
    if(checkIfLessThanZero(A[0])):
        for item in sorted(A):
            if(len(A)> 0):
                if(item == curr_value + 1):
                    curr_value = item
                    print(curr_value)
                    A.remove(item)
                else:
                    break
        curr_value += 1
        return curr_value
    else:
        return 1

    
def checkIfLessThanZero(num):
    if num < 0:
        return False
    else:
        return True

def removeDuplicates(x):
  return list(dict.fromkeys(x))


print(solution(listofvalues))

