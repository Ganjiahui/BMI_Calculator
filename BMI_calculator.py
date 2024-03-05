print("This is a BMI detector program")
print("Press q to terminate the program")
print()
a = int(input("Enter your BMI in kg: "))

while True:
    if a <= 24:
        print("You have a healthy BMI score")
        break
    elif a > 24:
        print("You have unhealthy BMI score!")
        break
    else:
        print("Thank you!")
        break