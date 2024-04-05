while True:
    # Nhập hai số từ người dùng
    n1 = float(input("Nhập số thứ nhất: "))
    n2 = float(input("Nhập số thứ hai: "))

    s = n1 + n2
    a = n1 - n2
    b = n1 * n2
    c = n1 / n2
    d = n1 ** n2
    e = n1 ** 0.5
    g = n2 ** 0.5

    print(" cộng:", s)
    print(" trừ:", a)
    print(" nhân:", b)
    print("chia:", c)
    print("lũy thừa:", d)
    print("Căn bậc hai của số thứ nhất:", e)
    print("Căn bậc hai của số thứ hai:", g)


    choice = input("Bạn có muốn tiếp tục không? (y/n): ")
    if choice.lower() != 'y':
        break