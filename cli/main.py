from rich.console import Console
from mcp_servers.tool_registry import ToolRegistry
from mcp_servers.monitoring_server import show_interfaces
from mcp_servers.config_server import configure_interface_tool
from utils.intent_parser import parse_intent

console = Console()

def main():
    console.print("[bold cyan]Network MCP Platform (Phase 1)[/bold cyan]")
    console.print(
        "Try:\n"
        "  show interfaces\n"
        "  configure interface GigabitEthernet0/1 with ip 10.1.1.1/24\n"
        "  exit\n"
    )

    registry = ToolRegistry()

    registry.register(
        name="show_interfaces",
        func=show_interfaces,
        description="Show interface status"
    )

    registry.register(
        name="configure_interface",
        func=configure_interface_tool,
        description="Configure interface IP address"
    )

    while True:
        user_input = console.input("[bold green]> [/bold green]").strip()

        if user_input.lower() in ("exit", "quit"):
            break

        intent = parse_intent(user_input)

        if not intent:
            console.print("[red]Could not understand intent[/red]")
            continue

        try:
            result = registry.execute(
                intent["tool"],
                **intent["args"]
            )

            console.print("[green]Result:[/green]", result)

        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")

if __name__ == "__main__":
    main()
    ## python -m cli.main
    ## Try "configure interface GigabitEthernet0/1 with ip 10.1.1.1/24"