
import random
class Wordle:
    #varibles
    chosenWord = ""
    wordsFile = "words.txt"
    numChances = 5
    guess = ""
    won = False
    lost = False

    #colors 
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    GRAY = "\033[90m"




    #constructors 

    def __init__(self):
        self.setChosenWord()
        self.printWordleBanner()
        while(not self.won and not self.lost):
            self.getGuess()
            print(self.checkGuess())
            self.checkWin()
            print(f"Remaing guess: {self.remaining()}")

        if self.lost:
            print(f"Wordle Word: {self.secretWord()}")
            self.printGameOverBanner()
        else:
            self.printWinBanner()



    #banners
    def printWordleBanner(self):
        banner = r"""
#   #   ###   ####   ####   #      #####
#   #  #   #  #   #  #   #  #      #
# # #  #   #  ####   #   #  #      ####
## ##  #   #  #  #   #   #  #      #
#   #   ###   #   #  ####   #####  #####
"""
        print(banner)

    def printWinBanner(self):
        banner = r"""
#   #   ###   #   #       #   #  #####  #   #
 # #   #   #  #   #       #   #    #    ##  #
  #    #   #  #   #       # # #    #    # # #
  #    #   #  #   #       ## ##    #    #  ##
  #     ###    ###        #   #  #####  #   #
"""
        print(banner)

    def printGameOverBanner(self):
        banner = r"""
 ####    #    #   #  #####        ###   #   #  #####  ####
#       # #   ## ##  #           #   #  #   #  #      #   #
#  ##  #####  # # #  ####        #   #   # #   ####   ####
#   #  #   #  #   #  #           #   #   # #   #      #  #
 ####  #   #  #   #  #####        ###     #    #####  #   #
"""
        print(banner)


    #getters

    def getGuess(self):
        curGuess = ""
        while len(curGuess) != 5 or not curGuess.isalpha():
            curGuess = input("Enter valid guess: ")
        self.guess = curGuess.upper()

    def checkWin(self):
        if self.guess == self.chosenWord:
            self.won = True
        else:
            self.numChances -= 1
            if self.numChances == 0:
                self.lost = True

    def secretWord(self):
        return self.chosenWord
    def remaining(self):
        return self.numChances
        
    def checkGuess(self):
        chosenList = list(self.chosenWord)
        letterCount = {}

        for char in chosenList:
            if char in letterCount:
               letterCount[char] += 1
            else:
                letterCount[char] = 1

        output = [None] * len(self.guess)

        # first pass fill in green letters 
        for i in range(len(chosenList)):
            if (self.guess[i] == chosenList[i]):
                output[i] = f"{self.GREEN}{self.guess[i]}{self.GRAY}"
                letterCount[self.guess[i]] -=1

        # second pass  in yellow letters 
        for i in range(len(chosenList)):
            if output[i] == None:
                if (self.guess[i] in letterCount):
                    if(letterCount[self.guess[i]] != 0):
                        output[i] = f"{self.YELLOW}{self.guess[i]}{self.GRAY}"
                        letterCount[self.guess[i]] -=1

        #final pass remaing letters gray
        for i in range(len(chosenList)):
            if output[i] == None:
                output[i] = f"{self.GRAY}{self.guess[i]}{self.GRAY}"


        return "".join(output)


    
    #setters 
    def setChosenWord(self):
        with open(self.wordsFile) as file:
            words = file.read().splitlines()
        self.chosenWord = random.choice(words).upper()

def main():
    game = Wordle()

if __name__ == "__main__":
    main()
                

    