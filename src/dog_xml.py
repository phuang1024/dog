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
import string
from dog_constants import *


def parse_xml(data: str):
    prev_tag = False
    in_tag = False
    tag_part = 0

    while len(data) > 0:
        sys.stdout.write(WHITE)

        if data.startswith(("<!", "<")):
            in_tag = True
            tag_part = 0
        elif data.startswith(">"):
            in_tag = False

        if data.startswith(("<!", "</")):
            sys.stdout.write(GRAY)
            sys.stdout.write(data[:2])
            data = data[2:]
            prev_tag = True
            continue
        if data.startswith(("<", ">")):
            prev_tag = (data[0] == "<")
            sys.stdout.write(GRAY)
            sys.stdout.write(data[0])
            data = data[1:]
            continue

        if prev_tag:
            sys.stdout.write(CYAN)
            while len(data) > 0 and (data[0] in VAR_CHARS+string.digits):
                sys.stdout.write(data[0])
                data = data[1:]
            prev_tag = False
            continue

        if in_tag and (data[0] in VAR_CHARS+string.digits):
            if tag_part == 0:
                sys.stdout.write(MAGENTA)
            elif tag_part == 1:
                sys.stdout.write(YELLOW)

            while len(data) > 0 and (data[0] in VAR_CHARS+string.digits):
                sys.stdout.write(data[0])
                data = data[1:]
            tag_part = 1 if tag_part == 0 else 0

            continue

        sys.stdout.write(data[0])
        data = data[1:]
        prev_tag = False
