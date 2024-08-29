fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products
print("Joined tuple (food_stuff_tp):", food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print("Converted list (food_stuff_lt):", food_stuff_lt)
length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length // 2 - 1 : length // 2 + 1]
else:
    middle_items = food_stuff_lt[length // 2]
print("Middle item(s):", middle_items)
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First three items:", first_three_items)
print("Last three items:", last_three_items)
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print("food_stuff_tp has been deleted.")
