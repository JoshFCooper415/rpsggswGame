import socket
import threading
from ip import NetworkConfig
# Basic game logic for the expanded version of Rock, Paper, Scissors
def game_logic(player1_choice, player2_choice):
    # Define the choices and their relationships
    win_map = {
        "Rock": ["Scissors", "Gun"],
        "Paper": ["Rock", "Steamroller"],
        "Scissors": ["Paper", "Wo Chien"],
        "Gun": ["Rock", "Scissors"],
        "Goku": ["Rock", "Paper", "Scissors", "Gun", "Steamroller"],
        "Steamroller": ["Scissors", "Paper", "Rock"],
        "Wo Chien": ["Scissors", "Paper"]
    }

    if player1_choice == player2_choice:
        return "It's a tie!"
    elif player2_choice in win_map[player1_choice]:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def server_program():
    host = NetworkConfig
    port = NetworkConfig

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        player2_choice = conn.recv(1024).decode()
        if not player2_choice:
            break
        print("Player 2's choice: " + player2_choice)
        
        player1_choice = input("Player 1, enter your choice: ")
        conn.send(player1_choice.encode())

        result = game_logic(player1_choice, player2_choice)
        print("Result: " + result)

    conn.close()

def client_program():
    host = NetworkConfig.host
    port = NetworkConfig.port

    client_socket = socket.socket()
    client_socket.connect((host, port))

    player2_choice = input("Player 2, enter your choice: ")
    client_socket.send(player2_choice.encode())
    player1_choice = client_socket.recv(1024).decode()

    print("Player 1's choice: " + player1_choice)
    result = game_logic(player1_choice, player2_choice)
    print("Result: " + result)

    client_socket.close()

if __name__ == '__main__':
    choice = input("Do you want to be Player 1 (server) or Player 2 (client)? Enter 1 or 2: ")
    if choice == '1':
        server_program()
    elif choice == '2':
        client_program()
    else:
        print("Invalid selection. Please restart and choose either 1 or 2.")
