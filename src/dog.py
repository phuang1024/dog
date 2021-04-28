#
#  Dog
#  Similar to Unix CAT but with syntax highlighting.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import sys
import os
from dog_constants import *
from dog_bark import bark
from dog_python import parse_python
from dog_c import parse_c
from dog_xml import parse_xml

VERSION = "0.0.3"
FILE_TYPES = (
    ((".py", ".pyw"), parse_python),
    ((".c", ".h", ".i"), parse_c),
    ((".xml", ".html"), parse_xml)
)


def main():
    if len(sys.argv) == 1:
        print(f"Dog {VERSION}, a file printer with syntax highlighting.")
        print("Type \"dog --help\" for more info.")
        return
    elif sys.argv[1] == "--help":
        print("Usage:")
        print("    dog file.py")
        print("OR")
        print("    dog file.c")
    elif sys.argv[1] == "--version":
        print(VERSION)
    elif sys.argv[1] == "bark":
        bark()

    path = os.path.expanduser(os.path.abspath(sys.argv[1]))
    ext = os.path.splitext(path)[-1]
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = file.read()
            if not data.endswith("\n"):
                data += "\n"
    else:
        print(f"No file: {path}")
        return

    func = None
    for exts, f in FILE_TYPES:
        if ext in exts:
            func = f
            break
    if func is not None:
        func(data)
    else:
        print(data)
        print("\nWARNING: File type not recognized")

    sys.stdout.write(RESET)
    sys.stdout.flush()


main()
