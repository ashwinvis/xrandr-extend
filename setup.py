import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the relevant file
with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

lines = long_description.splitlines(True)
long_description = "".join(lines[1:])

__version__ = "0.0.3"

console_scripts = [
    "xrandr-extend = xrandr_extend.main:run"
]

package_data={
    "xrandr_extend": ["default.cfg"]
}

setup(
    name="xrandr-extend",
    version=__version__,
    description=("Extend a HIDPI screen to a normal DPI external display"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="xrandr, hidpi, linux, external monitor",
    author="Ashwin Vishnu Mohanan",
    author_email="ashwinvis+gh@pm.me",
    url="https://github.org/ashwinvis/xrandr-extend",
    license="GPL",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    install_requires=["setuptools"],
    packages=find_packages(),
    package_data=package_data,
    entry_points={"console_scripts": console_scripts},
)
