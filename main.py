print("Welcome to RollerCoaster!!!")
height = int(input("What is your height in cm? "))
currency = "$"
bill = 0

if height >= 120:
    print("Good news, You can ride the Rollercoaster.")
    age = int(input("Please, Enter your age: "))
    if age <= 12:
        print(f"Child Ticket cost {currency}5")
        bill = 5
    elif age <= 18:
        print(f"Youth Ticket cost {currency}7")
        bill = 7
    else:
        print(f"Adults Ticket cost {currency}12")
        bill = 12
    # ask the user if he/she wants a photo
    want_photo = input("Do you want a photo? Type y if yes, n if no: ")
    if want_photo == "y":
        bill += 3
else:
    print("Sorry you can't ride a Rollercoaster.")

print(f"Your total bill is {currency}{bill}")
