class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        print(s)
        total = 0

        prev_char = ""
        while len(s) >= 1:
            if s[0] == "I":
                prev_char = "I"
                total += 1
                s=s[1:]

            if ((prev_char == "V") or (prev_char == "X")) and (s[0] == "I"):
                total -= 1
                s=s[1:]
            else:
                print(s)
                if s[0] == "V":
                    prev_char = "V"
                    total += 5
                    s = s[1:]
                else:
                    print("not V")

                if s[0] == "X":
                    prev_char = "X"
                    total += 10
                    s = s[1:]
                else:
                    print("not X")

            # if prev_char == "X" and s[0] == "I":
            #     total -= 1
            #     s=s[1:]
            
            # elif s[0] == "X":
            #     prev_char = "X"
            #     total += 10
            #     s = s[1:]

            # if prev_char == "L" and s[0] == "X":
            #     total -= 10
            #     s=s[1:]
            
            # elif s[0] == "L":
            #     prev_char = "L"
            #     total += 50
            #     s = s[1:]

            # if prev_char == "C" and s[0] == "X":
            #     total -= 10
            #     s=s[1:]
            
            # elif s[0] == "C":
            #     prev_char = "C"
            #     total += 100
            #     s = s[1:]
                    
            # if prev_char == "D" and s[0] == "C":
            #     total -= 100
            #     s=s[1:]
            
            # elif s[0] == "D":
            #     prev_char = "D"
            #     total += 500
            #     s = s[1:]
                    
            # if prev_char == "M" and s[0] == "C":
            #     total -= 100
            #     s=s[1:]
            
            # elif s[0] == "M":
            #     prev_char = "M"
            #     total += 1000
            #     s = s[1:]
            
        
        print(total)
        return total
        
Solution().romanToInt("III")