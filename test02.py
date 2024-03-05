mylist = [[0,1,2,3] for i in range(2)]
print(mylist)
# print(mylist[2][0])

num1 = [1,2,3]
num2 = num1[-1:-2]

print(num1, num2,sep=" | ")

ml = [1,2,3]
ml.insert(0,1)
print(ml)

a = [0,1,2]
a[0], a[2] = a[2], a[0]
print(a)

var = 1
while var < 10:
    print("#")
    var = var << 1

t = [[3-i for i in range(3)] for j in range(3)]
print(t)
s = 0
for i in range(3):
    print(i)
    print(t[i][i])
    s += t[i][i]
print(s)

my_list = [i for i in range(-1, 2)]
print(len(my_list))
for i in my_list:
    print(f"i: {i}")