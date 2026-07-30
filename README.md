# python-lib (zed-pkg-test/python-lib)

A trivial Python package published to the zed registry. Consumers source it
**via zed** (into their configured `[install].dir`) while pip keeps owning the
rest of the environment. See `.zpkg.toml`.

It also carries a normal `pyproject.toml` so the package is importable — and
buildable as a wheel — once zed drops it into place. The consumer puts the
install dir on `PYTHONPATH` (the python adapter writes `.zed/python_path`) and
imports `python_lib` as it would any other distribution.
