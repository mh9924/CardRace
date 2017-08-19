from random import randint

class Game:
    def __init__(self, numcards=21):
        self.numcards = numcards

    def takeCards(self, amount):
        self.numcards -= amount
        self.numcards = max(self.numcards, 0)

    def generateNextTurn(self):
    """Calculates next turn for computer."""
    if self.numcards <= 7 and self.numcards > 4:
        return self.numcards - 4
    if self.numcards == 3:
        return 3
    if self.numcards % 2 == 0:
        return 2
    return 1

    def main(self):
        first = input("Would you like to go first? (y/n): ")
        while self.numcards > 0:
            if first.lower() != "y" and first.lower() != "yes":
                take = self.generateNextTurn()
                print("\t", end="")
                print("I pick "+str(take)+" card(s).")
                self.takeCards(take)
            first = ""

            print("------------------------------")
            if self.numcards > 0:
                print("There are "+str(self.numcards)+" cards left")
                print("\n")
                utake = 0
                while utake < 1 or utake > 3:
                    utake = int(input("How many cards do you pick? (1-3): "))
                    if utake < 1 or utake > 3:
                        print("Please enter a number from 1 to 3.")
                print("\t", end="")
                print("You picked "+str(utake)+" card(s).")
                self.takeCards(utake)
                print("\n")
                print("There are "+str(self.numcards)+" cards left.")
            else:
                print("I win! Game over.")
                return

        print("You win! Game over.")

if __name__ == "__main__":
    main()
