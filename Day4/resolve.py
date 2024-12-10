############ 0 -> 1
# Đọc nội dung từ file input.txt
with open('input0.txt', 'r') as infile:
    lines = infile.readlines()

# Lật ngược nội dung mỗi dòng
reversed_lines = [line.strip()[::-1] for line in lines]

# Ghi nội dung lật ngược vào file input1.txt
with open('input1.txt', 'w') as outfile:
    for line in reversed_lines:
        outfile.write(line + '\n')

############ 0 -> 2
# Đọc nội dung từ file input0.txt
with open('input0.txt', 'r') as infile:
    lines = infile.readlines()

# Chuyển đổi các dòng thành danh sách các cột
# Loại bỏ ký tự newline và chia mỗi dòng thành một danh sách các ký tự
columns = list(zip(*[line.strip() for line in lines]))

# Ghi nội dung vào file input2.txt
with open('input2.txt', 'w') as outfile:
    for column in columns:
        outfile.write(''.join(column) + '\n')

############ 0 -> 3
# Đọc nội dung từ file input0.txt
with open('input0.txt', 'r') as infile:
    lines = infile.readlines()

# Chuyển đổi các dòng thành danh sách các cột và lật ngược thứ tự dòng
columns = list(zip(*[line.strip() for line in lines[::-1]]))

# Ghi nội dung vào file input3.txt
with open('input3.txt', 'w') as outfile:
    for column in columns:
        outfile.write(''.join(column) + '\n')

############ 0 -> 6
# Đọc nội dung từ file input0.txt
with open('input0.txt', 'r') as infile:
    lines = infile.readlines()

# Loại bỏ ký tự newline ở cuối mỗi dòng
lines = [line.strip() for line in lines]

# Lấy các phần tử chéo từ trên xuống từ trái sang phải
result = []
max_len = len(lines) + len(lines[-1]) - 1  # Tính độ dài tối đa của kết quả

# Duyệt qua các vị trí chéo
for i in range(max_len):
    diagonal = ''
    for j in range(len(lines)):
        if i - j >= 0 and i - j < len(lines[j]):
            diagonal += lines[j][i - j]
    if diagonal:
        result.append(diagonal)

# Ghi kết quả vào file input6.txt
with open('input6.txt', 'w') as outfile:
    for line in result:
        outfile.write(line + '\n')


############ 6 -> 4
# Đọc nội dung từ file input.txt
with open('input6.txt', 'r') as infile:
    lines = infile.readlines()

# Lật ngược nội dung mỗi dòng
reversed_lines = [line.strip()[::-1] for line in lines]

# Ghi nội dung lật ngược vào file input1.txt
with open('input4.txt', 'w') as outfile:
    for line in reversed_lines:
        outfile.write(line + '\n')

########## 1 -> 5
# Đọc nội dung từ file input1.txt
with open('input1.txt', 'r') as infile:
    lines = infile.readlines()

# Loại bỏ ký tự newline ở cuối mỗi dòng
lines = [line.strip() for line in lines]

# Lấy các phần tử chéo từ trên xuống từ trái sang phải
result = []
max_len = len(lines) + len(lines[-1]) - 1  # Tính độ dài tối đa của kết quả

# Duyệt qua các vị trí chéo
for i in range(max_len):
    diagonal = ''
    for j in range(len(lines)):
        if i - j >= 0 and i - j < len(lines[j]):
            diagonal += lines[j][i - j]
    if diagonal:
        result.append(diagonal)

# Ghi kết quả vào file input6.txt
with open('input5.txt', 'w') as outfile:
    for line in result:
        outfile.write(line + '\n')


############# 5 -> 7
# Đọc nội dung từ file input.txt
with open('input5.txt', 'r') as infile:
    lines = infile.readlines()

# Lật ngược nội dung mỗi dòng
reversed_lines = [line.strip()[::-1] for line in lines]

# Ghi nội dung lật ngược vào file input1.txt
with open('input7.txt', 'w') as outfile:
    for line in reversed_lines:
        outfile.write(line + '\n')


listInput = ['input0.txt','input1.txt','input2.txt','input3.txt','input4.txt','input5.txt','input6.txt','input7.txt']
count = 0
for input in listInput:
    # Đọc nội dung từ file input0.txt
    with open(input, 'r') as infile:
        lines = infile.readlines()

    # Duyệt qua từng dòng và đếm số lần xuất hiện của 'XMAS'
    for line in lines:
        count += line.count('XMAS')

    # In kết quả

print(f"Số lần xuất hiện của 'XMAS' là: {count}")

