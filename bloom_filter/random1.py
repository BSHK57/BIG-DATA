import random

# Generate 100 random 2-3 digit numbers (10-999)
random_numbers = [random.randint(10, 999) for _ in range(1000)]

# Save to a file, one number per line
with open("elements.txt", "w") as file:
    for num in random_numbers:
        file.write(str(num) + "\n")

print("Numbers saved to 'random_numbers.txt'")
