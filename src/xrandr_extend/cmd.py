"""Any function which executes a subprocess goes here."""

import subprocess
from shlex import split


def call(cmd):
    """Call a shell command

    Parameters
    ----------

    cmd : str

    """
    cmd = split(cmd)
    subprocess.call(cmd)


def detect_provider():
    output = subprocess.check_output(split("xrandr --listproviders")).decode(
        "utf8"
    )
    # Find index of sub-string "name:" in the output
    idx_name = output.rfind("name:")
    # Configuration
    if idx_name == -1:
        provider = None
    else:
        # idx_name + 5 to remove "name:"
        provider = output.lower().rstrip("\n")[idx_name + 5 :]
    return provider
