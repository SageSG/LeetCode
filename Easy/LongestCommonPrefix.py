class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length_of_word = len(strs[0])
        prefixes_list = []
        match_list = []
        answer = ""

        while length_of_word > 0:
            prefixes_list.append(strs[0][0:length_of_word])
            match_list.append(0)
            length_of_word -= 1

        if prefixes_list == []:
            return ""


        for index, x in enumerate(prefixes_list):
            for i in range(len(strs)):
                if x in strs[i][0:len(x)]:
                    match_list[index] += 1
                    
                else:
                    break

        match_list.reverse()        
        prefixes_list.reverse()
        
        for index, item in enumerate(match_list):
            if item == len(strs):
                answer = prefixes_list[index]

            if item != len(strs):
                break

        return answer

            
test = Solution.longestCommonPrefix(Solution, 

["flower","flow","flight"])
print(test)