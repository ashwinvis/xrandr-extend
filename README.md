xrandr-extend
=============


[![image](https://img.shields.io/pypi/v/xrandr_extend.svg)](https://pypi.python.org/pypi/xrandr_extend)
![python versions](https://img.shields.io/pypi/pyversions/xrandr-extend.svg)
[![image](https://img.shields.io/travis/ashwinvis/xrandr-extend.svg)](https://travis-ci.org/ashwinvis/xrandr-extend)

Extend a HIDPI screen to a normal DPI external display. This command line tool
implements various solutions described in the [HIDPI Arch Linux wiki
page](https://wiki.archlinux.org/index.php/HiDPI#Multiple_displays).

* Free software: GNU General Public License v3

[![asciicast](https://asciinema.org/a/mauTEQ1eHLajl2TiF0ZEH5k3X.svg)](https://asciinema.org/a/mauTEQ1eHLajl2TiF0ZEH5k3X)

## Installation

```sh
pip install xrandr-extend --user
```

or alternatively use [pipx](https://pipxproject.github.io/pipx/docs/):

```sh
pipx install xrandr-extend
```

## Configuration
```sh
python -m xrandr_extend.config
```
This creates a file `~/.config/xrandr-extend.cfg` which looks like this:

```ini
[provider:modesetting]
primary = eDP-1
hdmi = HDMI-1
vga = DP-1

[provider:intel]
primary = eDP1
hdmi = HDMI1
vga = DP1

[resolutions]
primary = 3200, 1800
hdmi = 1920, 1080
vga = 1920, 1200

# [scaling]
# primary = 1.0
# hdmi = 2.0
# vga = 2.0
```

The first few sections have the name in the format `[provider:display_driver]`.
Run `xrandr --listproviders` to find what your system has. The values in this
section should be given as `profile = monitor_name`, as in the output of
`xrandr --listmonitors` command. You may even remove existing sections and
add more sections for your *display driver*.

Each line in the `[resolutions]` section signifies a *resolution profile* in
the format `profile = [width_in_pixels, height_in_pixels]`.  The *profile*
`primary` should contain the resolution of your built-in display.  You may edit
or remove the remaining values `hdmi` and `vga`.

The `[scaling]` section contains the scale factors, which if uncommented,
overrides the scale factor computed from the resolutions.

## Quick reference

```console
usage: xrandr-extend [-h] [-p PRI_RES PRI_RES] [-e EXT_RES EXT_RES]
                     [-x EXT_SCALE] [-m] [-n] [-o] [-s] [-d]
                     profile

Extend a HIDPI screen to a normal DPI external display

positional arguments:
  profile               Use preset external resolution profiles (available:
                        ['hdmi', 'vga']).

optional arguments:
  -h, --help            show this help message and exit
  -p PRI_RES PRI_RES, --pri-res PRI_RES PRI_RES
                        Modify preset resolution of primary display (default:
                        3200, 1800)
  -e EXT_RES EXT_RES, --ext-res EXT_RES EXT_RES
                        Modify preset resolution of external display (default
                        based on profile)
  -x EXT_SCALE, --ext-scale EXT_SCALE
                        Sets the scale factor of external display (DPI of
                        primary display / DPI of external display), overriding
                        scale factor estimation from resolutions
  -m, --mirror          Mirror the external display
  -n, --pan             Pan the position of external display
  -o, --only            Extend and use only external display
  -s, --pos             Set the position of external display explicitly
  -d, --dry-run         Preview command without executing it

Examples
--------
# Built-in options or user-configured options are used when only the display
# profile is mentioned

$ xrandr-extend --dry-run vga
$ xrandr-extend vga
$ xrandr-extend hdmi

# Other options to extend the display

$ xrandr-extend --pan hdmi
$ xrandr-extend --only hdmi
$ xrandr-extend -e 1024 768 -n vga  # Pan with custom external resolution
$ xrandr-extend -x 2.0 hdmi         # Custom scale factor
```

# Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[ashwinvis/cookiecutter-pypackage](https://github.com/ashwinvis/cookiecutter-pypackage)
project template.
