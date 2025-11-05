import random

print("🎲  Rolling a six-sided die 10 times:\n")

for i in range(1, 11):
    roll = random.randint(1, 6)  # generates a random number between 1 and 6
    #print(f"Roll {i}: {roll}")
    print(i, "-",roll)