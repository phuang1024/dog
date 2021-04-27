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

import string

BLACK =   "\x1B[0;30m"
GRAY =    "\x1B[1;30m"
WHITE =   "\x1B[0;37m"
RED =     "\x1B[0;31m"
YELLOW =  "\x1B[0;33m"
GREEN =   "\x1B[0;32m"
CYAN =    "\x1B[0;34m"
MAGENTA = "\x1B[0;35m"

VAR_CHARS = string.ascii_letters + "_"
