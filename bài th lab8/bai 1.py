def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_sinh_doi(gioi_han):
    so_nguyen_to_sinh_doi = []
    so_nguyen_to_truoc = None
    
    for num in range(3, gioi_han):
        if la_so_nguyen_to(num):
            if so_nguyen_to_truoc and num - so_nguyen_to_truoc == 2:
                so_nguyen_to_sinh_doi.append((so_nguyen_to_truoc, num))
            so_nguyen_to_truoc = num
    
    return so_nguyen_to_sinh_doi

gioi_han = 1000
so_nguyen_to_sinh_doi = tim_so_nguyen_to_sinh_doi(gioi_han)

print("Cac so nto sinh doi be hon 1000 :")
for prime1, prime2 in so_nguyen_to_sinh_doi:
    print(f"({prime1}, {prime2})")
