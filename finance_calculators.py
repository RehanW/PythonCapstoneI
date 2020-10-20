import math
#COMPULSORY TASK

#First we need to display some output of choices to the user.
print("Choose  either 'investment' or 'bond' from the menu below to proceed: \n\n"
      "investment \t - to calculate the amount of interest you'll earn on interest. \n"
      "bond \t\t - to calculate the amount you'll have to pay on a home loan.")

#Next we will promp the user for their choice.
choice = input("Please enter which option you would like to go with: ").lower()

#Next we will check the selection and prompt the user for information based on their previous choice.
#In the first block we will code the program for choice of investment
if choice == "investment":
    P = float(input("Please enter the amount of money you'd like to invest: "))
    r = float(input("Please enter the interest rate: ")) / 100
    t = float(input("Please enter the number of years you'd like to invest for: "))
    interest_t = input("Please enter the type of interest, 'simple' or 'compound', that"
                       "you would like to receive: ").lower()

#Now we will decide based on user input which formula to use and print the answer
    if interest_t == "simple":
        returns = round(P * (1 + r * t), 2)
        print(returns)
    elif interest_t == "compound":
        returns = round(P * math.pow((1 + r), t), 2)
        print(returns)

#In this block we will code the program for choice of bond
elif choice == "bond":
    P = float(input("Please enter the present value of the house: "))
    i = float(input("Please enter the interest rate on the bond: "))/100 / 12
    n = int(input("Please enter the planned number of months to repay the bond: "))
    repay_amount = round((i * P) / (1 - math.pow((1 + i), (-n))), 2)
    print(repay_amount)
