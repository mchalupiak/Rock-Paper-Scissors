import random as rd


running = True
while running:    
    
    print("Welcome to Rock Paper Scissors, Python Edition!")
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
    print(str(convertedFails) + " rock")
    convertPlays(paper)
    print(str(convertedFails) + " paper")
    convertPlays(scissors)
    print(str(convertedFails) + " scissors")
    if convertedFails > 2:
        print("Oops, you didn's seem to pick a possible move. Resetting")
        continue

    if humanMove == computerMove:
        print("Tie!")
    
    elif humanMove == "Rock" and computerMove == "Scissors" or humanMove == "Paper" and computerMove == "Rock" or humanMove == "Scissors" and computerMove == "Paper":
        print("You Win!")
    
    elif computerMove == "Rock" and humanMove == "Scissors" or computerMove == "Paper" and humanMove == "Rock" or computerMove == "Scissors" and humanMove == "Paper":
        print("You Lose!")
    
    print("You choose " + humanMove + " and the computer Choose " + computerMove)
    again = input("Play again? ")
    if yn(again):
        continue
    else:
        break
