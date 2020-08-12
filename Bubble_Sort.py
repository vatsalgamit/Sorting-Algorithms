#Bubble Sort 

list1 = [int(input('Enter Elements: ')) for x in range(int(input('How many elements? : ')))]
print(list1)

def Bubble_Sort(list1):
	for i in range(len(list1)-1,0,-1):
		for j in range(i):
			if list1[j]>list1[j+1]:
				#Swapping
				# temp = list1[j]
				# list1[j]=list1[j+1]
				# list1[j+1]=temp
				list1[j], list1[j+1] = list1[j+1], list1[j]

	print(list1)

Bubble_Sort(list1)