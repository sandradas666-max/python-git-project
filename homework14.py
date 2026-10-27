
import random
import math

names = input("Enter customer names separated by commas: ")

# Split names and remove extra spaces
name_list = [name.strip() for name in names.split(",") if name.strip()]

# Remove duplicate names
unique_names = list(set(name_list))

# Shuffle the list randomly
random.shuffle(unique_names)

# Pick 2 winners
winners = random.sample(unique_names, 2)

# Display the winners in reverse
print("Winner 1:", winners[0][::-1])
print("Winner 2:", winners[1][::-1])

# Count unique participants
total = len(unique_names)
print("Total unique participants:", total)

# Calculate rounded square root
result = round(math.sqrt(total))
print("Rounded square root:", result)
