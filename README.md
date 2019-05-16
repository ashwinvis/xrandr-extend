xrandr-extend
=============


[![image](https://img.shields.io/pypi/v/xrandr_extend.svg)](https://pypi.python.org/pypi/xrandr_extend)
![python versions](https://img.shields.io/pypi/pyversions/xrandr-extend.svg)
[![image](https://img.shields.io/travis/ashwinvis/xrandr-extend.svg)](https://travis-ci.org/ashwinvis/xrandr-extend)
[![Documentation Status](https://readthedocs.org/projects/xrandr-extend/badge/?version=latest)](https://xrandr-extend.readthedocs.io/en/latest/?badge=latest)

Extend a HIDPI screen to a normal DPI external display. This command line tool
implements various solutions described in the [HIDPI Arch Linux wiki
page](https://wiki.archlinux.org/index.php/HiDPI#Multiple_displays).

* Free software: GNU General Public License v3

* Documentation: https://xrandr-extend.readthedocs.io.

## Installation

```sh
pip install xrandr-extend --user
```
or alternatively

```sh
pip install -e "git+https://github.com/ashwinvis/xrandr-extend.git#egg=xrandr_extend" --user
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
primary = (3200, 1800)
hdmi = (1920, 1080)
vga = (1920, 1200)

```

The first few sections have the name in the format `[provider:display_driver]`.
Run `xrandr --listproviders` to find what your system has. The values in this
section should be given as `alias = monitor_name`, as in the output of
`xrandr --listmonitors` command. You may even remove existing sections and 
add more sections for your *display driver*.

Each line in the `[resolutions]` section signifies a *resolution profile* in
the format `alias = [width_in_pixels, height_in_pixels]`.  The *profile*
`primary` should contain the resolution of your built-in display.  You may edit
or remove the remaining values `hdmi` and `vga`.

## Quick reference

```console
usage: xrandr-extend [-h] [-p PRI_RES PRI_RES] [-e EXT_RES EXT_RES] [-m] [-n]
                     [-o] [-s] [-d]
                     profile

Extend a HIDPI screen to a normal DPI external display

positional arguments:
  profile               Use preset external resolution profiles (available:
                        ['hdmi', 'vga']).

optional arguments:
  -h, --help            show this help message and exit
  -p PRI_RES PRI_RES, --pri-res PRI_RES PRI_RES
                        Modify preset resolution of primary display (default
                        [3200, 1800])
  -e EXT_RES EXT_RES, --ext-res EXT_RES EXT_RES
                        Modify preset resolution of ext. display (default
                        based on profile)
  -m, --mirror          Mirror the ext. display
  -n, --pan             pan the position of ext. display
  -o, --only            extend and use only ext. display
  -s, --pos             set the position of ext. display explicitly
  -d, --dry-run         Preview command without executing it

Examples
--------
# Default option requires only the scaling factors and display name
$ xrandr-extend --dry-run vga
$ xrandr-extend vga
$ xrandr-extend hdmi

# Other options to extend the display
$ xrandr-extend --pan hdmi
$ xrandr-extend --only hdmi
$ xrandr-extend -e 1024 768 -n vga  # Pan with custom external resolution
```

# Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[ashwinvis/cookiecutter-pypackage](https://github.com/ashwinvis/cookiecutter-pypackage)
project template.
