import random as rd


print("Welcome to Rock Paper Scissors, Python Edition!")
humanScore = 0
computerScore = 0
running = True
while running:    
    
    player = input("Choose Rock, Paper, or Scissors ")
    computerPlay = rd.randint(0,2)
    yesValues = ["y", "yes", "true", "t"]
    def yn(val):
        return val.lower() in yesValues

    rock = ["rock", "r"]
    paper = ["paper", "p"]
    scissors = ["scissors", "s", "scissor"]
    humanPlay = 3
    humanMove = ""
    convertedFails = 0
    possibleHumanPlays = [rock, paper, scissors]
    possibleComputerPlays = ["Rock", "Paper", "Scissors"]
    computerMove = possibleComputerPlays[computerPlay]
    def convertPlays(list):

        if player.lower() in list:
            global humanPlay
            global humanMove
            humanPlay = possibleHumanPlays.index(list)
            humanMove = possibleComputerPlays[humanPlay]
            
        else:
            global convertedFails
            convertedFails += 1
    convertPlays(rock)
    convertPlays(paper)
    convertPlays(scissors)
    if convertedFails > 2:
        print("Oops, you didn's seem to pick a possible move. Resetting")
        continue

    if humanMove == computerMove:
        print("Tie!")
    
    elif humanMove == "Rock" and computerMove == "Scissors" or humanMove == "Paper" and computerMove == "Rock" or humanMove == "Scissors" and computerMove == "Paper":
        print("You Win!")
        humanScore += 1

    
    elif computerMove == "Rock" and humanMove == "Scissors" or computerMove == "Paper" and humanMove == "Rock" or computerMove == "Scissors" and humanMove == "Paper":
        print("You Lose!")
        computerScore += 1
    
    print("You choose " + humanMove.lower() + " and The Computer choose " + computerMove.lower())
    print("Your score is " + str(humanScore))
    print("The Computer's score is " + str(computerScore))
    again = input("Play again? ")
    if yn(again):
        continue
    else:
        break
