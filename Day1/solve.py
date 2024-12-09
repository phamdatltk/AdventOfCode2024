# Đường dẫn tới file input.txt
file_path = 'input.txt'

# Khởi tạo hai danh sách để lưu các giá trị từ hai cột
list1 = []
list2 = []

# Đọc dữ liệu từ file và tách thành hai danh sách
with open(file_path, 'r') as file:
    for line in file:
        # Bỏ các khoảng trắng dư thừa và chia dòng theo tab hoặc khoảng trắng
        columns = line.strip().split()
        
        # Thêm giá trị vào danh sách
        if len(columns) == 2:  # Đảm bảo dòng có đúng 2 cột
            list1.append(int(columns[0]))
            list2.append(int(columns[1]))

list1.sort()
list2.sort()

### Puzzle 1
sum = 0

for i in range(len(list1)):
   sum += abs(list1[i]-list2[i])
   
print("Puzzle 1: ",sum)


### Puzzle 2
sum = 0
for member1 in list1:
   count = 0
   for member2 in list2:
      if member1==member2:
         count = count + 1
         
   sum = sum + member1*count
   
print("Puzzle 2: ",sum)