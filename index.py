class Guesser:
    def __init__(self, number,lives):
        self.number = number
        self.lives = lives

    def guess(self, number):
        if self.lives == 0:
            print("You lost!")
            return False
        if number == self.number: print("You won!")
        else:
            self.lives -= 1
            if self.lives != 1:
                print("You still have %d lives!" % self.lives)
                return False
            if self.lives == 1:
                print("You still have %d life!" % self.lives)
                return False
            if self.lives == 0:
                print("Last chance!")
                return False

guesser = Guesser(5, 3)

guesser.guess(2)
guesser.guess(1)
guesser.guess(3)
guesser.guess(0)