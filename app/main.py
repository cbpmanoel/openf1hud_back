#! /usr/bin python3

from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from utils.network import get_default_ip_address
from telemetry_ingestor.listener import TelemetryListener, F1_TELEMETRY_PORT
from telemetry_ingestor.service import process_telemetry_data


listener = TelemetryListener(data_callback=process_telemetry_data)


def print_startup_message(host_ip: str):
    print(f"""
Starting telemetry listener on {host_ip}:{F1_TELEMETRY_PORT}.
Please ensure F1 2025 is configured to send telemetry data to this address.
""")
    
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.
    Starts the telemetry listener on startup and stops it on shutdown.
    """
    
    host_ip = await get_default_ip_address()
    print_startup_message(host_ip)
    try:
        await listener.start()
        yield
    except Exception as e:
        print(f"Error in lifespan context manager: {e}")
    finally:
        await listener.stop()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "F1 2025 Telemetry Ingestor is running."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)