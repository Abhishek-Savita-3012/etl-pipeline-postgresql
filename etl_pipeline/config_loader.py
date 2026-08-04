from pathlib import Path

import yaml


CONFIG_FILE = (
    Path(__file__).resolve().parent.parent
    / "config"
    / "config.yaml"
)


def load_config():
    """
    Load project configuration from YAML.
    """

    with open(CONFIG_FILE, "r") as file:
        return yaml.safe_load(file)


config = load_config()