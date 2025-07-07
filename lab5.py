#  Lab  5 Husuke Nishoka
#  Step 2
#def cat_greeting(word):
    #print(f"Cat says {word}")
#cat_greeting("meow")

# Step 1

def cat_greeting(user, greeting):
    answer = input("You approach the cat. Do you pet it? (answer with a yes or no!!):")
    if answer == "Yes":
        print(f"{user}, you stink!! The cat runs away from you.")
    elif answer == "yes":
        print(f"{user}, you stink!! The cat runs away from you.")
    else:
        print(f"Cat says {greeting}")
cat_greeting("Sydney", "meow")
#I got a little creative on this one.. (I made it so it works with a capital/non capital answer)^^
    
# Step 2
def generate_superhero_power(name, power):
    name = "Johnny"
    power = "Flying"
    print(f"{name}'s super power is {power}")
generate_superhero_power("name", "power")

# Step 3 
def generate_superhero_power1():
    power = "Flying"
    return power
print(generate_superhero_power1())

#  Step 4
def generate_superhero_power(name, power):
    user_name = name
    super_power = power
    print(f"{user_name}'s super power is {super_power}")
generate_superhero_power("My mom", "Invisibility")

#  Step 5
def  cat_greetings_loop(Greeting):
    for i in range(5):
        print(f"Cat says {Greeting}")
cat_greetings_loop("Meow")

# Step 6
def generate_multiple_superpowers():
    superheropowers = ["Flying", "Invisibility", "Teleportation"]
    for  i in superheropowers:
        print(i)
generate_multiple_superpowers()