def liters_100km_to_miles_gallon(liters):
    return ((100_000/1609.344) / (liters/3.785411784))

def miles_gallon_to_liters_100km(miles):
    return ((1/((miles*1609.344)/1000)*100)*3.785411784)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))