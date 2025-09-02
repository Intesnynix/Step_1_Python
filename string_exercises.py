




# Convert String to LowerCase
"""Given a string s. The task is to convert string characters to lowercase."""
# class Solution:
#     def tolower(self,s:str):
#         self.s = s
#         return s.lower()
# soln = Solution()
# print(f"Lower = {soln.tolower("SFGHSEUFGSSDFBSIOESKGHHSE")}")




# Reverse Words
"""Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).
Note: The string may contain leading or trailing dots(.) or multiple dots(.) between two words. 
The returned string should only have a single dot(.) separating the words, and no extra dots should be included."""
# class Solution:
#     def reverseWords(self,s):
#         print(f"The original sentence is {("I....dont.like.to.code")}")
#         words = s.split(".")
#         cleanWords = []
#         for w in words:
#             if w != "":
#                 cleanWords.append(w)
#         cleanWords.reverse()
#         return".".join(cleanWords)
# sol = Solution()
# print(f"The reverse is {sol.reverseWords("I....dont.like.to.code")}")




# String Validation and Formatting
"""Given name of a person, the task is to welcome the person by printing the name with "Welcome". 
If name is "John", you should print "Welcome John"."""
# def welcomeAbroad():
#     name = input("Enter your name: ")
#     return name
# print(f"Welcome {welcomeAbroad()}")




# Slicing in String
"""Given a string of braces named bound_by, and a string named tag_name. 
The task is to print a new string such that tag_name is in the middle of bound_by."""
# def join_middle(bound_by, tag_name):
#   return bound_by[0 :len(bound_by)//2] + tag_name + bound_by[len(bound_by)//2:] #for equal halves
# print(f"{join_middle("<>","Suck")}")


# Repeat the strings
"""Given two strings a and b.
 The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. 
New string should be like shorter+longer+shorter."""
# def combo_string(a, b):
#     if len(a)< len(b):
#         short = a
#         longer = b
#     else:
#         short = b
#         longer = a
#     return short + longer + short
# print(combo_string("yolo", "poopie"))





# Palindrome String
"""You are given a string s. Your task is to determine if the string is a palindrome. 
A string is considered a palindrome if it reads the same forwards and backwards."""
# class Solution:
#     def isPalindrome(self, s):
#         return s == s[::-1] #IDENTATION MATTERS
# sol = Solution()
# print(f"{sol.isPalindrome('madam')}")
# print(f"{sol.isPalindrome('abra')}")




# Remove all duplicates from a given string
"""Given a string s which may contain lowercase and uppercase characters.
The task is to remove all duplicate characters from the string and find the resultant string. 
The order of remaining characters in the output should be same as in the original string."""
# class Solution:
# 	def removeDuplicates(self, s):
# 		dupe = set()
# 		result = []
# 		for char in s:
# 			if char not in dupe:
# 				dupe.add(char)
# 				result.append(char)
# 		return "".join(result)
# sol = Solution()
# print(sol.removeDuplicates("amalgum"))










# Check Anagram String
"""Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order."""
# class Solution:
#     def charCount(self,word):
#         count = {}
#         for char in word:
#             count[char] = count.get(char,0)+1
#         return count
#     def areAnagrams(self, s1, s2):
#         return self.charCount(s1) == self.charCount(s2)
# sol = Solution()
# print(sol.areAnagrams("evil", "live"))
# print(sol.areAnagrams("optimism", "hello"))
