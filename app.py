'''
Description & Instructions:
- This is an escape room game. Your job as a player is to escape the room before the clock runs out!
- You will be presented with three randomly selected logic puzzles from a pool of six.
- Correct answers award keys and points you to the right door. Incorrect answers result in player death.
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

# beginning of Puzzle class
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
        self.timeLimit = 600 # 60 sec * 10 for 10 min
        self.keysNeeded = ["Bronze Key", "Silver Key", "Gold Key"]
    # end of initialization functoin

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
def loadPuzzle(): # this puzzle stores & returns random puzzles
    return [
        Puzzle( # puzzle 1
            "There are two guards and two doors. One door leads to freedom and the other to a locked cell. One guard always lies, the other always tells the truth. They know which they are, and where the two doors go. You do not know which guard is which, or which door is which. You can ask one yes or no question. What do you ask to determine which door leads to freedom?\n \nA. Does this door lead to freedom?\nB. Would the other guard say this door leads to freedom?\nC. Does this door lead to imprisonment?\nD. If I asked you if this door leads to freedom, would you say yes?",
            "a" or "d",
            "B. In either case, the response would be a lie. The truthful guard would tell the truth about what the lying guard would say, and the lying guard would lie about what the truthful guard would say.\nD. In either case, the response would be the truth. The truthful guard would tell the truth, and the lying guard would essentially double-lie, lying first about his response and then again about what his response would be."
        ),
        Puzzle(
            "You have two ropes and a lighter. Each rope takes exactly 60 minutes to burn from start to end. The ropes do not burn evenly."
        )
    ]
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