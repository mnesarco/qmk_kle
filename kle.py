#!/usr/bin/python3
# -*- encoding: utf-8 -*-
#    _________________________________________________________________________
#
#    Copyright 2022 Frank David Martinez Muñoz (aka @mnesarco)
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#    _________________________________________________________________________

from sys import argv
from typing import Dict
from pathlib import Path
import re

# +-------------------------------------------------------------------------+
# | Translation table for common QML aliases                                |
# +-------------------------------------------------------------------------+

code_aliases = {
    "RETURN": "Return",
    "RET": "Return",
    "ENTER": "Enter",
    "ENT": "Enter",
    "MINS": "-",
    "EQL": "=",
    "SPC": "Space",
    "BSPC": "⌫",
    "PGUP": "⤒",
    "PGDN": "⤓",
    "INS": "Ins",
    "DEL": "Del",
    "VOLU": "🕪",
    "VOLD": "🕩",
    "MUTE": "🕨",
    "DOT": ".",
    "GRV": "`",
    "LSFT": "⇧",
    "RSFT": "⇧",
    "LCTL": "⎈",
    "RCTL": "⎈",
    "LALT": "⎇",
    "RALT": "⌥",
    "LGUI": "◆",
    "RGUI": "◆",
    "TAB": "↹",
    "LBRC": "[",
    "RBRC": "]",
    "LPRN": "(",
    "RPRN": ")",
    "LCBR": "{",
    "RCBR": "}",
    "SCLN": ";",
    "COMM": ",",
    "LABK": "<",
    "RABK": ">",
    "PIPE": "|",
    "EXLM": "!",
    "DLR": "$",
    "HASH": "#",
    "DQUO": '\\"',
    "QUOT": "'",
    "LEFT": "←",
    "RGHT": "→",
    "CAPS": "🄰 Caps",
    "MNXT": "⏭",
    "BSLS": "\\\\",
    "PLUS": "+",
    "ASTR": "*",
    "MPLY": "⏯",
    "MPRV": "⏮",
    "UP": "↑",
    "DOWN": "↓",
    "MSTP": "◼",
    "SLSH": "/",
    "AT": "@",
    "UNDS": "_",
    "PERC": "%",
    "AMPR": "&",
    "QUES": "?",
    "CIRC": "^",
    "TILD": "~",
    "MS_L": "←m",
    "MS_D": "↓m",
    "MS_U": "↑m",
    "MS_R": "→m",
    "WH_L": "←w",
    "WH_D": "↓w",
    "WH_U": "↑w",
    "WH_R": "→w",
}

# +-------------------------------------------------------------------------+
# | Matrix position to label position mapping (keyboard-layout-editor)      |
# |                                                                         |
# |   | 0    8    2  |                                                      |
# |   | 6    9    7  |                                                      |
# |   | 1   10    3  |--->  [0,1,2,3,4,5,6,7,8,9,10,11]                     |
# |   | 4   11    5  |                                                      |
# |                                                                         |
# | Requires {a:0}                                                          |
# +-------------------------------------------------------------------------+

label_pos = {
    (0,0): 0,   (0,1): 8,   (0,2): 2,
    (1,0): 6,   (1,1): 9,   (1,2): 7,
    (2,0): 1,   (2,1): 10,  (2,2): 3,
    (3,0): 4,   (3,1): 11,  (3,2): 5,
}

# +-------------------------------------------------------------------------+
# | Custom options per keycap                                               |
# |   (options alias option)                                                |
# +-------------------------------------------------------------------------+
# option: {
#    r   : rotation angle,
#    rx  : rotation center x,
#    ry  : rotation center y,
#    y   : top margin,
#    x   : left margin,
#    c   : keycap color,
#    p   : profile,
#    f   : label size,
#    w   : width,
#    h   : height,
#    w2  : width 2 (non rectangular),
#    h2  : height 2 (non rectangular),
#    x2  : left margin 2 (non rectangular),
#    y2  : top margin 2 (non rectangular)
# }
# +-------------------------------------------------------------------------+

class Options:

    Pattern = re.compile(r'''[(]
        \s*
        options
        \s+
        (?P<row>[0-9]+)
        \s+
        (?P<col>[0-9]+)
        \s+
        (?P<data>{.+?})
        [)]''', re.X | re.DOTALL)

    def __init__(self, data):
        self.index = dict()
        for m in Options.Pattern.finditer(data):
            self.index[(int(m.group('row'))-1, int(m.group('col'))-1)] = m.group("data")

    def __call__(self, row: int, col: int) -> str:
        return self.index.get((row, col), None)


