checking = "yes"

while checking == "yes":
    print("What is your age: ")
    user_input = int(input())
    if user_input >= 18:
        print("You can vote")
    else:
        print("You cant vote")
    print("Would you like to check another age?")
    user_input2 = input()
    checking = user_input2
    
list1 = [3, -1, 0, 6, -4]

for x in list1:
    if x > 0:
        print("Value is positive")
    elif x < 0:
        print("Value is negative")
    else:
        print("Number is  0")

inventory =  ["tnt", "glass", "grass", "Netherite", "Waxed Lightly Weathered Chiseled Copper Stairs"]

for i in inventory:
    if i == "Netherite":
      print(f"You found {i}, congrats!")
    else:
      print(f"You have {i}")
      


  
