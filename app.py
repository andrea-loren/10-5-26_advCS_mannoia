'''
Description & Instructions:
- This is an escape room game. Your job as a player is to escape the room before the clock runs out!
- You will be presented with three randomly selected puzzles.
- Correct answers award keys. Incorrect answers result in player death.
- The Gold Key is the final key and lets you out of the room. Good luck!

AI Use:
- I used AI the same way as I did in the last program where my code broke :(
- AI was helpful in explaining 

Technical Risk:
- I found some extra time this weekend to incorporate some of the technical risks I had in my last program.
- These include the "class" function, object-oriented programming, "for" loops, arrays, functions, and libraries.
- I also included the "enumerate" and "any" functions.

Notes
'''

# importing time & random libraries necessary to play escape room
import time
import random

# beginning of Player class
class Player: # class basically creates a "blueprint"

    # beginning of initialization function
    def __init__(self, name):
        self.name = name
        self.inventory = [] # player starts with an empty inventory
    # end of initialization function

    # beginning of addKey function
    def addKey(self, keyName):
        self.inventory.append(keyName) # adds the key to the inventory
    # end of addKey function

    # beginning of showInventory function
    def showInventory(self):
        print(f"{self.name}'s Inventory: ")
        
        # beginning of inventory checking conditional
        if not self.inventory:
            print("(Empty)")
        else:
            print(f"{index}. {item}")
        # end of inventory checking conditional
    # end of showInventory function
# end of Player class

# beginning of Question class
class Puzzle:

    # beginning of initialization function
    def __init__(self, answer):
        self.question = question
        self.answer = answer.strip.lower()
        self.explanation = explanation
    # end of initialization function
# end of Puzzle class

# beginning of EscapeRoom class
class EscapeRoom:

    # beginning of initialization function
    def __init__(self):
        self.initTime = time.time()
        self.timeLimit = 300 # 60 sec * 5 for 5 min
        self.keysNeeded = ["Bronze Key", "Silver Key", "Gold Key"]
    # end of initialization function

    # beginning of getTimeRemaining function
    def getTimeRemaining(self):
        elapsed = time.time() - self.initTime
        remaining = self.timeLimit - elapsed
        return max(0, int(remaining))
    # end of getTimeRemaining function

    # beginning of checkTimeUp function
    def checkTimeUp(self):
        return self.getTimeRemaining <= 0 # returns boolean value of whether it's true or false that getTimeRemaining is <= 0
    # end of checkTimeUp function
# end of EscapeRoom class

# end of blueprints, start of game logic!

# beginning of loadPuzzle function
def loadPuzzle(): # this function stores & returns random puzzles
    return [ # first array that will return a random puzzle
        # nested arrays containing puzzle details
        Puzzle( # puzzle 1
            "You find a scrap of paper that reads 'HBV.' On the wall next to it, the phrase 'Three steps forwards' is scratched. What is the secret password?",
            "key",
            "Three letters after H is the letter K; B becomes E, and V becomes Y."
        ),
        Puzzle( # puzzle 2
            "This room contains three-legged stools and four-legged chairs. There are five total pieces of furniture and seventeen total legs. How many stools are there? Enter the number as an integer.",
            "3",
            "Three stools means nine legs; two chairs means eight legs. Nine plus eight gives seventeen."
        ),
        Puzzle( # puzzle 3
            "To get to the next door, you must follow the cardinal directions. Take two steps North, one step East, one step South, and two steps West. Enter your final coordinate location relative to the starting point (e.g. (1, 0) would be 1 East).",
            "(-1, 1)",
            "Two West and one East results in one West (-1), and two North and one South results in one North (1). Together, that's (-1, 1) on a Cartesian plane."
        ),
        Puzzle( # puzzle 4
            "In this room, you find a chalkboard with the word 'LISTEN' written on it. A note beneath the word says, 'Rearranged, what must you do to hear the truth?'",
            "silent",
            "You can rearrange the letters of 'LISTEN' to make the word 'SILENT.'"
        ),
        Puzzle( # puzzle 5
            "A monitor displays the following binary sequence: 1011. A note on the monitor instructs you to convert it to a normal number. Enter the number as an integer",
            "11",
            "1011 has an eight, no fours, a two, and a one (in that order). Added together gives you eleven."
        ),
        Puzzle( # puzzle 6
            "You find a stone with numbers carved into it. These numbers read: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ? Enter the next number in the sequence as an integer.",
            "89",
            "This is the Fibonacci sequence! Each number is the sum of the two previous numbers. Thirty-four plus fifty-five results in eighty-nine."
        ),
        Puzzle( # puzzle 7
            "A dusty book flips open in front of you. Its open pages show you a question: 'The more of them you take, the more you leave behind. What are they?'",
            ["steps", "footsteps"],
            "Think about it: the more steps you take, the more you're leaving behind you."
        ),
        Puzzle( # puzzle 8
            "This room is a laboratory. A note on the door says, 'You associate me with potassium, but you spell me with barium and sodium. What am I?",
            "banana",
            "Bananas have potassium (K) in them, but to literally spell the word, you can use barium (Ba) and two sodiums (Na)."
        ),
        Puzzle( # puzzle 9
            "A computer terminal reads the string 'ahead' in green letters. But when you look down to enter the word, you notice that all the keys have been shifted to the right! What keys would you type?",
            "sjrsf",
            "To the right of 'A' is 'S,' to the right of 'H' is 'J,' to the right of 'E' is 'R,' and to the right of 'D' is 'F.'"
        )
        # end of arrays
    ]
    # end of return array
