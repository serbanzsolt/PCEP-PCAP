num = int(input("Positive Integer: "))
step_counter = 0

while num != 1:
    if num % 2 == 0:
        num = int(num / 2)
    else:
        num = 3 * num + 1
    
    print(f"{step_counter}. Step: {num}")
    step_counter += 1

else:    
    print(f"{step_counter}. Step: {num}")

print(f"Total steps: {step_counter}")
    

