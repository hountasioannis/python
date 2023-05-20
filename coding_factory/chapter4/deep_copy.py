import copy

original_list = [1,2,[3,4],5]

shallow_copy = original_list.copy()

original_list[2][0] = 333
print(original_list,shallow_copy)

original_list = [1,2,[3,4],5]

deep_copy = copy.deepcopy(original_list)

original_list[2][0] = 333
print(original_list,deep_copy)