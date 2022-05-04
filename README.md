# QMK to KLE Generator

Compile QMK layout file into kle code to visualize at http://www.keyboard-layout-editor.com/

This is a port of my previous generator for KMonad (https://github.com/mnesarco/kmonad_dump)

## From this:

```
...


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    // Base Colemak DH
    // ---------------------------------------------------------------------------------------------------------------------------------
    [LAYER_BASE] = LAYOUT_split_3x6_4(
    // <deflayer>
                  KC_Q,     KC_W,     KC_F,     KC_P,     KC_B,            KC_J,     KC_L,     KC_U,     KC_Y,      XKC_N,    KC_ESC,
        OS_LSFT,  A_GUI,    R_ALT,    S_CTL,    T_SFT,    KC_G,            KC_M,     N_SFT,    E_CTL,    I_ALT,     O_GUI,    OS_RSFT,
        KC_LCTL,  KC_Z,     KC_X,     KC_C,     KC_D,     KC_V,            KC_K,     KC_H,     KC_COMM,  KC_DOT,    KC_SLSH,  KC_ENT,
                            KC_LGUI,  L_NUM,    L_NAV,    L_SYM,           L_FUN,    L_MOU,    L_MED,    KC_RALT
    // </deflayer>
    ),

    // Navigation
    // ---------------------------------------------------------------------------------------------------------------------------------
    [LAYER_NAV] = LAYOUT_split_3x6_4(
    // <deflayer nav>
                  _______,  _______,  _______,  _______,  _______,         U_REDO,   U_PST,    U_CPY,    U_CUT,     U_UNDO,   _______,
        _______,  KC_LGUI,  KC_LALT,  KC_LCTL,  KC_LSFT,  _______,         _______,  KC_LEFT,  KC_DOWN,  KC_UP,     KC_RGHT,  _______,
        _______,  KC_RALT,  _______,  _______,  _______,  _______,         _______,  KC_HOME,  KC_PGDN,  KC_PGUP,   KC_END,   _______,
                            _______,  _______,  _______,  _______,         KC_ENT,   KC_SPC,   KC_DEL ,  _______
    // </deflayer>
    ),


...

```

## To this:

![Layout Visualization](https://github.com/mnesarco/qmk_kle/raw/main/example_output.png)

## Just adding some comments in your keymap file:

```

/*
<hardware-layout>

!!! Keycap layout and colors
----------------------------

(keycap 
    _ _ _
    _ _ _
    _ _ _
    _ _ _
)

(colors
    _ _ _
    _ _ _
    _ _ _
    _ _ _
)

!!! Custom options per key (Optional)
!!! Options are based on row column and kle syntax
!!! (options row col data)
-------------------------------------------------------

(options key custom_layout)
.
.
.

!!! Override or assign labels (Optional)
----------------------------------------

(label alias text)
.
.
.

!!! Add some notes (Optional)
-----------------------------

(description
    Free Text
)

</hardware-layout>
*/
```

See example: https://github.com/mnesarco/qmk_kle/blob/main/example_keymap.c

## Usage:

```
python3 kle.py example_keymap.c

```

## Output:

The generated code must be copied and pasted into KLE's Raw Data Box. 

```
➜  qmk_kle python kle.py example_keymap.c 

            +-----------------------------------------------------------+
            | Go to: http://www.keyboard-layout-editor.com/             |
            | And paste the following code into "</> Raw Data" section. |
            +-----------------------------------------------------------+

        
[{a:0, y:-1, t:"#3498DB\n#7D3C98\n#D68910\n#ff0000\n#239B56\n#5D6D7E\n\n\n\n#000000"}],
[{y:0.75, x:1},"\n\n\nF12\n↷\n\n\n\n\nQ",{y:-0.5},"\n\n\nF7\npaste\n\n\n\n\nW",{y:-0.25},"\n\n\nF8\ncopy\n\n\n\n\nF",{y:0.35},"\n\n\nF9\ncut\n\n\n\n\nP",{y:0.2},"\n\n\npscr\n↶\n\n\n\n\nB",{x: 6},"\n↷\n!\n\n\n\n\n\n\nJ",{y:-0.2},"7\npaste\n)\n\n\n\n\n\n\nL",{y:-0.35},"8\ncopy\n}\n\n\n\n\n\n\nU",{y:0.25},"9\ncut\n]\n\n\n\n\n\n\nY",{y:0.5},"\\\n↶\n^\n\n\n\n\n\n\nÑ","\n\n~\n\n\n\n\n\n\nesc"],
["\n\n\n\n\n\n\n\n\n⇮","◆\n◆\n◆\nF11\n←m\n⏮\n\n\n\nA",{y:-0.5},"⎇\n⎇\n⎇\nF4\n↓m\n🕩\n\n\n\nR",{y:-0.25},"⎈\n⎈\n⎈\nF5\n↑m\n🕪\n\n\n\nS",{y:0.35},"⇧\n⇧\n⇧\nF6\n→m\n⏭\n\n\n\nT",{y:0.2},"\n\n\n\n\n\n\n\n\nG",{x: 6},";\n\n#\n\n\n\n\n\n\nM",{y:-0.2},"4\n←\n(\n⇧\n⇧\n⇧\n\n\n\nN",{y:-0.35},"5\n↓\n{\n⎈\n⎈\n⎈\n\n\n\nE",{y:0.25},"6\n↑\n[\n⎇\n⎇\n⎇\n\n\n\nI",{y:0.5},"*\n→\n<\n◆\n◆\n◆\n\n\n\nO","-\n\n>\n\n\n\n\n\n\n⇮"],
["\n\n\n\n\n\n\n\n\n⎈","⌥\n⌥\n⌥\nF10\n←w\n\n\n\n\nZ",{y:-0.5},"\n\n\nF1\n↓w\n\n\n\n\nX",{y:-0.25},"\n\n\nF2\n↑w\n\n\n\n\nC",{y:0.35},"\n\n\nF3\n→w\n\n\n\n\nD",{y:0.2},"\n\n\npause\n\n\n\n\n\nV",{x: 6},"`\n\n$\n\n\n\n\n\n\nK",{y:-0.2},"1\nhome\n%\n\n\n\n\n\n\nH",{y:-0.35},"2\n⤓\n&\n\n\n\n\n\n\n,",{y:0.25},"3\n⤒\n?\n\n\n\n\n\n\n.",{y:0.5},"/\nend\n|\n⌥\n⌥\n⌥\n\n\n\n/","+\n\n_\n\n\n\n\n\n\nEnter"],
[{x:3.75},"\n\n\n\n\n\n\n\n\n◆","\n\n\nesc\nRB\n🕨\n\n\n\nNum","\n\n\n⌫\nLB\n⏯\n\n\n\nNav","\n\n\n↹\nMB\n◼\n\n\n\nSym",{x:2.5},".\nEnter\n\"\n\n\n\n\n\n\nFn",",\nSpace\n'\n\n\n\n\n\n\n🖱","0\nDel\n*\n\n\n\n\n\n\nMedia","=\n\n@\n\n\n\n\n\n\n⌥"],
[{f:4,w:20,h:3,d:true,t:"#333333",y:1},"example_keymap.c<br /><br />Marz Split 44<br />"]
```

# Requirements:

- Python3.6+

# References:

- QMK: https://github.com/qmk/qmk_firmware/
<br />Amazing keyboard firmware.

- Keyboard Layout Editor: http://www.keyboard-layout-editor.com/
<br />Online Keyboard Layout visualization and editing tool.

# TODO

- [ ] Translate all QMK keycodes to labels
- [ ] Export output in json format
