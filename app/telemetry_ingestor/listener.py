import asyncio
import socket
from typing import Callable, Coroutine

#TODO: Implement proper logging and error handlings

F1_TELEMETRY_PORT = 20777
F1_TELEMETRY_HOST = ''


class TelemetryListener:

    def __init__(self, port: int = F1_TELEMETRY_PORT, host: str = F1_TELEMETRY_HOST, data_callback: Callable = None):
        self._port = port
        self._host = host
        self._task = None
        self._data_callback = data_callback

    async def _listener_routine(self):
        """
        Main routine for listening to incoming telemetry data.
        
        It creates a UDP endpoint and waits for incoming data,
        passing received data to the provided callback function.
        """
        try:
            loop = asyncio.get_running_loop()
            
            # Manually creates the socket so we can use SO_REUSEADDR
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setblocking(False)
            sock.bind((self._host, self._port))
            
            transport, _ = await loop.create_datagram_endpoint(
                lambda: UDPProtocol(self._data_callback),
                sock=sock
            )

            print(f"Telemetry Listener started on {self._host}:{self._port}")
            await asyncio.Future()  # Run until cancelled
        except asyncio.CancelledError:
            print("Telemetry Listener routine cancelled.")
        finally:
            print("Closing Telemetry Listener transport.")
            transport.close()

    async def start(self):
        """
        Start the telemetry listener.
        """
        if self._task is None or self._task.done():
            print("Starting Telemetry Listener...")
            self._task = asyncio.create_task(self._listener_routine())

    async def stop(self):
        """
        Stop the telemetry listener.
        """
        if self._task and not self._task.done():
            print("Stopping Telemetry Listener...")
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            finally:
                print("Telemetry Listener stopped.")
                self._task = None


class UDPProtocol(asyncio.DatagramProtocol):
    """
    Helper class for asyncio UDP protocol handling.
    """

    def __init__(self, data_callback: Callable[[bytes], Coroutine]):
        self.data_callback = data_callback

    def datagram_received(self, data: bytes, addr):
        print(f"Data received from {addr}, length: {len(data)} bytes")
        asyncio.create_task(self.data_callback(data))

    def error_received(self, exc):
        print(f"Error received: {exc}")

    def connection_lost(self, exc):
        print(f"Connection lost: {exc}")
