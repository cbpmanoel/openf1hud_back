from pyroute2 import IPRoute
import socket
import asyncio


def _get_default_ip_address_blocking() -> str:
    """
    Get the default IP address of the machine.

    Returns:
        str: The default IP address.
    """
    ipr = IPRoute()
    default_routes = ipr.get_default_routes(family=socket.AF_INET)
    if not default_routes:
        raise RuntimeError("No default route found")
    
    pref_route = default_routes[0].get_attr('RTA_PREFSRC')
    if not pref_route:
        raise RuntimeError("No preferred source address found for default route")
    
    return pref_route


async def get_default_ip_address() -> str:
    """
    Asynchronously get the default IP address of the machine.
    This function is a workaround for uvloop not supporting AF_NETLINK, used by pyroute2,
    so it runs the blocking version in a separate thread.
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, _get_default_ip_address_blocking)