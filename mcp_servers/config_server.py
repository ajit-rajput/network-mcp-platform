from mcp_servers.config_impl import configure_interface

def configure_interface_tool(interface: str, ip: str, mask: str):
    """
    MCP Tool: configure_interface
    """
    return configure_interface(interface, ip, mask)