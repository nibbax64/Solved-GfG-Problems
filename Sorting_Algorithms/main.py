from Algo_Lib import *
from random import shuffle
if __name__ == "__main__":
	array = list(map(int, input("INPUT -> ").split()))
	n = len(array)
	while True:
		print(f"INPUT : {array}")
		print("_"*24)
		print("|  [1] Selection Sort  |")
		print("|  [2] Bubble Sort     |")
		print("|  [3] Insertion Sort  |")
		print("|  [4] Quick Sort      |")
		print("|  [5] Merge Sort      |")
		print("|  [6] Radix Sort      |")
		print("|  [7] Heap Sort       |")
		print("|  [8] Bucket Sort     |")
		print("| ~Keyboard Interrupt~ |")
		print("‾"*24)
		choice = int(input("CHOICE : "))
		if(choice == 1):
			obj = Selection_Sort(array)
			obj.sort_it()
			print(obj)
		elif(choice == 2):
			obj = Bubble_Sort(array)
			obj.sort_it()
			print(obj)
		elif(choice == 3):
			obj = Insertion_Sort(array)
			obj.sort_it()
			print(obj)
		elif(choice == 4):
			obj = Quick_Sort(array)
			obj.sort_it(0, n-1)
			print(obj)
		elif(choice == 5):
			obj = Merge_Sort(array)
			obj.sort_it(0, n-1)
			print(obj)
		elif(choice == 6):
			obj = Radix_Sort(array)
			obj.sort_it()
			print(obj)
		else:
			print("! Wrong Input !")
		shuffle(array)
		print()

# 1727 8174 214 99 4 84 2774 17 1624 35 4 845 25 46 9 8541
