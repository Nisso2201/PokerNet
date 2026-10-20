import socket
import threading
import tkinter as tk


class PokerClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setup_gui()

    def setup_gui(self):
        self.window = tk.Tk()
        self.window.title("PokerNet - Texas Hold'em")
        self.window.geometry("900x600")

        # Placeholder Label
        self.status_label = tk.Label(self.window, text="Welcome to PokerNet Lobby", font=("Arial", 16))
        self.status_label.pack(pady=20)

    def connect_to_server(self, host='127.0.0.1', port=55555):
        try:
            self.sock.connect((host, port))
            self.status_label.config(text="Connected to Server!")

            # Thread 1: Listen for game updates and incoming voice data
            threading.Thread(target=self.receive_server_data, daemon=True).start()

            # Thread 2: Continuously capture local microphone audio
            threading.Thread(target=self.capture_microphone_stream, daemon=True).start()

        except Exception as e:
            self.status_label.config(text=f"Connection Failed: {e}")

    def receive_server_data(self):
        # Differentiates between JSON text (Game State/AI) and Binary (Voice)
        pass

    def capture_microphone_stream(self):
        # Uses PyAudio to read microphone chunks and send them to the socket
        pass

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = PokerClient()
    # For now, it won't auto-connect until you build the connect button,
    # but the GUI will launch successfully.
    app.run()