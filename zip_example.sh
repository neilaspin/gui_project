#!/usr/bin/env python
a =[1,2,3,4,5]
b =['a','b','c','d','e','f']
for x,y in zip(a,b):
    if len(a) == len(b):
        print(x,y)
    else:
        print("This is no good")
        exit(255)
#def selection_sort(arr):
#  spot_marker = 0
#  comparisons = 0
#while spot_marker <  len(arr):
#  comparisons += 1
#  for num in range(spot_marker, len(arr)):
#    comparisons += 1
#    if arr[num] < arr[spot_marker]:
#      arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
#  spot_marker += 1
#print(comparisons)
#l = [6,8,1,4,10,7,8,9,3,2,5]
#selection_sort(l)
#print(l)

def selection_sort(arr):
  spot_marker = 0
  comparisons = 0
while spot_marker < len(arr):
  comparisions += 1
  for num in range(spot_marker, len(arr)):
    comparisons += 1
    if arr[num] < arr[spot_marker]:
      arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
  spot_marker += 1
print(comparisons)

