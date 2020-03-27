def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
   
    rev = reverse(s) 
    if (s == rev): 
        return True
    return False
  
  
s = input("Ju lutemi, shkruani nje tekst : ")
ans = isPalindrome(s) 
  
if ans == 1: 
    print("TRUE") 
else: 
    print("FALSE") 

    #Referenca:
    #https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/