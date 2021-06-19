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
    parser.add_argument("-v", "--version", help="Print version info.")
    parser.add_argument("-l", "--lang", nargs="?", default="", help="Force language mode. Omit for autodetect.", choices=LANGS)
    parser.add_argument("file", help="File path to read from (put - for stdin)")
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

    sys.stdout.write(ostream.read())
    sys.stdout.write(RESET)


main()
