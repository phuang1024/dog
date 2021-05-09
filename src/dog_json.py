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
from dog_constants import *

LIST = 0
DICT = 1


def parse_json(data: str):
    layers = []
    dict_status = 0

    while len(data) > 0:
        sys.stdout.write(WHITE)

        if data.startswith(("true", "null")):
            sys.stdout.write(CYAN)
            sys.stdout.write(data[:4])
            data = data[4:]
            continue
        if data.startswith("false"):
            sys.stdout.write(CYAN)
            sys.stdout.write(data[:5])
            data = data[5:]
            continue

        if data[0] == "{":
            layers.append(DICT)
            dict_status = 0
        elif data[0] == "[":
            layers.append(LIST)
        elif data[0] in "}]":
            layers.pop()
            dict_status = 0
        elif data[0] == ",":
            dict_status = 0

        if data[0] == "\"":
            col = CYAN if dict_status == 0 and len(layers) > 0 and layers[-1] == DICT else YELLOW
            sys.stdout.write(col)
            sys.stdout.write("\"")
            data = data[1:]
            while len(data) > 0 and data[0] != "\"":
                sys.stdout.write(data[0])
                data = data[1:]
            sys.stdout.write("\"")
            data = data[1:]

            dict_status = 1 if dict_status == 0 else 0
            continue

        sys.stdout.write(data[0])
        data = data[1:]