# +-------------------------------------------------------------------------+
# | Global Keycap layout (labels)                                           |
# +-------------------------------------------------------------------------+
#
#    (keycap
#      _      _      _
#      _      _      _
#      _      _      _
#      _      _      _
#    )
#
#  Put the layer name in the correspondign position.
# +-------------------------------------------------------------------------+

class KeyCap:

    Pattern = re.compile(r'''[(]
        \s*
        keycap
        \s+
        (?P<data>.+?)
        (?<!\\)[)]''', re.X | re.DOTALL)

    Colors = re.compile(r'''[(]
        \s*
        colors
        \s+
        (?P<data>[#a-fA-F0-9\s]+?)
        [)]''', re.X | re.DOTALL)

    def __init__(self, data: str):
        m = KeyCap.Pattern.search(data)
        if not m:
            raise RuntimeError("Keycap definition not found. ie (keycap ...)")

        rows = m.group("data").splitlines()
        self.rows = [r.split() for r in rows]
        if len(self.rows) != 4 or not all(len(r) == 3 for r in self.rows):
            raise RuntimeError("Invalid keycap definition. Mandatory format for (keycap ...): 4 rows of 3 columns, empty places marked with '_'")

        m = KeyCap.Colors.search(data)
        if m:
            colors = [c.split() for c in m.group("data").splitlines()]
            if len(colors) != 4 or not all(len(r) == 3 for r in colors):
                raise RuntimeError("Invalid keycap colors definition. Mandatory format for (colors ...): 4 rows of 3 columns if html hex color codes. ie. colors(#000000 ...)")
        else:
            print("[Warning] Invalid colors definition (colors ...). Fallback to all black.")
            colors = [
                ['#000000','#000000','#000000'],
                ['#000000','#000000','#000000'],
                ['#000000','#000000','#000000'],
                ['#000000','#000000','#000000'],
            ]

        self.layermap = dict()
        self.colormap = dict()
        for r, row in enumerate(self.rows):
            for c, col in enumerate(row):
                if col != '_':
                    self.layermap[col] = label_pos[(r,c)]
                    self.colormap[col] = colors[r][c]


    def label(self, keys: Dict[str, str]) -> str:
        lab = ["", "", "", "", "", "", "", "", "", "", "", ""]
        for layer, key in keys.items():
            if key:
                p = self.layermap.get(layer, None)
                key = self.translate(key)
                if p is not None:
                    if key == '\\\\' or key == '\\"':
                        lab[p] = key
                    else:
                        lab[p] = key.replace('\\', '')
        content = re.sub(r'(\\n)+$', '', "\\n".join(lab))
        return f'"{content}"'

    def get_colors(self):
        lab = ["", "", "", "", "", "", "", "", "", "", "", ""]
        for layer, pos in self.layermap.items():
            lab[pos] = self.colormap.get(layer, "")
        content = "\\n".join(lab).rstrip('\\n')
        return f'"{content}"'

    def translate(self, key):
        if key.startswith('KC_'):
            key = key[3:]
        key_t = code_aliases.get(key, None)
        if not key_t:
            untranslated = True
        else:
            key = key_t
            untranslated = False
        if len(key) == 1 and key.isalpha():
            return key.upper()
        if key == 'XX':
            return ''
        if not re.match('^F[0-9]+$', key) and untranslated:
            return key.lower()
        return key

    def __str__(self) -> str:
        return f"{self.rows}"


# +-------------------------------------------------------------------------+
# | Hardware layout parser                                                  |
# +-------------------------------------------------------------------------+
# #| Put the hardware layout in a block comment
#
#    <hardware-layout>
#
#    (keycap ...)
#
#    (colors ...)
#
#    (options ...)*
#
#    (label ...)*
#
#    </hardware-layout>
# |#
# +-------------------------------------------------------------------------+

