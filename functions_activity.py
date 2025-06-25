menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

def total_price(item1, item2):
    total_sum = menu[item1] + menu[item2]
    return total_sum
    
print(total_price('Pizza', 'Burger'))

#sentence = f"The total price of {menu['item1']} and {menu['item2']} is {total_sum}"
 #  print(sentence)
#  do f strings work with this?? ^^^


#next function

def price_difference(item1, item2):
    total_difference = menu[item1] - menu[item2]
    return total_difference
    
print((abs(price_difference('Pizza', 'Burger'))))

#next function
#def inflation(item1): 
    #inflated_price = menu[item1] * 1.5
    #return inflated_price
    #menu['item1'] = inflated_price
    #print(menu)
#print(inflation('Pizza'))


def inflation(item1): 
    #inflated_price = menu[item1] * 1.5
    #return inflated_price
    menu.update({item1: menu[item1]*1.5})
    print(menu)
print(inflation('Ice cream'))

#last function
def deflation(item1):
    menu.update({item1: menu[item1]/1.5})
    print(menu)
print(inflation('Cheese'))

#my own  function

#this function will identify the cost of an item while the restaurant is on happy hour

def happy_hour(item1):
    discount = menu[item1]/2
    #return discount
    #print(discount)
    print(f"The price of {item1} is ${discount} during happy hour.")
print(happy_hour('Pizza'))