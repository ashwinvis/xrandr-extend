#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `xrandr_extend` package."""

import pytest
from contextlib import suppress
from shlex import split
from pathlib import Path
from tempfile import gettempdir
import os

from xrandr_extend import main, config


if os.getenv("CI"):
    to_test = ["-h"]
else:
    to_test = [
        "-h",
        "--dry-run vga",
        "--dry-run hdmi",
        "-d --pan vga",
        "-d --mirror vga",
        "-d --only vga",
    ]


@pytest.mark.parametrize("args", to_test)
def test_command_line_interface(args):
    """Test the CLI."""
    with suppress(SystemExit):
        main.run(split(args))


def test_write_config():
    config.CFG_FILE = Path(gettempdir()) / "xrandr-extend.cfg"
    if config.CFG_FILE.exists():
        with suppress(FileExistsError):
            config.write_defaults()
    else:
        config.write_defaults()
    config.read()
    config.CFG_FILE.unlink()  # remove
