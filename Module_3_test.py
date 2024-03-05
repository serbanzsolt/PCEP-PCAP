def elvalaszto ():
    print("\n------------------------------------------------------------\n")
elvalaszto()
# 01 - What is the output of the following snippet?

t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

elvalaszto()
# 02 - How many Stars

i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
    
elvalaszto()
# 03 - Sum of all vals elements

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(sum(vals))

# 04 - How many elements the list contains
