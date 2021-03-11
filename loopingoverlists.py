pets = ["Dog", "Cat", "Bird"]
# Ypu can use len to find the length of the list
# ex print(len(pets))

# Loop over a list
index = 0

# a while loop requires a condition
while index < len(pets):
    pet = pets[index]
    print("What pet are you? Im a % s" % pet)
    index += 1


# For loop (for something in something) ("for in" loops are better for lists than While Loops)
count = 0
for pet in pets:
    print(pet)
    print(count)
    count += 1
