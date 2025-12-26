
## This is deterministic NLP, not AI — perfect for Phase 1.

import re

def parse_intent(user_input: str):
    text = user_input.lower().strip()

    # Show interfaces
    if "show" in text and "interface" in text:
        return {
            "tool": "show_interfaces",
            "args": {}
        }

    # Configure interface Gi0/1 with IP 10.1.1.1/24
    match = re.search(
        r"configure interface (\S+) with ip (\S+)",
        text
    )

    if match:
        interface = match.group(1)
        ip_cidr = match.group(2)

        ip, prefix = ip_cidr.split("/")
        mask = cidr_to_mask(int(prefix))

        return {
            "tool": "configure_interface",
            "args": {
                "interface": interface,
                "ip": ip,
                "mask": mask
            }
        }

    return None

def cidr_to_mask(prefix: int) -> str:
    mask = (0xffffffff >> (32 - prefix)) << (32 - prefix)
    return ".".join(str((mask >> i) & 0xff) for i in [24, 16, 8, 0])