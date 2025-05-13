import numpy as np
choices = ["rock", "paper", "scissors"]

go = True
i = 0
num_moves = int(input("how many rounds of rock paper scissors?"))
win = ""
wins = 0
ties = 0
losses = 0
while go:
    ai_move = np.random.randint(0, 3)
    ai_move = choices[ai_move]
    move = input("rps?: ")
    if move == "r" or move == "R":
        move = "rock"
    elif move == "p" or move == "P":
        move = "paper"
    elif move == "s" or move == "S":
        move = "scissors"
    elif move == "quit":
        go = False
        break
    if move == "rock" and ai_move == "rock":
        win = "Tie"
        ties += 1
    elif move == "paper" and ai_move == "paper":
        win = "Tie"
        ties += 1
    elif move == "scissors" and ai_move == "scissors":
        win = "Tie"
        ties += 1
    elif move == "rock" and ai_move == "paper":
        win = "Lose"
        losses += 1
    elif move == "rock" and ai_move == "scissors":
        win = "Win"
        wins += 1
    elif move == "paper" and ai_move == "rock":
        win = "Win"
        wins += 1
    elif move == "paper" and ai_move == "scissors":
        win = "Lose"
        losses += 1
    elif move == "scissors" and ai_move == "rock":
        win = "Lose"
        losses += 1
    elif move == "scissors" and ai_move == "paper":
        win = "Win"
        wins += 1

    i += 1
    print(f"{move} vs {ai_move}: you {win}")
    if i == num_moves:
        go = False

print(f"\nRock Paper Scissors results:\nNumber of rounds: {num_moves}\nNumber of wins against AI: {wins}\nNumber of losses: {losses}\nNumber of ties: {ties}")

