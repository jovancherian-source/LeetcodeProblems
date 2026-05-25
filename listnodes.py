list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
real_list = [n for i in list_of_lists for n in i]
print(real_list)