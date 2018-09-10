#
# Copyright (c) 2014-2015 Sylvain Peyrefitte
#
# This file is part of rdpy.
#
# rdpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
Basic virtual scancode mapping
"""

_SCANCODE_QWERTY_ = {
    0x00: "<00UNKNOWN>\n",
    0x01: "<ESC>\n",
    0x02: "1",
    0x03: "2",
    0x04: "3",
    0x05: "4",
    0x06: "5",
    0x07: "6",
    0x08: "7",
    0x09: "8",
    0x0A: "9",
    0x0B: "0",
    0x0C: "-",
    0x0D: "+",
    0x0E: "<BKSPC>\n",
    0x0F: "<TAB>\n",
    0x10: "Q",
    0x11: "W",
    0x12: "E",
    0x13: "R",
    0x14: "T",
    0x15: "Y",
    0x16: "U",
    0x17: "I",
    0x18: "O",
    0x19: "P",
    0x1A: "4",
    0x1B: "6",
    0x1C: "<RETURN>\n",
    0x1D: "<LCONTROL>\n",
    0x1E: "A",
    0x1F: "S",
    0x20: "D",
    0x21: "F",
    0x22: "G",
    0x23: "H",
    0x24: "J",
    0x25: "K",
    0x26: "L",
    0x27: "1",
    0x28: "7",
    0x29: "3",
    0x2A: "<LSHIFT>\n",
    0x2B: "5",
    0x2C: "Z",
    0x2D: "X",
    0x2E: "C",
    0x2F: "V",
    0x30: "B",
    0x31: "N",
    0x32: "M",
    0x33: ",",
    0x34: ".",
    0x35: "2",
    0x36: "<RSHIFT>\n",
    0x37: "*",
    0x38: "<LMENU>\n",
    0x39: " ",
    0x3A: "<CAPSLOCK>\n",
    0x3B: "\n<F1>",
    0x3C: "\n<F2>",
    0x3D: "\n<F3>",
    0x3E: "\n<F4>",
    0x3F: "\n<F5>",
    0x40: "\n<F6>",
    0x41: "\n<F7>",
    0x42: "\n<F8>",
    0x43: "\n<F9>",
    0x44: "\n<F10>",
    0x45: "\n<NUMLOCK>",
    0x46: "\n<SCROLLLOCK>",
    0x47: "<NUMPAD7>\n",
    0x48: "<NUMPAD8>\n",
    0x49: "<NUMPAD9>\n",
    0x4A: "-",
    0x4B: "<NUMPAD4>\n",
    0x4C: "<NUMPAD5>\n",
    0x4D: "<NUMPAD6>\n",
    0x4E: "+",
    0x4F: "<NUMPAD1>\n",
    0x50: "<NUMPAD2>\n",
    0x51: "<NUMPAD3>\n",
    0x52: "<NUMPAD0>\n",
    0x53: ".",
    0x54: "<SYSREQ>\n",
    0x56: "<OEM_102>\n",
    0x57: "<F11>\n",
    0x58: "<F12>\n",
    0x5b: "<WINDOWS>\n",
    0x5F: "<SLEEP>\n",
    0x62: "<ZOOM>\n",
    0x63: "<HELP>\n",
    0x64: "<F13>\n",
    0x65: "<F14>\n",
    0x66: "<F15>\n",
    0x67: "<F16>\n",
    0x68: "<F17>\n",
    0x69: "<F18>\n",
    0x6A: "<F19>\n",
    0x6B: "<F20>\n",
    0x6C: "<F21>\n",
    0x6D: "<F22>\n",
    0x6E: "<F23>\n",
    0x6F: "<F24>\n",
    0x70: "<HIRAGANA>\n",
    0x71: "<HANJA_KANJI>\n",
    0x72: "<KANA_HANGUL>\n",
    0x73: "<ABNT_C1>\n",
    0x76: "<F24_JP>\n",
    0x79: "<CONVERT_JP>\n",
    0x7B: "<NONCONVERT_JP>\n",
    0x7C: "<TAB_JP>\n",
    0x7D: "<BACKSLASH_JP>\n",
    0x7E: "<ABNT_C2>\n",
}


def scancodeToChar(code):
    """
    @summary: try to convert native code to char code
    @return: char
    """
    if not _SCANCODE_QWERTY_.has_key(code):
        return "<unknown scancode %x>"%code
    return _SCANCODE_QWERTY_[code]