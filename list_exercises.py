


# Min and Max in list
"""Given an array arr. Your task is to find the minimum and maximum elements in the array.
Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum."""
# class Solution:
#     def get_min_max(arr):
#         return max(arr) , min(arr)
#     number = [1,2,3,4,21,532,5555]
#     maximum , minimum = get_min_max(number)
#     print("maximum = ", maximum)
#     print("minimum = ", minimum)



# Union of two arrays
"""You are given two arrays a[] and b[], return the Union of both the arrays in any order.
The Union of two arrays is a collection of all distinct elements present in either of the arrays. 
If an element appears more than once in one or both arrays, it should be included only once in the result.
Note: Elements of a[] and b[] are not necessarily distinct."""
# class Solution:    
#     def findUnion(self, a, b):
#         self.a = a
#         self.b = b
#         return list(set(a)|set(b))
# sol = Solution()
# a = [12,32,"1aa", "adva"]
# b= [12,31,32,"wada", "grhd"]
# print(f"Union = {Solution().findUnion(a,b)}")




# Intersection of two sorted arrays
"""Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.
Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.
Note: If there is no intersection then return an empty array."""
# class Solution:
#     def intersection(self, arr1, arr2):
#         self.arr1 = arr1
#         self.arr2 = arr2
#         return list(set(arr1) & set(arr2))
# sol = Solution()
# arr1 = [1241,4124,443]
# arr2 = [1241,4124,43]
# newArr1 = sorted(arr1)
# newArr2 = sorted(arr2)
# print(f"Intersection = {Solution().intersection(newArr1,newArr2)}")





