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


def detect_provider():
    output = subprocess.check_output(split("xrandr --listproviders")).decode(
        "utf8"
    )
    # Configuration
    provider = output.lower().rstrip("\n").split(":")[-1]
    return provider
