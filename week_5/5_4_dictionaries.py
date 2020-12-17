# key value pairs
fruit_bowl = {}

fruit_bowl["apple"] = 4
fruit_bowl["banana"] = 2

print(fruit_bowl)

# get()
user_input = input("What kind of fruit will you add?")
fruit_bowl[user_input] = fruit_bowl.get(user_input, 0) + 1

print(fruit_bowl)

# iterate over all keys

for fruit, quanity in fruit_bowl.items():
    print(fruit, quanity)

# in tests keys (not values)
if "pineapple" in fruit_bowl:
    print("What an exotic fruitbowl!")
else:
    print("What a mundane fruitbowl!")

if 4 in fruit_bowl.values():
    print("there are four of something")

# exercise 3 and 4 require files, we'll cover that next week, but you can have look
