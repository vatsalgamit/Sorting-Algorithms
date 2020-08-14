#Insertion Sort

def insertion_sort(my_list):
	for i in range(1,len(my_list)):
		x = my_list[i]

		while my_list[i-1]>x and i>0:
			print('my_list',my_list)
			my_list[i],my_list[i-1]=my_list[i-1],my_list[i]
			i = i-1
	return my_list

my_list = [2,5,8,1,2,3,5,6]
print(insertion_sort(my_list))
