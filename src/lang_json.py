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

import east
from typing import IO
from utils import *


def write_null(element: east.json.Null, ostream: IO[str]):
    ostream.write(CYAN)
    ostream.write("null")

def write_bool(element: east.json.Bool, ostream: IO[str]):
    ostream.write(CYAN)
    ostream.write(str(element.value).lower())

def write_num(element: east.json.Number, ostream: IO[str]):
    ostream.write(CYAN)
    ostream.write(str(element.value))

def write_colon(element: east.json.Colon, ostream: IO[str]):
    ostream.write(WHITE)
    ostream.write(":")

def write_comma(element: east.json.Comma, ostream: IO[str]):
    ostream.write(WHITE)
    ostream.write(",")

def write_str(element: east.json.String, ostream: IO[str]):
    ostream.write(YELLOW)
    ostream.write(f"\"{element.value}\"")

def write_array(element: east.json.Array, ostream: IO[str]):
    ostream.write(WHITE)
    ostream.write("[")
    ostream.write(element.padding_after_start)
    for ele in element.elements:
        write_element(ele, ostream)
    ostream.write(WHITE)
    ostream.write("]")

def write_dpair(element: east.json.DictPair, ostream: IO[str]):
    write_element(element.key, ostream)
    write_element(element.colon, ostream)
    write_element(element.value, ostream)

def write_dict(element: east.json.Dictionary, ostream: IO[str]):
    ostream.write(WHITE)
    ostream.write("{")
    ostream.write(element.padding_after_start)
    for ele in element.elements:
        write_element(ele, ostream)
    ostream.write(WHITE)
    ostream.write("}")

def write_element(element: east.json.Element, ostream: IO[str]):
    if isinstance(element, east.json.Null):
        write_null(element, ostream)
    elif isinstance(element, east.json.Bool):
        write_bool(element, ostream)
    elif isinstance(element, east.json.Number):
        write_num(element, ostream)
    elif isinstance(element, east.json.Colon):
        write_colon(element, ostream)
    elif isinstance(element, east.json.Comma):
        write_comma(element, ostream)
    elif isinstance(element, east.json.String):
        write_str(element, ostream)
    elif isinstance(element, east.json.Array):
        write_array(element, ostream)
    elif isinstance(element, east.json.DictPair):
        write_dpair(element, ostream)
    elif isinstance(element, east.json.Dictionary):
        write_dict(element, ostream)
    ostream.write(element.padding_after)


def dump(istream: IO[bytes], ostream: IO[str]):
    ast = east.json.load(istream)
    write_element(ast.element, ostream)
