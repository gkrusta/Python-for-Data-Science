# ft_package

A sample test package for counting occurrences of an item in a list.

## Functionality

This package includes the following functionality:

- `count_in_list`: Counts occurrences of an item in a given list.

## Struct

ft_package/

├── ft_package/       # Package directory

│		├── __init__.py   # It tells Python: "This folder is a package!"

│		├── core.py       # main module with the function

├── LICENSE           # License file (e.g., MIT)

├── README.md         # Description of package

├── pyproject.toml    # It describes what tools are needed to build the package.


├── setup.py          # Package name, version, author, and dependencies.


## Installation
```bash
 -m build
```

The build tool creates two files:
- `.tar.gz`: A compressed archive of your package source code.
- `.whl` (wheel file): A ready-to-install version of your package.


To install the package, run:
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```