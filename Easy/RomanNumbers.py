class Solution:
    def romanToInt(self, s: str) -> int:
        total_value = 0
        previous_value = ""
        subtract_value = False
        for index, value in enumerate(s):   
            
            match value:
                case "I":
                    total_value += 1
                case "V":
                    total_value += 5
                    if index > 0: 
                        if previous_value == "I":
                            total_value -= 2
                    
                case "X":
                    total_value += 10
                    if index > 0:
                        if previous_value == "I":
                            total_value -= 2
                case "L":
                    total_value += 50
                    if index > 0:
                        if previous_value == "X":
                            total_value -= 20
                case "C":
                    total_value += 100
                    if index > 0:
                        if previous_value == "X":
                            total_value -= 20
                case "D":
                    total_value += 500
                    if index > 0:
                        if previous_value == "C":
                            total_value -= 200
                case "M":
                    total_value += 1000
                    if index > 0:
                        if  previous_value == "C":
                            total_value -= 200
                
                    
            previous_value = value
            print(index, value, previous_value, subtract_value, total_value)
        return total_value
            
Solution.romanToInt(Solution,"MMMDCCXXIV")