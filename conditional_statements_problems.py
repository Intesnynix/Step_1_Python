


#Check for even or odd
"""Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number).
Note: Return "Even" if the number is even; otherwise, return "Odd"."""
# def checkOddEven(x):
#     if x%2 == 0:
#         return "even"
#     else:
#         return "odd"     
# num = int(input("enter your number"))
# print(checkOddEven(num))






#check the status
"""Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False."""
# class Solution:
#     @staticmethod
#     def checkStatus(a, b, flag):
#       if not flag:
#          return (a<0 and b>=0) or (a>=0 and b<0)
#       else:
#          return a<0 and b<0
#     print(checkStatus(-4,10,False))
#     print(checkStatus(-4,-10,True))




# Trouble with Angry Friends
"""There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. 
You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false"""
# def friends_in_trouble(j_angry, s_angry):
#     if j_angry == True and s_angry == True:
#         return True
#     else:
#         return False
# print(friends_in_trouble(True,False))
# print(friends_in_trouble(True,True))
    





# Check for Equal Occurrences of 'cat' and 'hat' in a String
"""You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
Note: str contains only lowercase English alphabets."""
# def cat_hat(str):
#     if "cat" in str and "hat" in str:
#         return True
#     else:
#         return False
# print(cat_hat("catinahat"))
# print(cat_hat("agahatt"))
# print(cat_hat("aksfifua"))





#Conditional Boolean Evaluation
"""You are given a number N, you need to print its multiplication table."""
# def multiplicationTable(N):
#     result = ""
#     for i in range(1,11):
#         result += f"{N} x {i} = {N * i}\n"
#     return result
# print(multiplicationTable(5))



# Print Characters at Even Indices in a String
"""You are given a string s, you need to print its characters at even indices(index starts at 0)."""
# def string_slicer(s):
#     for i in range(0,len(s),2):
#         print(s[i])
# string = "odsagufufasjfguas"
# print(string_slicer(string))



# Print Numbers in Decreasing Order
""" Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line."""
# def printInDecreasing(x):
#     while(x>=0):
#         print(x) 
#         x-=1
# print(printInDecreasing(5))




# Jumping through While 
"""Given a positive integer x, the task is to print the numbers from 1 to x in the order as 1^2, 2^2, 3^2, 4^2, 5^2, ... (in increasing order)"""
# def printIncreasingPower(x):
#     i = 1
#     while(i <=x):
#         print(i**2)
#         i+=1    
# print(printIncreasingPower(10))

    


# Zero Converter
"""You are given a number n. The number n can be negative or positive.
If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. 
If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function."""
# def pos(n):
#     while(n > 0):
#         n-=1
#         print(n , end =" \n" , )
# def neg(n):
#     while(n<=0):
#         n+=1
#         print(n, end="\n")
# print(pos(5))
# print(neg(-5))



