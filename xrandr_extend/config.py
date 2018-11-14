from pathlib import Path
from configparser import ConfigParser


# Default configuration file
DEFAULT_CFG_FILE = Path(__file__).parent / "default.cfg"

# User-configuration file
CFG_FILE = Path.home() / ".config" / "xrandr-extend.cfg"


def default_cfg():
    config = ConfigParser()
    config.read(str(DEFAULT_CFG_FILE))

    return config


def read():
    if CFG_FILE.exists():
        config = default_cfg()
        config.read(str(CFG_FILE))
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
