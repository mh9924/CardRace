from random import randint

class Deck:
    def __init__(self, numcards=21):
        self.numcards = numcards

    def takeCards(self, amount):
        self.numcards -= amount
        self.numcards = max(self.numcards, 0)

def generateNextTurn(game):
    """Calculates next turn for computer."""
    if game.numcards <= 7 and game.numcards > 4:
        return game.numcards - 4
    if game.numcards == 3:
        return 3
    if game.numcards % 2 == 0:
        return 2
    return 1

def main():
    game = Deck()
    first = input("Would you like to go first? (y/n): ")
    while game.numcards > 0:
        if first.lower() != "y" and first.lower() != "yes":
            take = generateNextTurn(game)
            print("\t", end="")
            print("I pick "+str(take)+" card(s).")
            game.takeCards(take)
        first = ""

        print("------------------------------")
        if game.numcards > 0:
            print("There are "+str(game.numcards)+" cards left")
            print("\n")
            utake = 0
            while utake < 1 or utake > 3:
                utake = int(input("How many cards do you pick? (1-3): "))
                if utake < 1 or utake > 3:
                    print("Please enter a number from 1 to 3.")
            print("\t", end="")
            print("You picked "+str(utake)+" card(s).")
            game.takeCards(utake)
            print("\n")
            print("There are "+str(game.numcards)+" cards left.")
        else:
            print("I win! Game over.")
            return
        
    print("You win! Game over.")

main()
