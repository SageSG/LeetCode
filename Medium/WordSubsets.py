"""Runtime: 1497 ms, faster than 40.92% of Python3 online submissions for Word Subsets.
Memory Usage: 18.5 MB, less than 64.90% of Python3 online submissions for Word Subsets."""
from collections import Counter

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        
        
        answerList = []
        final_set = {}

        for subset in words2:
            
            if final_set:
                for key, value in final_set.items():
                    value["count"] = 0

            for letter in subset:
                if letter not in final_set.keys():
                    final_set[letter] = {"current":1,"count":1}
                else:
                    if final_set[letter]["count"] + 1 > final_set[letter]["current"]:
                        final_set[letter]["current"] += 1
                    final_set[letter]["count"] += 1
        

        for word in words1:
            temp = Counter(word)
            if all([alphabets in temp and container["current"]<=temp[alphabets] for alphabets, container in final_set.items()]):
                    answerList.append(word)

        return answerList

Solution.wordSubsets(Solution, ["amazon","apple","facebook","google","leetcode"], ["lo","eo"])
# Solution.wordSubsets(Solution, ["amazon","apple","facebook","google","leetcode"], ["lo","eo"])
