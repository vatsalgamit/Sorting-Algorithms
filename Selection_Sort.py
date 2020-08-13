#Selection sort

my_list = [11, 30, 25, 12, 11,75]
#    0   1    2   3   4


for i in range(len(my_list)):
	min_ind = i
	print(min_ind)

	for j in range(i+1,len(my_list)):
		if my_list[min_ind]>my_list[j]:
			min_ind=j

	my_list[i],my_list[min_ind] = my_list[min_ind],my_list[i]

print(my_list)