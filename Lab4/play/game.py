def match(player, cpu):
    if player == cpu:
        return 'draw'
    elif (player == 'rock' and cpu == 'scissors') or (player == 'scissors' and cpu == 'paper') or (player == 'paper' and cpu == 'rock'):
        return 'player won'
    else:
        return 'cpu won'
