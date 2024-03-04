# beker = input("Adj meg egy számot: ")
# print(beker)

print(0.0000000000000000000001)
print("I like \"Monty Python\"")
print(1/1)
print(2//4)
print(0//2)
# print(4//0)
print("modulo ", 1%2*3)

print(2+3*5.)
x=y=z=1
print(x,y,z, sep="malacka")

y = 2+3*5.
print(y)


print(3 * "Alma")
print("Alma" * 3)
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

lista = 99 * [0]
print(lista[98])

lista.append("paraszt")
print(f"{len(lista)} hosszú a tömb")

lista.pop()
print(lista)

print(2+3*5.)
vals  = []
print(len(vals))

one = []
print(len(one))
two = one
print(len(one), len(two))
two.append(1)
two.append(2)
two.append(3)
print(len(one), len(two))
print(one, two, sep=" | ")