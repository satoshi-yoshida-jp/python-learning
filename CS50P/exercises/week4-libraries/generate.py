import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
print("Shuffled")
for card in cards:
    print(card)

print("=============")

card = random.choice(cards)
print(f"Random choice: {card}")

print("=============")

number = random.randint(1, 10)
print(f"Random number: {number}")