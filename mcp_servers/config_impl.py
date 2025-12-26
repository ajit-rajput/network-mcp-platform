import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PLAYBOOK = (
    BASE_DIR
    / "automation"
    / "ansible"
    / "playbooks"
    / "interface_config.yaml"
)

INVENTORY = (
    BASE_DIR
    / "automation"
    / "ansible"
    / "inventory"
    / "hosts.yaml"
)

def configure_interface(interface: str, ip: str, mask: str):
    cmd = [
        "ansible-playbook",
        "-i",
        str(INVENTORY),
        str(PLAYBOOK),
        "--extra-vars",
        f"interface_name={interface} interface_ip={ip} interface_mask={mask}"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return {
        "interface": interface,
        "ip": ip,
        "mask": mask,
        "status": "configuration rendered"
    }