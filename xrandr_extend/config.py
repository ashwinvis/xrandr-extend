from pathlib import Path
from configparser import ConfigParser
import pkg_resources


# Default configuration file
DEFAULT_CFG_FILE = pkg_resources.resource_filename(__name__, "default.cfg")

# User-configuration file
CFG_FILE = Path.home() / ".config" / "xrandr-extend.cfg"


def default_cfg():
    config = ConfigParser()
    config.read(DEFAULT_CFG_FILE)

    return config


def read():
    if CFG_FILE.exists():
        config = default_cfg()
        config.read(CFG_FILE)
        return config
    else:
        return default_cfg()


def write_defaults():
    config = default_cfg()
    with open(CFG_FILE, "x") as f:
        config.write(f)


if __name__ == "__main__":
    print("Writing default configuration to {} ...".format(CFG_FILE))
    write_defaults()
    print("Done!")
