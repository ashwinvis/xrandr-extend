#!/usr/bin/env python3
"""
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
"""
import argparse
from ast import literal_eval
from datetime import datetime

from . import cmd, config

COPYING = """
xrandr-extend Copyright (C) 2018-{} Ashwin Vishnu Mohanan
This program comes with ABSOLUTELY NO WARRANTY; This is free software, and you
are welcome to redistribute it under certain conditions. You should have
received a copy of the GNU General Public License (version 3 or later) along
with this program. If not, see <http://www.gnu.org/licenses/>.
""".format(
    datetime.now().year
)

cfg = config.read()

display_res_defaults = cfg["resolutions"]
display_scale_defaults = cfg["scaling"] if cfg.has_section("scaling") else None

# Parse command-line arguments
parser = argparse.ArgumentParser(
    prog="xrandr-extend",
    description="Extend a HIDPI screen to a normal DPI external display",
    epilog=__doc__ + COPYING,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "profile",
    help="Use preset external resolution profiles (available: {}).".format(
        [k for k in display_res_defaults.keys() if k != "primary"]
    ),
)
parser.add_argument(
    "-p",
    "--pri-res",
    help="Modify preset resolution of primary display (default: {})".format(
        display_res_defaults["primary"]
    ),
    nargs=2,
    type=int,
    default=literal_eval(display_res_defaults["primary"]),
)
parser.add_argument(
    "-e",
    "--ext-res",
    help=(
        "Modify preset resolution of external display (default based on "
        "profile)"
    ),
    nargs=2,
    type=int,
    default=None,
)
parser.add_argument(
    "-x",
    "--ext-scale",
    help=(
        "Sets the scale factor of external display (DPI of primary display / "
        "DPI of external display), overriding scale factor estimation from "
        "resolutions"
    ),
    type=float,
    default=None,
)
parser.add_argument(
    "-m", "--mirror", help="Mirror the external display", action="store_true"
)
parser.add_argument(
    "-n",
    "--pan",
    help="Pan the position of external display",
    action="store_true",
)
parser.add_argument(
    "-o",
    "--only",
    help="Extend and use only external display",
    action="store_true",
)
parser.add_argument(
    "-s",
    "--pos",
    help="Set the position of external display explicitly",
    action="store_true",
)
parser.add_argument(
    "-d",
    "--dry-run",
    help="Preview command without executing it",
    action="store_true",
)


def run(args=None):
    args = parser.parse_args(args)
    provider = cmd.detect_provider()
    display_names = config.display_names_from_providers(provider)

    monitor1 = display_names["primary"]
    monitor2 = display_names[args.profile]

    # HIDPI monitor resolution
    A = args.pri_res[0]
    B = args.pri_res[1]

    # External non-HIDPI monitor resolution
    if args.ext_res is None:
        ext_res = display_res_defaults.get(args.profile)
        args.ext_res = literal_eval(ext_res)

    C = args.ext_res[0]
    D = args.ext_res[1]

    # Scaling factor
    if args.ext_scale is None:
        tmp_e = round(A / C, 2)
        tmp_f = round(B / D, 2)
        tmp_max = max(tmp_e, tmp_f)
        if display_scale_defaults is None:
            args.ext_scale = tmp_max
        else:
            args.ext_scale = display_scale_defaults.getfloat(
                args.profile, fallback=tmp_max
            )

    assert args.ext_scale is not None
    E = F = args.ext_scale

    # Prepare commands
    commands = ["xrandr --auto"]
    commands.append("xrandr --listmonitors")
    if args.mirror:
        commands.append("xrandr --output {} --scale {}x{}".format(monitor2, E, F))
    elif args.pan:
        commands.append(
            (
                "xrandr --output {} --auto --output {} --auto --panning "
                "{}x{}+{}+0 --scale {}x{} --right-of {}"
            ).format(
                monitor1, monitor2, int(C * E), int(D * F), A, E, F, monitor1
            )
        )
    elif args.pos:
        commands.append(
            (
                "xrandr --output {} --auto --pos 0x{}  --output {} "
                "--scale {}x{} --auto --pos 0x0 --fb {}x{}"
            ).format(
                monitor1,
                int(D * F),
                monitor2,
                E,
                F,
                int(max(A, C * E)),
                int(B + D * F),
            )
        )
    elif args.only:
        commands.append("xrandr --output {} --off".format(monitor1))
    else:
        commands.append(
            (
                "xrandr --output {} --auto --output {} --auto --scale {}x{} "
                "--right-of {}"
            ).format(monitor1, monitor2, E, F, monitor1)
        )

    if provider == "modesetting" and not (args.mirror or args.only):
        flicker_correction = 0.9999
        commands.append(
            "xrandr --output {0} --scale {1}x{1}".format(
                monitor1, flicker_correction
            )
        )

    list(map(print, commands))
    if not args.dry_run:
        list(map(cmd.call, commands))


if __name__ == "__main__":
    run()
