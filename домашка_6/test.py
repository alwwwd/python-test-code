def maximum(nums):
   Max = 0
   for item in nums:
       if item > Max:
           Max=item
   return Max

List = [1,5,8,77,24,95,1000]
print (maximum(List))
