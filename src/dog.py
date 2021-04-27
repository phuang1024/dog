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
from dog_python import parse_python
from dog_c import parse_c
import time

VERSION = "0.0.1"


def main():
    if len(sys.argv) == 1:
        print("Dog, a file printer with syntax highlighting.")
        print("Type \"dog --help\" for more info.")
        return
    elif sys.argv[1] == "--help":
        print("Usage:")
        print("    dog file.py")
        print("OR")
        print("    dog file.c")
    elif sys.argv[1] == "--version":
        print(VERSION)

    path = os.path.expanduser(os.path.abspath(sys.argv[1]))
    if os.path.isfile(path):
        with open(path, "r") as file:
            data = file.read()
            if not data.endswith("\n"):
                data += "\n"
    elif path[(len(path)-4):] == "bark":
        pass
    else:
        print(f"No file: {path}")
        print(path[(len(path)-4):])
        return

    if path.endswith(".py"):
        parse_python(data)
    elif path.endswith(".c"):
        parse_c(data)
    elif path[(len(path)-4):] == "bark":
        while 1:
            os.system("clear")
            print('''                               /-|/-|
                        ______/__/  |
                       / O         /
                     _/          /
                   0|_____     /
                        |_____| ''')
            time.sleep(1)
            os.system("clear")
            print('''                               /-|/-|
                        ______/__/  |
                       / O         /
                     _/          /
                   0|_____--   /
               Woof! _____/  
                        |_____| ''')
            time.sleep(1)
            
    else:
        print(data)
        print()
        print("WARNING: File type not recognized.")

    print(RESET)
    sys.stdout.flush()


main()
