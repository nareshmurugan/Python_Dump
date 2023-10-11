import time
start=time.time()
# Python program for implementation of Bubble Sort
def bubbleSort(arr):
	n = len(arr)
	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):
			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
# Driver code to test above
arr=[81,94,11,96,12,35,17,95,28,58]
bubbleSort(arr)
end=time.time()
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i])
print(end)
