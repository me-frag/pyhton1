print("select your ride:")
print("Car")
print("Bike")

choice=int(input("Enter your Choice:"))

if choice == 1:
    print("What type of Car?")
    print("1.Lexus\n2.Nissan")
    choice=int(input("Enter your choice2:"))
    if choice==1:
        print("you have selected Lexus")
    else:
        print("you have selected Nissan")
elif choice == 2:
    print("What type of bike?")
    print("1.scooty\n2.scooter")
    choice3=int(input("Enter your choice3:"))
    if choice3==1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")

else:
    print("Wrong choice!")
