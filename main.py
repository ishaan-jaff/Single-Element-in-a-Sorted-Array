"""
In this problem, you’re given an array of sorted integers in which all of the integers, except one, appears twice. Your task is to find the single integer that appears only once.

The solution should have a time complexity of O(\log n)
O(logn)
 or better and a space complexity of O(1)
O(1)

[1,1,2,2,3,4,4,5]

[1,2,2,3,3,4,4]
 when before /left then 1st elem is odd 

[1,1,2,2,3,3,4]
# when after / right then 1st elem is even

# end condition: elem before or after != curr elem
# left
# right 

"""

def is_single(mid, nums):
  next_dir = ""
  left, right = mid - 1, mid + 1
  if left >= 0:
    if nums[left] == nums[mid]:
      if left % 2 == 0:
        next_dir = "right"
      else:
        next_dir = "left"
      return False, next_dir
  if right < len(nums):
    if nums[right] == nums[mid]:
      if mid % 2 == 0:
        next_dir = "right"
      else:
        next_dir = "left"
      return False, next_dir
  return True, ""
  

def single_non_duplicate(nums): 
  lo, hi = 0, len(nums)-1

  while lo <= hi:
    mid = lo + ((hi-lo)//2)
    result, dir = is_single(mid, nums)
    if result:
      return nums[mid]
    # go left 
    if dir == "left":
      hi = mid - 1
    if dir == "right":
      lo = mid + 1
  return -1
      
    

  # Write your code here to find the single element in a sorted array.
  
  # You may use the code template provided in the binary_search.py file.

  return -1


print(single_non_duplicate([1,1,2,3,3,4,4]))

print(single_non_duplicate([1,2,2,3,3,4,4]))
print(single_non_duplicate([1,1,2,2,3,3,4,4,5]))
print(single_non_duplicate([1,1,2,2,3,3,4,4,]))