import os
import json
from typing import Dict, Any

class ConfigHandler:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self._load_config()

    def _load_config(self) -> None:
        """Load configuration from the config file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(
                f"Config file not found at {self.config_path}. "
                "Please create a config.json file with your API keys."
            )
        
        try:
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in config file: {self.config_path}")

    def get_api_key(self, key_name: str) -> str:
        """Get an API key from the configuration."""
        if key_name not in self.config:
            raise KeyError(f"API key '{key_name}' not found in config file")
        return self.config[key_name]

    def get_config_value(self, key: str, default: Any = None) -> Any:
        """Get a configuration value with an optional default."""
        return self.config.get(key, default) 