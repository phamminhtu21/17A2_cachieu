fib_sequence = [0, 1] 
for i in range(2, 100):
    next_number = fib_sequence[i-1] + fib_sequence[i-2]
    if next_number >= 100: break
    fib_sequence.append(next_number)
print("Chuỗi Fibonacci số cuối cùng nhỏ hơn 100 là:", fib_sequence)