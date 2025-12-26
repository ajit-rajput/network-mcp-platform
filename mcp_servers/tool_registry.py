from typing import Callable, Dict

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable, description: str):
        self._tools[name] = {
            "func": func,
            "description": description,
        }

    def list_tools(self):
        return {
            name: meta["description"]
            for name, meta in self._tools.items()
        }

    def execute(self, name: str, **kwargs):
        if name not in self._tools:
            raise ValueError(f"Tool '{name}' not found")

        return self._tools[name]["func"](**kwargs)