import random
import time

def bubbleSortAlgorithm(nums):
	swap = True
	while swap:
		swap = False
		for value in range(len(nums) - 1):
			if nums[value] > nums[value + 1]:
				nums[value], nums[value + 1] = nums[value + 1], nums[value]
				swap = True
	return nums

numberList = []
for value in range(1, 10000):
	numberList.append(value)

random.shuffle(numberList)

start = time.time()
bubbleSortAlgorithm(numberList)
stop = time.time()
print(numberList)
print("\n\tTime: " + str((stop - start)))
