#! /usr/bin python3

from utils.network import get_default_ip_address

def main():
    """
    Main entry point for the OpenF1 HUD backend application.
    """
    ip_address = get_default_ip_address()

    print(f"Configure your F1 game to send data to {ip_address}.")

if __name__ == "__main__":
    main()
