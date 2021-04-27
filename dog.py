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
import string
import colorama
from colorama import Fore
colorama.init()

KWDS_RED = [
    "as",     "assert",    "async",    "await",
    "break",  "continue",  "del",      "elif",
    "else",   "except",    "finally",  "for",
    "from",   "if",        "import",   "pass",
    "raise",  "return",    "try",      "while",
    "with",   "yield",
]

KWDS_BLUE = [
    "and",  "class",  "def",     "global",
    "in",   "is",     "lambda",  "nonlocal",
    "not",  "or",     "True",    "False",
    "None",
]

VAR_CHARS = string.ascii_letters + "_"
STRING_START = sorted([
    "\"",
    "'",
    "\"\"\"",
    "'''",
], key=len, reverse=True)


def is_kwd(text, kwds):
    for k in kwds:
        if text.startswith(k) and text[len(k)] not in VAR_CHARS:
            return (True, len(k))
    else:
        return (False, 0)


def main():
    if len(sys.argv) == 1:
        return

    with open(os.path.expanduser(os.path.abspath(sys.argv[1])), "r") as file:
        data = file.read()

    prev = " "
    in_string = False
    string_char = ""
    while len(data) > 0:
        # Comment
        if data.startswith("#") and not in_string:
            while data[0] != "\n":
                sys.stdout.write(Fore.GREEN)
                sys.stdout.write(data[0])
                data = data[1:]
            continue

        # Check if in string
        if in_string:
            if data.startswith(string_char):
                in_string = False
        else:
            for start in STRING_START:
                if data.startswith(start):
                    in_string = True
                    string_char = start
                    break

        # String escape character
        if in_string and data.startswith("\\"):
            sys.stdout.write(Fore.YELLOW)   # TODO bug here
            sys.stdout.write(data[:2])
            prev = data[1]
            data = data[2:]
            continue

        # Write string color
        if in_string:
            sys.stdout.write(Fore.YELLOW)
            sys.stdout.write(data[0])
            prev = data[0]
            data = data[1:]
            continue

        # Check keywords
        red = is_kwd(data, KWDS_RED)
        blue = is_kwd(data, KWDS_BLUE)
        if red[0] and prev not in VAR_CHARS:
            sys.stdout.write(Fore.MAGENTA)
            sys.stdout.write(data[:red[1]])
            prev = data[red[1]-1]
            data = data[red[1]:]
        elif blue[0] and prev not in VAR_CHARS:
            sys.stdout.write(Fore.CYAN)
            sys.stdout.write(data[:blue[1]])
            prev = data[blue[1]-1]
            data = data[blue[1]:]

        # Print white text
        else:
            sys.stdout.write(data[:1])
            prev = data[0]
            data = data[1:]
        sys.stdout.write(Fore.WHITE)

    sys.stdout.flush()


main()
