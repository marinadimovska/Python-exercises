sample_list = [1, 1, 8, 4, 4, 2, 4, 8]
count_dict = {}

for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("#############")
print("Original list ", sample_list)

print("Printing count of each item", count_dict)
