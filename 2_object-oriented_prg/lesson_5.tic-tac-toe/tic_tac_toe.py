
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_state(state):
    for i, c in enumerate(state):
        if ((i+1) % 3) != 0:
            print(f'{c}|', end='')
        else:
            print(c)

# print_state(board)

winner_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def get_winner(state, comb):
    for each in comb:
        if state[each[0]] == state[each[1]] == state[each[2]]:
            if state[each[0]] == 'X' or state[each[0]] == 'O':
                return state[each[0]]
        return None
    
def playgame(board):
    current_sign = 'X'
    get_winner(board, winner_combinations)
    print(get_winner(board, winner_combinations))
    result = False

    while result == False:
        index = int(input(f"Enter your number in range 0-8 for move: "))
        # if state[index] == 'X' or state[index] == 'O':
        #     print("Enter again!")
        board[index] = current_sign
        print(get_winner(board, winner_combinations))
        print_state(board)


        if get_winner(board, winner_combinations) :
            print(f"\nGame has been ended, {current_sign} won! Congratulations!")
            result = True
        
        if current_sign == 'X':
            current_sign = 'O'
        else:
            current_sign = 'X'
        
playgame(board)




# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)                      #Улучшенная версия

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)