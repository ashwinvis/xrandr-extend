# History

0.2.0 (2019-07-15)
------------------

* New optional option `-x` or `--ext-scale` for the scaling factor (PR #4, #5)

0.1.1 (2019-05-16)
------------------

* Correct command `xrandr_extend` -> `xrandr-extend`

0.1.0 (2019-05-16)
------------------

* Flicker correction
* Use cookiecutter to generate src layout

0.0.3
-----

* Deploy to PyPI
* Reorganize as a package and allow for configuration
* Use `pkg_resources` to find `default.cfg`

0.0.2
-----

* Simpler defaults which uses only scaling factors
* Parse args only inside `__main__` and do not run any commands during dry run
* Less bugs
