    # Assume two list, remove duplicates and populate listing with unique values
list_1 = [1,2,3,4,5,6,7]
list_2 = [1,2,7,9,10,13]

unique_list = list(set(list_1 + list_2))
print("\nCombined list with unique values: ",unique_list)
    # Also remove duplicates from each list.
for list_value_1 in list_1:
    for list_value_2 in list_2:
        if list_value_1 == list_value_2:
            list_1.remove(list_value_1)
            list_2.remove(list_value_2)
print()
print ("First list with all unique values: ",list_1)
print ("Second list with all unique values: ",list_2)
