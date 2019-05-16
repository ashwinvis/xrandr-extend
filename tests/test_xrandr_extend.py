#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `xrandr_extend` package."""

import pytest
from contextlib import suppress
from shlex import split
from xrandr_extend.main import run


def test_command_line_interface(args="-h"):
    """Test the CLI."""
    with suppress(SystemExit):
        run(split(args))
