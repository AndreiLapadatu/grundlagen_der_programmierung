from aestethic_ex3.menu_ex3 import player, robot
from play.game import match


def main():
    player_cnt = 0
    cpu_cnt = 0

    while (player_cnt != 3) and (cpu_cnt != 3):
        cpu = robot()
        user = player()
        result = match(user, cpu)

        if result == 'draw':
            print('Draw')
        if result == 'player won':
            player_cnt += 1
            print(f'You won! Your points: {player_cnt}')
        if result == 'cpu won':
            cpu_cnt += 1
            print(f'Computer won:( Computer points {cpu_cnt}')

    if player_cnt > cpu_cnt:
        print('Congrats, You won!')
    if player_cnt < cpu_cnt:
        print('Yoy lost,try again')


main()
