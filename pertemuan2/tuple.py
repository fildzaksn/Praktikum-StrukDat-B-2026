#imuttable
#tuple pakai kurung biasa
#secara harfiah sm aja kek list

"""Change Tuple Values
ou can convert the tuple into a list, 
change the list, 
and convert the list back into a tuple."""

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

