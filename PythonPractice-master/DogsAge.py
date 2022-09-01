DogAge = int(input("Enter a dog's age in human years: "))

if DogAge < 0:
    print("We cant count 0 ")
elif DogAge < 3:
    dog_age = DogAge * 10.5
else:
    dog_age = DogAge * 4 + 13
print("The dog's age in human years is: ", dog_age)