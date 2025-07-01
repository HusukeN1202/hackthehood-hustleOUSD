#Story

cookbook = ["Sushi", "Pizza", "Food"]

def create(recipe):
    cookbook.append(recipe)
    print(f"The recipe for {recipe} has been added")

def read(index):
    if index < (len(cookbook)):
        return cookbook[index]
    else:
        print("Please pick an index within the range")
        read(index)

def update(index, recipe):
    if index < (len(cookbook)):
        cookbook[index] = recipe
        print("This recipe has been updated!")
    else:
        print("Error")
        read(index)

def destroy(index):
    if index < (len(cookbook)):
        cookbook.pop(index)
        print(f"The recipe for {cookbook[index]} has been removed.")
    else:
        print('Please make sure the index is  within range.')
        read(destroy)

def list_all_recipes():
    for i in range(len(cookbook)): 
        print(cookbook[i])

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()



