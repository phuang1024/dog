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

import os
import subprocess
import shutil

VERSION = "0.0-4"

PARENT = os.path.dirname(os.path.realpath(__file__))
SRC = os.path.join(os.path.dirname(PARENT), "src")
PKG_NAME = f"dog_{VERSION}"
PKG = os.path.join(PARENT, PKG_NAME)

BIN = os.path.join(PKG, "usr", "local", "bin")
START = os.path.join(BIN, "dog")
CONTROL = os.path.join(PKG, "DEBIAN", "control")

DATA = {
    "Package": "dog",
    "Version": VERSION,
    "Section": "base",
    "Priority": "optional",
    "Architecture": "i386",
    "Maintainer": "Patrick Huang <huangpatrick16777216@gmail.com>",
    "Description": "Unix Cat with syntax highlighting."
}


os.makedirs(BIN)
os.makedirs(os.path.dirname(CONTROL))

for file in os.listdir(SRC):
    if file.endswith(".py"):
        shutil.copy(os.path.join(SRC, file), os.path.join(BIN, file))

with open(CONTROL, "w") as file:
    for key in DATA:
        file.write("{}: {}\n".format(key, DATA[key]))

os.rename(os.path.join(BIN, "dog.py"), os.path.join(BIN, "dog"))
os.system(f"chmod +x {START}")

with open(START, "r") as file:
    data = file.read()
with open(START, "w") as file:
    file.write("#!/usr/bin/python3\n\n")
    file.write(data)

subprocess.Popen(["dpkg-deb", "--build", PKG_NAME], cwd=PARENT).wait()

shutil.rmtree(PKG)
