"""nums_a = [1, 3, 5]
nums_b = [2, 4, 6]

res = 0
for a, b in zip(nums_a, nums_b):
    res += a * b"""

"""Write a function called enum_sum which takes a list of numbers and returns the sum of the numbers multiplied by their corresponding index incremented by one.

Ex: enum_sum([2, 4, 6]) -> (index 0 + 1)*2 + (index 1 + 1)*4 + (index 2 + 1)*6 -> 1*2 + 2*4 + 3*6 -> 28


num_list = []
def enum_sum(num_list):
  num_sum = 0
  for idx, elem in enumerate(num_list):
    num_sum += (idx+1)*elem
  return num_sum

print(enum_sum([2,4,6]))
"""

"""Implement the function dbl_seq_sum which takes two lists of positive integers and computes the summation

∑k=1(−1)k⋅ak+bk1+ak⋅bk

Where ak
and bk refer to the k-th elements in the two given lists. Notice that there is no upper bound on the summation. This just means "sum over all the elements". Assume that both lists will be the same length, and take note of the starting index of the summation."""

def dbl_seq_sum(list1,list2):
  