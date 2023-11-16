total_blocks = int(input("Enter the number of blocks: "))
blocks = 1
level = 1

for lvl in range(1, total_blocks):
    if blocks <= total_blocks:
        blocks += lvl+1
        level = lvl
        # continue
    else:
        break
 
print("The height of the pyramid:", level)
