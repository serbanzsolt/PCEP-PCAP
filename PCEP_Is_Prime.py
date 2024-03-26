def is_prime(num):
    if num > 0:
        for i in range(2, num-1):
            # print(f"num:{num}, i:{i}")
            if num % i == 0:
                return False
        return True
    else:
        print("The number you given is negative")

# print(is_prime(97))

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")