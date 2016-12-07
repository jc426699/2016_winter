#names = []
names = ["Alice", "Tom", "John"] #list of string
ages = [10, 40, 25] #list of int

print(names[1]) #print second data
print(names[-1])

while True:
    name = input("Enter a name:")

    if name == "":
        break #exit while loop

    names.append(name)

print(names)
