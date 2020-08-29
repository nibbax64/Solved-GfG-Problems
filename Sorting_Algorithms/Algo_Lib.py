class Sort:
	array = None
	size = None
	time_complexity = None

	def __init__(self, array):
		self.array = array
		self.size = len(array)

	def sort_it(self):
		print("Function to be overwritten")

	def __str__(self):
		return f"Time Complexity : {self.time_complexity}\nOUTPUT : {self.array}"

#----------SELECTION SORT----------
class Selection_Sort(Sort):

	def __init__(self, array):
		super().__init__(array)
		self.time_complexity = "O(n²) -- O(n²) -- O(n²)"

	def sort_it(self):
		for i in range(self.size - 1):
			min_index = i
			for j in range(i+1, self.size):
				if(self.array[j] < self.array[min_index]):
					min_index = j

			self.array[min_index], self.array[i] = self.array[i], self.array[min_index]

#----------BUBBLE SORT----------
class Bubble_Sort(Sort):

	def __init__(self, array):
		super().__init__(array)
		self.time_complexity = "O(n) -- O(n²) -- O(n²)"

	def sort_it(self):
		for i in range(self.size):
			for j in range(self.size - 1 - i):
				if(self.array[j] > self.array[j+1]):
					self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

#----------INSERTION SORT----------
class Insertion_Sort(Sort):

	def __init__(self, array):
		super().__init__(array)
		self.time_complexity = "O(n) -- O(n²) -- O(n²)"

	def sort_it(self):
		for i in range(1, self.size):
			key = self.array[i]
			j = i-1
			while(j>=0 and self.array[j]>key):
				self.array[j+1] = self.array[j]
				j = j-1
			self.array[j+1] = key

#----------QUICK SORT----------
class Quick_Sort(Sort):

	def __init__(self, array):
		super().__init__(array)
		self.time_complexity = "O(n*log(n)) -- O(n*log(n)) -- O(n²)"

	def partition(self, low, high):
		i = low-1
		pivot = self.array[high]

		for j in range(low, high):
			if(self.array[j] < pivot):
				i = i+1
				self.array[i],self.array[j] = self.array[j],self.array[i]

		self.array[i+1],self.array[high] = self.array[high],self.array[i+1]
		return i+1

	def sort_it(self, low, high):
		if(low < high):
			p = self.partition(low, high)
			self.sort_it(low, p-1)
			self.sort_it(p+1, high)

#----------MERGE SORT----------
class Merge_Sort(Sort):

	def __init__(self, array):
		super().__init__(array)
		self.time_complexity = "O(n*log(n)) -- O(n*log(n)) -- O(n*log(n))"

	def merge(self, left, mid, right):
		n1 = mid-left+1
		n2 = right-mid

		left_arr = [0 for i in range(n1)]
		right_arr = [0 for i in range(n2)]

		for i in range(n1):
			left_arr[i] = self.array[left+i]
		for j in range(n2):
			right_arr[j] = self.array[mid+1+j]

		i,j,k = 0,0,left

		while(i<n1 and j<n2):
			if(left_arr[i] <= right_arr[j]):
				self.array[k] = left_arr[i]
				i += 1
			else:
				self.array[k] = right_arr[j]
				j += 1
			k += 1

		while(i<n1):
			self.array[k] = left_arr[i]
			i += 1
			k += 1

		while(j<n2):
			self.array[k] = right_arr[j]
			j += 1
			k += 1

	def sort_it(self, left, right):
		if(left < right):
			mid = (left+right)//2

			self.sort_it(left, mid)
			self.sort_it(mid+1, right)

			self.merge(left, mid, right)

#----------RADIX SORT----------
class Radix_Sort(Sort):

	def __init__(self, array):
		super().__init__(array)
		self.time_complexity = "O(n*K) -- O(n*K) -- O(n*K)"

	def bucketSort(self, place):
		output = [0]*self.size
		count = [0]*10

		for i in range(0, self.size):
			index = self.array[i] // place
			count[index % 10] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		i = self.size - 1
		while(i >= 0):
			index = self.array[i] // place
			output[count[index % 10] - 1] = self.array[i]
			count[index % 10] -= 1
			i -= 1

		for i in range(0, self.size):
			self.array[i] = output[i]

	def sort_it(self):
		max_element = max(self.array)
		place = 1

		while(max_element//place > 0):
			self.bucketSort(place)
			place *= 10
#----------HEAP SORT----------
#----------BUCKET SORT----------
