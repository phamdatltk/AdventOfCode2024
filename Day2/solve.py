import shutil

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


# Copy file input to a temp file
source_file = 'input.txt'
destination_file = 'temp.txt'

shutil.copy(source_file, destination_file)
print(f"File {source_file} đã được sao chép thành {destination_file}.")

result1 = 0

# Đường dẫn file
file_path = 'temp.txt'

while True:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if not lines:  # Nếu file rỗng, dừng vòng lặp
        break

    first_line = lines[0].strip()
    first_line_list = [int(value) for value in first_line.split()]

    with open(file_path, 'w') as file:
        file.writelines(lines[1:])

    print("Dòng: ", first_line_list)
    print("Check: ", check_safe_of_list_part_2(first_line_list))

    if check_safe_of_list_part_2(first_line_list):
        result1 += 1

print("Result1: ", result1)
