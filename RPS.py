import random as rd
running = True
while running:    
    print("Welcome to Rock Paper Scissors, Python Edition!")
    player = input("Choose Rock, Paper, or Scissors ")
    computerPlay = rd.randint(0,2)
    yesValues = ["y", "yes", "true", "t"]
    def yn(val):
        return val.lower() in yesValues
    print(computerPlay)
    rock = ["rock", "Rock", "ROCK", "r", "R"]
    paper = ["paper", "Paper", "PAPER", "p", "P"]
    scissors = ["scissors", "Scissors", "SCISSORS", "s", "S", "Scissor", "SCISSOR", "scissor"]
    humanPlay = 3
    convertedFails = 0
    possiblePlays = [rock, paper, scissors]
    def convertPlays(play, list, playList):
        if play in list:
            humanPlay = playList.index(list)
        else:
            convertedFails += 1
            return
    
            


    def winner(ai, human):
        if ai == human:
            return("Tie!")
    if convertedFails > 3:
        print("Oops, you didn's seem to pick a possible move. Resetting")
        continue
    again = input("Play again?)