import os
import sys
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
        config.read(str(CFG_FILE))  # py35
        return config
    else:
        return default_cfg()


def write_defaults():
    config = default_cfg()
    # py35 doesn't support pathlike?
    with open(str(CFG_FILE), "x") as f:
        config.write(f)


def display_names_from_providers(provider):
    # Try to read a section such as:
    # [provider:modesetting]
    config = read()
    if os.getenv("CI"):
        # override provider while testing
        provider = "modesetting"

    section = "provider:{}".format(provider)
    if config.has_section(section):
        display_names = config[section]
    else:
        print(
            (
                "Unknown X server provider. Output of `xrandr --listproviders` was: "
                + provider.strip("\n")
                + "\n"
                + "Hint: perhaps you are using Wayland and not an X server? "
                + "If not simply add a section [{}] in {}".format(
                    section, CFG_FILE
                )
            )
        )
        sys.exit(1)

    return display_names


if __name__ == "__main__":
    print("Writing default configuration to {} ...".format(CFG_FILE))
    write_defaults()
    print("Done!")
