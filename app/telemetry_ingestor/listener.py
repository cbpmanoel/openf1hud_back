import socket
from threading import Thread, Event
from typing import Callable

#TODO: Implement proper logging and error handlings

F1_TELEMETRY_PORT = 20777
F1_TELEMETRY_HOST = ''

SOCKET_TIMEOUT = 0.1
SOCKET_BUFFER_SIZE = 1024

class TelemetryListener:
    def __init__(self,
                 port: int = F1_TELEMETRY_PORT,
                 host: str = F1_TELEMETRY_HOST,
                 data_callback: Callable = None):
        self._port = port
        self._host = host
        self._socket = None
        self._thread = None
        self._stop_event = Event()
        self._data_callback = data_callback
            
    def _initialize_socket(self):
        try:
            if self._socket:
                self._socket.close()
            
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._socket.bind((self._host, self._port))
            self._socket.settimeout(SOCKET_TIMEOUT)
            print(f"Socket initialized on {self._host}:{self._port}")
            
        except socket.error as e:
            print(f"Socket error: {e}")
            self._socket = None
        
    def _initialize_thread(self):
        if self._thread is None or not self._thread.is_alive():
            self._stop_event.clear()
            self._thread = Thread(target=self._listener_routine, daemon=True)

    def _listener_routine(self):
        while not self._stop_event.is_set():
            if self._socket is None:
                print("Socket is not initialized.")
                self._stop_event.set()
                continue
            
            try:
                data, _ = self._socket.recvfrom(SOCKET_BUFFER_SIZE)
                
                try:
                    if self._data_callback:
                        self._data_callback(data)
                except Exception as e:
                    print(f"Data callback error: {e}")
                    continue
                    
            except socket.timeout:
                continue

        if self._socket:
            self._socket.close()

    def start(self):
        self._initialize_socket()
        if self._socket:
            self._initialize_thread()
            self._thread.start()

    def stop(self):
        self._stop_event.set()
        
    def is_running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

