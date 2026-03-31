import random

print("Welcome to the rock paper scissor game!!!")
 
option = ["rock", "paper","scissor"]

user = input("Choose rock, paper or scissor:").lower()
computer = random.choice(option)

print("User: ",user)
print("Computer: ",computer)

# user winning case:
if(user == "paper" and computer == "rock"):
    print("User win!!")
elif(user == "scissor" and computer == "paper"):
    print("User win!!")
elif(user == "rock" and computer == "scissor"):
    print("User win!!")

# computer winning case:
elif(user == "paper" and computer == "scissor" ):
    print("Computer win!!")
elif(user == "scissor" and computer == "rock" ):
    print("Computer win!!")
elif(user == "rock" and computer == "paper" ):
    print("Computer win!!")

# draw case:
elif(user == computer):
    print("Draw!!")

else:
    print("Invalid input!!")