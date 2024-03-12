def introduction(fr, ln):
    print(fr, ln)

#positional argument passing
introduction("Zsolt", "Serbán")
#keyword argument passing
introduction(ln= "Zsolt", fr= "Serbán")

def hello(firstname, lastname = "Smith"):
    print (f"Hello {firstname} {lastname}")
    
hello("Zsolt", "Serbán")
hello("Zsolt")
hello(firstname="Zsolt")
# hello(lastname="Serbán")

# Mixing positional and keyword arguments
def substract (a, b):
    print(f"{a} - {b} = {(a - b)}")

substract(5,2)
substract(5,b=2)
# substract(a=5,2) This will generate error
substract(a=10, b=2)

# Tricky one
def intro (a, b="Bond"):
    print("My name is", b + ".", a + ".")
    
intro("Zsolt")