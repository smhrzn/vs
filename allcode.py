#simple calaulator:
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     # take input from the user
#     choice = input("Enter choice(1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))

#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
#     else:
#         print("Invalid Input")



#rock paper scissor
import random

bot=['rock','paper','scissor']

ans=random.choice(bot)

def user_input():
    user=input("Enter "R" for  rock ,Enter P for  paper or,Enter S for scissor:")
    if user=="R" or user=="r":
        print("You chose Rock")
    elif user=="P" or user=="p":
        print("You chose paper")  
    elif user=="S" or user=="s":
        print("You chose Scissor")
    else:
        print("Invalid move")
    print("Bot choose:",ans)
    return user
    
user_input()


def condition(user_input):
    if user_input==bot:
        print("Draw")
    elif (user_input=='rock' and bot=='scissor')or(user_input=='paper'and bot=='rock') or (user_input=='scissor'and bot=='paper'):
        print("User won")
    else:
        print("Bot wins!")
    
condition(user_input)
