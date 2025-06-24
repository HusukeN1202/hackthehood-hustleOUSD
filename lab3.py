food = "cheese pizza"
print(food[0:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food  =  ' '.join(food_list)
print(joined_food)

#task 2: working with lists

number_list = [1, 384, 67, 908, 10]
number_list.append(20)
print(number_list)
number_list.insert(3, '86')
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)
print(number_list[0:3])
print(number_list[-3:])

# Task 3: working with dictionaries

books = {'Dr. Seuss': 'Cat in the hat', 'Asato  Asato': '86', 'Sharon Creech': "Walk Two Moons", 'Paul Auster':"Moon palace"}
print(books.keys())
print(books.values())
print(books.get('Sharon Creech'))
books.pop(list(books.keys())[2])
print(books)
del books[list(books.keys())[0]]
print(books)