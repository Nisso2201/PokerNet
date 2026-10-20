import socket
import threading

class GameRoom:
    def __init__(self, room_id):
        self.room_id = room_id
        self.players = []
        self.is_active = True
        print(f"Room {self.room_id} created.")

    def broadcast_game_state(self, message):
        # Sends card and pot updates to everyone in this specific room
        pass

    def route_voice_chat(self, audio_bytes, sender_socket):
        # Sends real-time audio bytes to everyone EXCEPT the sender
        pass

    def request_ai_analysis(self, game_history):
        # Background thread to ping the GenAI API for coaching
        pass

class PokerServer:
    def __init__(self, host='127.0.0.1', port=55555):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.rooms = {}  # Dictionary to manage multiple active rooms
        print(f"PokerNet Multi-Room Server started on {host}:{port}")

    def accept_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"New connection from {address}")
            # Spawn a new thread immediately for the lobby routing
            threading.Thread(target=self.handle_lobby, args=(client_socket,), daemon=True).start()

    def handle_lobby(self, client_socket):
        # Logic to ask the user for a username and assign them to a GameRoom
        pass

if __name__ == "__main__":
    server = PokerServer()
    server.accept_connections()