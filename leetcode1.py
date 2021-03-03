## https://leetcode.com/problems/basic-calculator-ii/submissions/

class Solution:
    def calculate(self, s: str) -> int:
        
        temp_list = []
        temp = ''
        
        for i in range(len(s)):
            if s[i].isdigit():
                temp += s[i]
            elif s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
                temp_list.append(temp)
                temp_list.append(s[i])
                temp = ''
        temp_list.append(temp)
        
        i = 0
        
        while i < len(temp_list):
            if (temp_list[i] == "*"):
                
                x = temp_list.pop(i - 1)
                y = temp_list.pop(i)
                temp_list[i - 1] = int(x) * int(y)
                i -= 1
                
            elif (temp_list[i] == "/"):
                
                x = temp_list.pop(i - 1)
                y = temp_list.pop(i)
                temp_list[i - 1] = int(x) // int(y)
                i -= 1
            
            i += 1
            
        for i in range(len(temp_list)):
            
            if temp_list[i] == "+":
                
                temp_list[i + 1] = int(temp_list[i - 1]) + int(temp_list[i + 1])
            
            elif temp_list[i] == "-":
                
                temp_list[i + 1] = int(temp_list[i - 1]) - int(temp_list[i + 1])
            
        return temp_list[-1]