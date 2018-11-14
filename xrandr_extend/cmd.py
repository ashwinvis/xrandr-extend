"""Any function which executes a subprocess goes here."""

import subprocess
import sys
from shlex import split
from .config import read, CFG_FILE


def call(cmd):
    """Call a shell command

    Parameters
    ----------

    cmd : str

    """
    cmd = split(cmd)
    subprocess.call(cmd)


def display_names_from_providers():
    output = subprocess.check_output(split("xrandr --listproviders")).decode(
        "utf8"
    )
    # Configuration
    config = read()
    provider = output.lower().rstrip("\n").split(":")[-1]

    # Try to read a section such as:
    # [provider:modesetting]
    section = "provider:{}".format(provider)
    if config.has_section(section):
        display_names = config[section]
    else:
        print(
            (
                "Unknown X server provider. Output of `xrandr --listproviders` was:\n"
                + output
                + "Hint: perhaps you are using Wayland and not an X server? "
                + "If not simply add a section [{}] in {}".format(
                    section, CFG_FILE
                )
            )
        )
        sys.exit(1)

    return display_names
