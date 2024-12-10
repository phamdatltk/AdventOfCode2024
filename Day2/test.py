def check_safe_of_list(lst):
    if len(lst) < 2:  # Kiểm tra độ dài danh sách
        return False

    isIncrease = lst[1] - lst[0] > 0
    if lst[1] - lst[0] == 0:
        return False

    for i in range(1, len(lst)):
        if isIncrease:
            if lst[i] - lst[i - 1] <= 0 or (lst[i] - lst[i - 1]) not in [1, 2, 3]:
                return False
        else:
            if lst[i] - lst[i - 1] >= 0 or (lst[i] - lst[i - 1]) not in [-1, -2, -3]:
                return False
    return True

def remove_element(lst, index):
    if 0 <= index < len(lst):
        new_lst = lst[:index] + lst[index+1:]
        return new_lst
    return lst 



def check_safe_of_list_part_2(lst):
   for i in range(len(lst)):
      modify_list = remove_element(lst, i)
      print(modify_list)
      if check_safe_of_list(modify_list):
         return True
      
lst = [1,3,2,4,5]
print(check_safe_of_list_part_2(lst))


