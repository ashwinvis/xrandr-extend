import os
from pkg_resources import parse_version
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the relevant file
with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

lines = long_description.splitlines(True)
long_description = "".join(lines[1:])

__version__ = "0.0.1"

# Get the development status from the version string
parsed_version = parse_version(__version__)
try:
    if parsed_version.is_prerelease:
        if "a" in __version__:
            devstatus = "Development Status :: 3 - Alpha"
        else:
            devstatus = "Development Status :: 4 - Beta"
    else:
        devstatus = "Development Status :: 5 - Production/Stable"
except AttributeError:
    if "a" in __version__:
        devstatus = "Development Status :: 3 - Alpha"
    elif "b" in __version__:
        devstatus = "Development Status :: 4 - Beta"
    else:
        devstatus = "Development Status :: 5 - Production/Stable"

install_requires = []
scripts = ["xrandr-extend"]

setup(
    name="xrandr-extend",
    version=__version__,
    description=("Extend a HIDPI screen to a normal DPI external display"),
    long_description=long_description,
    keywords="xrandr, hidpi, linux, external monitor",
    author="Ashwin Vishnu Mohanan",
    author_email="ashwinvis+gh@pm.me",
    url="https://github.org/ashwinvis/xrandr-extend",
    license="GPL",
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        devstatus,
        "Intended Audience :: End Users/Desktop",
        "Topic :: Desktop Environment",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # Specify the Python versions you support here. In particular,
        # ensure that you indicate whether you support Python 2,
        # Python 3 or both.
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    install_requires=install_requires,
    scripts=scripts,
)
