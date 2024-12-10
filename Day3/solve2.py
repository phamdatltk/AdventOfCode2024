import re

# Đường dẫn file
file_path = "input.txt"
output_file = "output1.txt"

# Biểu thức regex để tìm các chuỗi mul(X,Y), do(), và don't()
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

# Đọc dữ liệu từ file
with open(file_path, "r") as file:
    content = file.read()

# Tìm tất cả các chuỗi khớp với biểu thức regex
matches = re.findall(pattern, content)

# Lưu kết quả vào file output1.txt
with open(output_file, "w") as file:
    for match in matches:
        file.write(match + "\n")  # Ghi từng kết quả vào file, mỗi kết quả trên một dòng

print(f"Kết quả đã được lưu vào {output_file}.")

import re

# Đường dẫn file
input_file = "output1.txt"

# Khởi tạo danh sách để lưu kết quả
result_list = []

# Biểu thức regex để kiểm tra nội dung từng dòng
pattern_mul = r"mul\((\d+),(\d+)\)"  # Regex cho mul(X,Y)
pattern_do = r"do\(\)"               # Regex cho do()
pattern_dont = r"don't\(\)"          # Regex cho don't()

# Đọc file và xử lý từng dòng
with open(input_file, "r") as file:
    for line in file:
        line = line.strip()  # Loại bỏ khoảng trắng thừa

        # Kiểm tra nếu dòng có dạng mul(X,Y)
        match_mul = re.match(pattern_mul, line)
        if match_mul:
            x, y = map(int, match_mul.groups())  # Lấy X và Y, ép kiểu int
            result_list.append((x, y))
            continue

        # Kiểm tra nếu dòng có nội dung là do()
        if re.match(pattern_do, line):
            result_list.append(1)
            continue

        # Kiểm tra nếu dòng có nội dung là don't()
        if re.match(pattern_dont, line):
            result_list.append(0)

# In ra danh sách kết quả
print("Danh sách kết quả:", result_list)

result = 0
multiply = 1
for item in result_list:
    if item == 1:
        multiply = 1
        continue
    if item == 0:
        multiply = 0
        continue
    if multiply == 1:
        result = result + int(item[0])*int(item[1])

print(result)