# end of loadPuzzle function

# beginning of gameplay function
def playGame():
    
    # beginning of welcome & player name storage
    print("Welome to the escape room!")
    playerName = input("Enter your name: ").strip()
    if not playerName:

        playerName = "Player"
    # end of welcome & player name storage

    player = Player(playerName) # call Player class with playerName in the self parameter
    game = EscapeRoom() # call EscapeRoom class

    puzzles = loadPuzzle() # load the puzzles into the game
    selectedPuzzles = random.sample(puzzles, 3) # randomly select three puzzles

    # beginning of instructions
    print(f"Greetings, {playerName}! You are locked in a room.")
    print("You have exactly five minutes (300 seconds) to solve three puzzles and escape.")
    print("Failure or wrong choices will result in a tragic end...")
    # end of instructions

    for stage_index, puzzle in enumerate(selectedPuzzles):

        timeLeft = game.getTimeRemaining()

        if game.checkTimeUp():

            break

        print(f"Puzzle {stage_index + 1} of 3:")
        print(f"Time remaining: {timeLeft // 60}m {timeLeft % 60}s")
        print(f"Challenge: {puzzle.question}")

        userAnswer = input("Your answer: ").strip().lower()

        while userAnswer == "":

            print("You must enter an answer!")
            if game.checkTimeUp:
                break
            userAnswer = input("Your answer: ").strip().lower()
        
        if userAnswer == puzzle.answer:

            awardedKey = game.keysNeeded[stage_index]
            player.addKey(awardedKey)

            print("Correct! Here is the explanation behind your logic:")
            print(puzzle.explanation)
            print(f"You retreived the {awardedKey}")
            player.showInventory()

        else:
            print("Incorrect!")
            print(f"Game over, {player.name}!")
            return

    if game.checkTimeUp:
        print("Time is up!")
        print(f"Game over, {player.name}!")
        return

    hasGoldKey = any(key == "Gold Key" for key in player.inventory)

    if hasGoldKey:
        print(f"Congratulations, {player.name}!")
        print("You insert the Gold Key into the final door and step out to freedom!")
        print(f"Time remaining upon escape: {timeLeft / 60}m {timeLeft % 60}s")

playGame()
'''
Pseudocode:

import libraries
player blueprint
    initialization function
        variable for name
        array for inventory
    key-adding function
        add keys to inventory array
    inventory-showing function
        print player's inventory
        if the inventory is empty
            print empty
        else
            print the inventory
puzzle blueprint
    initialization function
        variable for question
        variable for answer (stripped of spaces and capitals)
        variable for hint
escape room blueprint
    initialization function
        start timer
        set time limit
        define what keys are needed in an array
    time remaining function
        variable calculating elapsed time
        variable subtracting elapsed time from start time to get time left
        return how much time is left to user
    time up function
        if the returned value from the previous function is less than/equal to 0
            return the time remaining function (will be used later)
puzzle pool function
    return one of the following puzzles
        puzzle 1
        puzzle 2
        puzzle 3
        puzzle 4
        puzzle 5
        puzzle 6
death function
    return one of the following deaths
        death 1
        death 2
        death 3
        death 4
        death 5
        death 6
gameplay function
    print welcome
    let user input name
        if user doesn't input a name, assign "player"
    assign name to player class
    call escape room class
    load the puzzle pool
    use random to pick random puzzle
    print instructions
    loop through three selected puzzles to play
        check how much time is left
        if time is up
            break loop
        print puzzle number, remaining time, & question
        get user input for answer
        while answer is not one of options
            force user to keep entering answers
            if time is up
                break loop
            try to get answer from user input again
        if user answers correctly
            check which key user needs next
            add that key to user's inventory
            print hint, key, inventory
        else
            use random to pick random death
            user dies
            print death, game over
            return to top of playing loop
    if time is up
        print time up
        user dies
        return to top of playing loop
    if user has gold key
        print congrats
call gameplay function
'''