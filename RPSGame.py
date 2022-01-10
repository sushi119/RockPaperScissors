def rps_game(rounds):
  '''
  Purpose: Plays multiple rounds of Rock-Paper-Scissors
  Input Parameter(s):
    rounds - an integer representing the number of rounds to play
  Return Value: A dictionary representing the computer's win differential for each of the three possible choices
  '''
  win_diff = {'R':0, 'S':0, 'P':0}
  i = 0
  while i < rounds:
    player_choice = user_turn()
    print(player_choice)
    computer_choice = computer_turn(win_diff)
    print(computer_choice)
    if player_choice == computer_choice:
      print('Tie!')
    if player_choice == 'R':
      if computer_choice == 'S':
        print('Player wins!')
        win_diff['S'] -= 1
      if computer_choice == 'P':
        print('Computer wins!')
        win_diff['P'] += 1
    if player_choice == 'S':
      if computer_choice == 'R':
        print('Computer wins!')
        win_diff['R'] += 1
      if computer_choice == 'P':
        print('Player wins!')
        win_diff['P'] -= 1
    if player_choice == 'P':
      if computer_choice == 'R':
        print('Player wins!')
        win_diff['R'] -= 1
      if computer_choice == 'S':
        print('Computer wins!')
        win_diff['S'] += 1
    print(win_diff)
    i += 1
  return win_diff
    #TODO: Finish this function and write at least two helper functions

def user_turn():
  '''
  Purpose: for the user to choose rock, paper, or scissors
  Input Parameter(s): This function takes in no arguments
  Return Value: A print statement with what the user chose followed by a return statement with the choice
  '''
  player_pick = ''
  while player_pick != 'R' and player_pick != 'P' and player_pick != 'S':
    player_pick = input('Enter R, P, or S: ')
    if player_pick != 'R' and player_pick != 'P' and player_pick != 'S':
      print('Invalid input, try again')
  print('Player selects ', player_pick)
  return player_pick



def computer_turn(win_diff):
  '''
  Purpose: to determine the computer's choice in a game of rock, paper, or scissors
  Input Parameter(s): win_diff: the dictionary with the win differential for the rock, paper and Scissors
  Return Value: A print statement with what the computer chose followed by a return statement with the choice
  '''
  if win_diff['R'] >= win_diff['S'] and win_diff['S'] >= win_diff['P']:
    computer_pick = 'R'
  if win_diff['R'] < win_diff['S'] and win_diff['S'] >= win_diff['P']:
    computer_pick = 'S'
  if win_diff['P'] > win_diff['R'] and win_diff['P'] > win_diff['S']:
    computer_pick = 'P'
  print('computer selects ', computer_pick)
  return computer_pick
  
if __name__ == '__main__':

    #TODO: Write test cases for your Problem A Helper functions here
    #Make sure you include Expected Return and Input Sequence (if applicable)

    #Input sequence: S
    #Expected Return: {'R': 1, 'S': 0, 'P': 0}
    print(rps_game(1))

    #Input sequence: Scissors, P, r, 4, P, P
    #Expected Return: {'R': -1, 'S': 2, 'P': 0}
    print(rps_game(3))

    #Input sequence: R, P, P, R, R, S, P, P, P, S
    #Expected Return: {'R': -2, 'S': 1, 'P': -1}
    print(rps_game(10))
