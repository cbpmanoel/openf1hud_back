from pyroute2 import IPRoute
import socket

def get_default_ip_address() -> str:
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
