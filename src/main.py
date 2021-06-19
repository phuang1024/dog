#
#  Dog
#  Console printer with syntax highlighting.
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
import io
import argparse
import lang_json
from utils import *

VERSION = "0.1.0"
LANGS = (
    "json",
    "txt",
)


def get_lang(path, lang):
    if lang != "":
        return lang
    if path == "-":
        return "txt"

    if path.endswith(".json"):
        return "json"
    if path.endswith(".txt"):
        return "txt"

    return "txt"


def main():
    parser = argparse.ArgumentParser(description="Console printer with syntax highlighting.")
    parser.add_argument("file", help="File path to read from (put - for stdin)")
    parser.add_argument("-v", "--version", help="Print version info.")
    parser.add_argument("-l", "--lang", nargs="?", default="", help="Force language mode. Omit for autodetect.", choices=LANGS)
    parser.add_argument("--linenos", action="store_true", help="Show line numbers.")
    parser.add_argument("-w", "--whitespace", action="store_true", help="Show whitespace as bullet points.")
    args = parser.parse_args()

    if args.version:
        print(f"Dog {VERSION}")
        return

    if args.file == "-":
        data = sys.stdin.read().encode()
    else:
        with open(args.file, "rb") as file:
            data = file.read()

    istream = io.BytesIO(data)
    ostream = io.StringIO()
    lang = get_lang(args.file, args.lang)

    if lang == "txt":
        ostream.write(istream.read().decode())
    elif lang == "json":
        lang_json.dump(istream, ostream)
    ostream.seek(0)

    line = 2
    curr_col = WHITE
    recording_col = False

    if args.linenos:
        sys.stdout.write(f"{GRAY}1     {WHITE}")

    while len(ch := ostream.read(1)) > 0:
        if args.whitespace and ch == " ":
            sys.stdout.write(GRAY)
            sys.stdout.write(BULLET_POINT)
            sys.stdout.write(curr_col)
        else:
            sys.stdout.write(ch)

        if ch == "\x1b":
            curr_col = "\x1b"
            recording_col = True
        elif ch == "m" and recording_col:
            recording_col = False
            curr_col += "m"
        elif recording_col:
            curr_col += ch

        if ch == "\n" and args.linenos:
            sys.stdout.write(GRAY)
            sys.stdout.write(str(line))
            sys.stdout.write(" "*(6-len(str(line))))
            sys.stdout.write(curr_col)
            line += 1

    sys.stdout.write(RESET)
    if args.linenos:
        sys.stdout.write("\n")
    sys.stdout.flush()


main()
