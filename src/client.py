import socket
import pickle

from tic_tac_toe import TicTacToe

server = '127.0.0.1'
port = 13337

# Присоединение к серверу
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))
print(f"\nСоединение с ('{server}', {port})!")

# Создаем объект игры
player_o = TicTacToe("O")

# Параметр отвечающий за перезапук игры
rematch = True

while rematch == True:
    # Заголовок игры 
    print(f"\n\n Крестики - нолики ")

    # Рисуем доску
    player_o.draw_field()

    # Ждем, когда стартанет сервер
    print(f"\nОжидание другого игрока...")
    x_field = s.recv(1024)
    x_field = pickle.loads(x_field)
    player_o.update_field(x_field)

    # Пока никто не выиграл цикл продолжается 
    while player_o.is_win("O") == False and player_o.is_win("X") == False and player_o.is_full() == False:
        
        print(f"\n       Твоя очередь!")
        
        while True:
            player_o.draw_field()
            player_coord = input(f"Введите координату клетки: ")
            if player_o.edit_field(player_coord):
                break
            else:
                print("Вы ввели неверные координаты!")
        
        # Преобразуем данные в бинарный формат и отправляем на сервер-клиент 
        o_field = pickle.dumps(player_o.field)
        s.send(o_field)

        # Если игрок сделал ход и выиграл, то останавливаем игру  
        if player_o.is_win("O") == True or player_o.is_full() == True:
            break

        # Ждем ход другого игрока
        print(f"\nОжидание другого игрока...")
        x_field = s.recv(1024)
        x_field = pickle.loads(x_field)
        player_o.update_field(x_field)

    if player_o.is_win("O") == True:
        print(f"Поздравляю, Вы выиграли!")
    elif player_o.is_full() == True:
        print(f"Ничья, поле заполнено!")
    else:
        print(f"К сожалению, Вы проиграли!")

    # Ждем ответ от сервера, хочет ли он начать игру заново 
    print(f"\nОжидание другого игрока...")
    server_response = s.recv(1024)
    server_response = pickle.loads(server_response)
    client_response = "N"

    # Если сервер предлагает начать игру заново, то спрашиваем у клиента, хочет ли он продолжить игру 
    if server_response == "Y":
        print(f"\nСоперник хочет начать новую игру!")
        client_response = input("Хотите начать игру заново? (Y/N): ")[0]
        client_response = client_response.capitalize()
        temp_client_resp = client_response
        
        client_response = pickle.dumps(client_response)
        s.send(client_response)

        if temp_client_resp == "Y":
            player_o.restart()

        else:
            rematch = False
 
    else:
        print(f"\nСоперник отказался от новой игры")
        rematch = False

spacer = input(f"\nНажмите любую клавишу, чтобы завершить игру...\n")

s.close()