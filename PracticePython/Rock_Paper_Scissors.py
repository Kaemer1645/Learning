print('This is Rock Paper Scissors game')
new_game = 'Yes'

while new_game == 'Yes':

    player_1 = input('Player_1 --- Write Rock, Paper or Scissors ')
    player_2 = input('Player_2 --- Write Rock, Paper or Scissors ')
    player_1_points = 0
    player_2_points = 0

    if player_1 == 'Rock' and player_2 == 'Paper':
        player_2_points += 1
    elif player_1 == 'Rock' and player_2 == 'Scissors':
        player_1_points += 1
    elif player_1 == 'Scissors' and player_2 == 'Paper':
        player_1_points += 1
    elif player_1 == 'Scissors' and player_2 == 'Rock':
        player_2_points += 1
    elif player_1 == 'Paper' and player_2 == 'Rock':
        player_1_points += 1
    elif player_1 == 'Paper' and player_2 == 'Scissors':
        player_2_points += 1
    else:
        player_2_points += 1
        player_1_points += 1

    if player_1_points > player_2_points:
        print('Player 1 WIN!!!')
    elif player_1_points == player_2_points:
        print('This is a tie')
    else:
        print('Player 2 WIN!!!')
    new_game = input('Write "Yes" to continue game or click Enter')