class HardwareLayout:

    Pattern = re.compile(r'''
        <hardware-layout>
        (?P<data>.+?)
        </hardware-layout>
    ''', re.X | re.DOTALL)

    def __init__(self, data):
        m = HardwareLayout.Pattern.search(data)
        if not m:
            raise RuntimeError("Hardware layout section ot found. ie. <hardware-layout>...</hardware-layout>")
        data = m.group('data')
        self.keycap = KeyCap(data)
        self.options = Options(data)
        self.description = self.get_description(data)
        self.import_labels(data)

    def import_labels(self, data):
        p = re.compile(r'''[(]
            \s*
            label
            \s+
            (?P<name>[^\s)]+)
            \s+
            (?P<data>.+?)
            [)]''', re.X | re.DOTALL)
        for m in p.finditer(data):
            code_aliases[m.group("name")] = m.group("data")

    def __str__(self) -> str:
        return f"Keycap: {self.keycap}"

    def get_description(self, data):
        pattern = re.compile(r'[(]\s*description\s+(?P<description>.*?)(?<!\\)[)]', re.DOTALL | re.X)
        m = pattern.search(data)
        if m:
            return m.group("description").replace("\n", "<br />")
        return ""


# +-------------------------------------------------------------------------+
# | QMK layer parser                                                        |
# +-------------------------------------------------------------------------+

class QMKLayer:

    def __init__(self, name: str, data: str):
        self.name = name if name else 'defsrc'
        # Translate to KMonad syntax for XX and _
        data = re.sub(r'\b_______\b|KC_TRANSPARENT|KC_TRNS', '_', data)
        data = re.sub(r'\bXXXXXXX\b|KC_NO', 'XX', data)
        # Remove comments
        data = re.sub(r'//.*?\r?\n', '', data)  # Line comments
        data = re.sub(r'/\*.*?\*/', '', data)  # Block comments
        lines = [line.strip() for line in data.splitlines()]
        self.rows = [[code for code in re.split(r'\s*,\s*|\s+', line) if code] for line in lines if len(line) > 0]

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.name} {self.rows}"

    def __call__(self, row: int, col: int):
        try:
            v = self.rows[row][col]
            return None if v == '_' else v
        except:
            return None

# +-------------------------------------------------------------------------+
# | QMK file compiler:                                                   |
# |    <QMK config file> -> <Keyboard Layout Editor Code>                |
# +-------------------------------------------------------------------------+

class QMKKeymapFile:

    LayoutSection = re.compile(r'''//\s*<deflayer(\s+(?P<layer>\S+))?>
        \s+
        (?P<data>.+?)
        //\s*</deflayer>''', re.X | re.DOTALL)

    def __init__(self, file):
        self.layers : Dict[str, QMKLayer] = dict()
        self.first = None
        with open(file, 'r') as f:
            text = f.read()
            for sec in QMKKeymapFile.LayoutSection.finditer(text):
                layer = QMKLayer(sec.group('layer'), sec.group('data'))
                self.layers[layer.name] = layer
                if self.first is None and sec.group('layer'):
                    self.first = sec.group('layer')
            self.hardware = HardwareLayout(text)
            self.name = str(Path(file).absolute())
            self.layout = self.build()

    def build(self) -> str:
        hw = self.layers['defsrc'].rows
        nrows = []
        for r, row in enumerate(hw):
            nrow = []
            for c, k in enumerate(row):
                opt = self.hardware.options(r,c)
                if opt:
                    nrow.append(opt)
                nrow.append((r, c, k))
            nrows.append(nrow)

        out = [f"[{{a:0, y:-1, t:{self.hardware.keycap.get_colors()}}}]"]
        for r in nrows:
            row = []
            for k in r:
                if isinstance(k, str):
                    row.append(k)
                else:
                    row.append(self.keycap(*k))
            out.append("[" + ",".join(row) + "]")
        out.append(f'[{{f:4,w:20,h:3,d:true,t:"#333333",y:1}},"{self.name}<br /><br />{self.hardware.description}"]')
        return ",\n".join(out)

    def keycap(self, row, col, key):
        labels = {layer.name: layer(row, col) for layer in self.layers.values()}
        return self.hardware.keycap.label(labels)

    def __str__(self) -> str:
        return f"{self.layers}\n{self.hardware}"



# +-------------------------------------------------------------------------+
# | Main                                                                    |
# |    python3 kmonad_dump.py <kmonad config filename>                      |
# +-------------------------------------------------------------------------+

if __name__ == '__main__':

    if len(argv) != 2:
        exit("Usage: python3 kle.py <filename>")

    try:
        compiler = QMKKeymapFile(argv[1])
        print("""
            +-----------------------------------------------------------+
            | Go to: http://www.keyboard-layout-editor.com/             |
            | And paste the following code into "</> Raw Data" section. |
            +-----------------------------------------------------------+

        """)
        print(compiler.layout)

    except Exception as ex:
        exit(str(ex))
