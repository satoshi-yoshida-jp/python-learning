import random

cards = ["jack", "queen", "king"]


def main():

    random.seed(42)

    print(random.choices(cards, k=2))
    print(random.choices(cards, k=2))

    random.seed(42)
    print(random.choices(cards, k=2))
    print(random.choices(cards, k=2))


main()
