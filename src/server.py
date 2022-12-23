import socket
import pickle

from tic_tac_toe import TicTacToe

server = '127.0.0.1' 
port = 13337

# Запускаем сервер на прослушивание
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(5)

# Устанавливаем соединение с клиентом-клиентом
client_socket, client_address = s.accept()
print(f"\nСоединение с {client_address}!")

player_x = TicTacToe("X")

# Разрешаем перезапуск игры
rematch = True

while rematch == True:
    print(f"\n\n Крестики - нолики ")

    # Основной цикл игры
    while player_x.is_win("X") == False and player_x.is_win("O") == False and player_x.is_full() == False:

        print(f"\n       Твоя очередь!")
        
        while True:
            player_x.draw_field()
            player_coord = input(f"Введите координату клетки: ")
            if player_x.edit_field(player_coord):
                break
            else:
                print("Вы ввели неверные координаты!")

        x_field = pickle.dumps(player_x.field)
        client_socket.send(x_field)

        if player_x.is_win("X") == True or player_x.is_full() == True:
            break

        print(f"\nОжидание ответа от другого игрока...")
        o_field = client_socket.recv(1024)
        o_field = pickle.loads(o_field)
        player_x.update_field(o_field)

    if player_x.is_win("X") == True:
        print(f"Поздравляю, Вы выиграли!")
    elif player_x.is_full() == True:
        print(f"Ничья, поле заполнено!")
    else:
        print(f"К сожалению, Вы проиграли!")

    server_response = input(f"\nХотите начать игру заново? (Y/N): ")[0]
    server_response = server_response.capitalize()
    temp_server_resp = server_response
    client_response = ""

    server_response = pickle.dumps(server_response)
    client_socket.send(server_response)

    if temp_server_resp == "Y":
        print(f"Ожидание ответа от другого игрока...")
        client_response = client_socket.recv(1024)
        client_response = pickle.loads(client_response)

        if client_response != "Y":
            print(f"\nСоперник отказался от новой игры")
            rematch = False
        else:
            print(f"\nСоперник хочет начать новую игру!")
            player_x.restart()
    else:
        rematch = False

spacer = input(f"\nНажмите любую клавишу, чтобы завершить игру...\n")

client_socket.close()
s.close()