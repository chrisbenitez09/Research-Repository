Month = input("Enter a Month: ")

if Month == "February":
    print("No. of Days 28/29")
elif Month in ("April", "June" , "September" ,"November"):
    print("No. of Days 30")
elif Month in ("January", "March", "May", "July", "August", "October" , "December"):
    print("No. of Days 31")
else:
    print("You didn't type the correct Month")