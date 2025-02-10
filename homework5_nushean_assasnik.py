# List Exercise
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig"]  # Create a list with 6 items

print("The full list is:", my_list)  # Print the full list

# Print the first two items using slicing
print("The first two items in the list are:", my_list[0], my_list[1])

# Print the middle two items using slicing
print("The middle two items in the list are:", my_list[2], my_list[3])

# Print the first and last items using indexes
print("The first and last items in the list are:", my_list[0], my_list[-1])
# Tuple Exercise
menu = ("burger", "pizza", "pasta", "salad", "soup")  # Create a tuple with 5 foods

print("Original menu:")
for item in menu:  # Print each item using a loop
    print(item)

# Create a new tuple with two updated items
updated_menu = ("burger", "pizza", "sushi", "burrito", "soup")

print("\nUpdated menu:")
for item in updated_menu:  # Print each item in the new tuple
    print(item)

