chuoi = input("Nhap chuoi: ")
result_string = ""
for char in chuoi:
    if char != ' ':
        result_string += char
print("Chuoi sau khi bo khoang trang:", result_string)
