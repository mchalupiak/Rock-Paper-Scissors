import random as rd


running = True
while running:    
    
    print("Welcome to Rock Paper Scissors, Python Edition!")
    player = input("Choose Rock, Paper, or Scissors ")
    computerPlay = rd.randint(0,2)
    yesValues = ["y", "yes", "true", "t"]
    def yn(val):
        return val.lower() in yesValues

    rock = ["rock", "Rock", "ROCK", "r", "R"]
    paper = ["paper", "Paper", "PAPER", "p", "P"]
    scissors = ["scissors", "Scissors", "SCISSORS", "s", "S", "Scissor", "SCISSOR", "scissor"]
    humanPlay = 3
    humanMove = ""
    convertedFails = 0
    possibleHumanPlays = [rock, paper, scissors]
    possibleComputerPlays = ["Rock", "Paper", "Scissors"]
    computerMove = possibleComputerPlays[computerPlay]
    def convertPlays(play, list, playList, avaliblePlays):

        if play in list:
            humanPlay = playList.index(list)
            humanMove = avaliblePlays[humanPlay]
            return(humanMove)
            
        else:
            convertedFails =+ 1
            return(convertedFails)
    
    convertPlays(player, rock, possibleHumanPlays, possibleComputerPlays)
    convertPlays(player, paper, possibleHumanPlays, possibleComputerPlays)
    convertPlays(player, scissors, possibleHumanPlays, possibleComputerPlays)
    print(convertedFails)
    if convertedFails > 2:
        print("Oops, you didn's seem to pick a possible move. Resetting")
        continue

    if humanMove == computerMove:
        print("Tie!")
    
    elif humanMove == "Rock" and computerMove == "Scissors" or humanMove == "Paper" and computerMove == "Rock" or humanMove == "Scissors" and computerMove == "Paper":
        print("You Win!")
    
    elif computerMove == "Rock" and humanMove == "Scissors" or computerMove == "Paper" and humanMove == "Rock" or computerMove == "Scissors" and humanMove == "Paper":
        print("You Lose!")
    
    print("You choose " + humanMove + " And the computer Choose " + computerMove)
    again = input("Play again?")
    if yn(again):
        continue
    else:
        break
