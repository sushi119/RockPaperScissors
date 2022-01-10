# RockPaperScissors
Created a rock, paper, scissors game via Python versus the computer

Files include: RPSGame.py

Three different functions: rps_game(rounds), user_turn(), computer_turn(win_diff)

rps_game(rounds): Purpose: Plays multiple rounds of Rock-Paper-Scissors
  Input Parameter(s):rounds - an integer representing the number of rounds to play, this is determined in the test case
  Return Value: A dictionary representing the computer's win differential for each of the three possible choices

user_turn(): Purpose: for the user to choose rock, paper, or scissors
  Input Parameter(s): This function takes in no arguments
  Return Value: A print statement with what the user chose followed by a return statement with the choice

computer_turn(win_diff): Purpose: to determine the computer's choice in a game of rock, paper, or scissors
  Input Parameter(s): win_diff: the dictionary with the win differential for the rock, paper and Scissors
  Return Value: A print statement with what the computer chose followed by a return statement with the choice

In order to run the RPSGame program via terminal compile file by:
"python3 RPSGame.py" 

The program will then ask you to enter a letter:
"R", for Rock
"P", for paper
"S", for scissors

The program will then print the user's pick as well as the computer's pick
It then prints whether the user won, the computer won, or it was tie
It lastly prints the computer's win differential for either choosing rock, paper or scissors
The game continues until the number of rounds selected have been played

Enjoy!
