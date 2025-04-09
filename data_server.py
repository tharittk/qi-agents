import socket
import pickle
import threading
import struct
import subprocess

from qi.qi_g161_loader import load_g161_wells
from qi.qi_arthit_loader import load_arthit_wells
from qi.qi_bongkot_loader import load_bk_wells


class WellServer:
    def __init__(self, host="localhost", port=9988):
        self.host = host
        self.port = port
        self.data = load_g161_wells() | load_bk_wells() | load_arthit_wells()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_response(self, client_socket, response):
        data = pickle.dumps(response)
        data_size = struct.pack("!I", len(data))
        client_socket.sendall(data_size + data)

    def handle_client(self, client_socket):
        try:
            while True:
                request = client_socket.recv(1024)
                if not request:
                    break
                key = pickle.loads(request)
                print(f"Received query for key: {key}")
                response = self.data.get(key, "Key not found")
                self.send_response(client_socket, response)

        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(4)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def print_available_wells(self):

        for well_name in self.data:
            well = self.data[well_name]
            print(well)
            if well.litho_config == "G161":
                pass
            elif well.litho_config == "Bongkot":
                pass
            elif well.litho_config == "Arthit":
                pass
            else:
                raise (ValueError("Well config is not properly set"))


if __name__ == "__main__":
    server = WellServer()
    server.print_available_wells()
    server.start()
