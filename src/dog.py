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
import argparse
from dog_constants import *
from dog_bark import bark
from dog_json import parse_json
from dog_python import parse_python
from dog_c import parse_c
from dog_xml import parse_xml
from dog_java import parse_java

VERSION = "0.0.3"
FILE_TYPES = (
    ((".py", ".pyw"), parse_python),
    ((".c", ".h", ".i"), parse_c),
    ((".xml", ".html"), parse_xml),
    ((".json",), parse_json),
    ((".java",), parse_java),
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--no-color", help="don't display any color", action="store_true")
    parser.add_argument("-b", "--bark", help="display a dog barking animation", action="store_true")
    parser.add_argument("file", default=None)
    args = parser.parse_args()

    if args.bark:
        bark()
        return

    path = os.path.expanduser(os.path.abspath(args.file))
    ext = os.path.splitext(path)[-1]
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = file.read()
            if not data.endswith("\n"):
                data += "\n"
    else:
        print(f"No file: {path}")
        return

    if args.no_color:
        print(data)
        return

    func = None
    for exts, f in FILE_TYPES:
        if ext in exts:
            func = f
            break
    if func is not None:
        func(data)
    elif data == "\n":
        pass
    else:
        print(data)
        print("\nWARNING: File type not recognized")

    sys.stdout.write(RESET)
    sys.stdout.flush()


main()
