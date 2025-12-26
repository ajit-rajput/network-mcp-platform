import json
from pathlib import Path

MOCK_PATH = Path("validation/genie/mock_data/R1/show_ip_interface_brief.parsed")

def get_interfaces():
    with open(MOCK_PATH) as f:
        data = json.load(f)

    interfaces = []
    for name, details in data["interface"].items():
        interfaces.append(
            {
                "name": name,
                "ip": details["ip_address"],
                "status": details["status"],
                "protocol": details["protocol"],
            }
        )
    return interfaces
