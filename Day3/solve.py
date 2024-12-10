import re

# Đường dẫn file
file_path = "input.txt"

# Biểu thức regex để tìm các chuỗi mul(X,Y) với X và Y là các số từ 1 đến 3 chữ số
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Đọc dữ liệu từ file
with open(file_path, "r") as file:
    content = file.read()

# Tìm tất cả các chuỗi khớp với biểu thức regex
matches = re.findall(pattern, content)

sum = 0
# In ra các kết quả
for match in matches:
    x, y = match
    print(f"mul({x},{y})")
    sum = sum + int(x)*int(y)

print(sum)