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

# TODO: [Agastya] need to add more C keywords

import sys
from dog_constants import *
from dog_utils import is_kwd

KWDS_RED = [
    "break",  "switch", "continue"
    "else",  "for",
    "if",        "#include",
    "return",  "while", "#define"
]

KWDS_BLUE = [
    "&&",  "struct", "enum",  "void",     "global",  "||",     "true", "false"
]

KWDS_YELLOW = [
    "printf", "scanf", "fprintf", "fscanf", "qsort"
]

KWDS_GREEN = [
    "char", "int", "String[]", "float", "double", "long", "const", "unsigned", "signed", 
]

STRING_START = sorted([
    "\"",
    "'",
    "\"\"\"",
    "'''",
], key=len, reverse=True)


def parse_c(data):
    prev = " "
    in_string = False
    string_char = ""

    while len(data) > 0:
        # Comment
        if (data.startswith("//") or data.startswith("/*")) and not in_string:
            while data[0] != "\n":
                sys.stdout.write(GRAY)
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
            sys.stdout.write(YELLOW)    # TODO bug here
            sys.stdout.write(data[:2])
            prev = data[1]
            data = data[2:]
            continue

        # Write string color
        if in_string:
            sys.stdout.write(YELLOW)
            sys.stdout.write(data[0])
            prev = data[0]
            data = data[1:]
            continue

        # Check keywords
        red = is_kwd(data, KWDS_RED)
        blue = is_kwd(data, KWDS_BLUE)
        yellow = is_kwd(data, KWDS_YELLOW)
        green = is_kwd(data, KWDS_GREEN)
        if red[0] and prev not in VAR_CHARS:
            sys.stdout.write(MAGENTA)
            sys.stdout.write(data[:red[1]])
            prev = data[red[1]-1]
            data = data[red[1]:]
        elif blue[0] and prev not in VAR_CHARS:
            sys.stdout.write(CYAN)
            sys.stdout.write(data[:blue[1]])
            prev = data[blue[1]-1]
            data = data[blue[1]:]
        elif yellow[0] and prev not in VAR_CHARS:
            sys.stdout.write(YELLOW)
            sys.stdout.write(data[:yellow[1]])
            prev = data[yellow[1]-1]
            data = data[yellow[1]:]
        elif green[0] and prev not in VAR_CHARS:
            sys.stdout.write(GREEN)
            sys.stdout.write(data[:green[1]])
            prev = data[green[1]-1]
            data = data[green[1]:]

        # Print white text
        else:
            sys.stdout.write(data[:1])
            prev = data[0]
            data = data[1:]
        sys.stdout.write(WHITE)
