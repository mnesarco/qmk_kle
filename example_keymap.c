// Copyright 2022 Frank Martinez (aka mnesarco)

#include QMK_KEYBOARD_H

// Special Chars
#define XKC_N RALT(KC_N)  // ñ

// Home Row
#define A_GUI LGUI_T(KC_A)
#define R_ALT LALT_T(KC_R)
#define S_CTL LCTL_T(KC_S)
#define T_SFT LSFT_T(KC_T)
#define O_GUI LGUI_T(KC_O)
#define I_ALT LALT_T(KC_I)
#define E_CTL LCTL_T(KC_E)
#define N_SFT LSFT_T(KC_N)

// Clipboard
#define U_CPY C(KC_INS)
#define U_PST S(KC_INS)
#define U_CUT C(KC_X)
#define U_REDO C(KC_Y)
#define U_UNDO C(KC_Z)

// Layers
#define L_NUM LT(LAYER_NUMS, KC_ESC)
#define L_NAV LT(LAYER_NAV, KC_BSPC)
#define L_SYM LT(LAYER_SYMB, KC_TAB)

#define L_FUN LT(LAYER_FUNC, KC_ENT)
#define L_MOU LT(LAYER_MOUSE, KC_SPC)
#define L_MED LT(LAYER_MEDIA, KC_DEL)

// OneShot Shift
#define OS_LSFT OSM(MOD_LSFT)
#define OS_RSFT OSM(MOD_LSFT)



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

    // Symbols
    // ---------------------------------------------------------------------------------------------------------------------------------
    [LAYER_SYMB] = LAYOUT_split_3x6_4(
    // <deflayer symbols>
                  _______,  _______,  _______,  _______,  _______,         KC_EXLM,     KC_RPRN,     KC_RCBR,     KC_RBRC,      KC_CIRC,      KC_TILD,
        _______,  KC_LGUI,  KC_LALT,  KC_LCTL,  KC_LSFT,  _______,         KC_HASH,     KC_LPRN,     KC_LCBR,     KC_LBRC,      KC_LABK,      KC_RABK,
        _______,  KC_RALT,  _______,  _______,  _______,  _______,         KC_DLR,      KC_PERC,     KC_AMPR,     KC_QUES,      KC_PIPE,      KC_UNDS,
                            _______,  _______,  _______,  _______,         KC_DQUO,     KC_QUOT,     KC_ASTR,     KC_AT
    // </deflayer>
    ),

    // Numbers
    // ---------------------------------------------------------------------------------------------------------------------------------
    [LAYER_NUMS] = LAYOUT_split_3x6_4(
    // <deflayer numbers>
                  _______,  _______,  _______,  _______,  _______,         _______,  KC_7,     KC_8,     KC_9,      KC_BSLS,   _______,
        _______,  KC_LGUI,  KC_LALT,  KC_LCTL,  KC_LSFT,  _______,         KC_SCLN,  KC_4,     KC_5,     KC_6,      KC_ASTR,   KC_MINS,
        _______,  KC_RALT,  _______,  _______,  _______,  _______,         KC_GRV,   KC_1,     KC_2,     KC_3,      KC_SLSH,   KC_PLUS,
                            _______,  _______,  _______,  _______,         KC_DOT,   KC_COMM,  KC_0,     KC_EQL
    // </deflayer>
    ),

    // Functions
    // ---------------------------------------------------------------------------------------------------------------------------------
    [LAYER_FUNC] = LAYOUT_split_3x6_4(
    // <deflayer functions>
                  KC_F12,   KC_F7,    KC_F8,    KC_F9,    KC_PSCR,         _______,    _______,     _______,     _______,      _______,    _______,
        _______,  KC_F11,   KC_F4,    KC_F5,    KC_F6,    _______,         _______,    KC_RSFT,     KC_RCTL,     KC_LALT,      KC_RGUI,    _______,
        _______,  KC_F10,   KC_F1,    KC_F2,    KC_F3,    KC_PAUSE,        _______,    _______,     _______,     _______,      KC_RALT,    _______,
                            _______,  KC_ESC,   KC_BSPC,  KC_TAB,          _______,    _______,     _______,     _______
    // </deflayer>
    ),

    // Mouse
    // ---------------------------------------------------------------------------------------------------------------------------------
    [LAYER_MOUSE] = LAYOUT_split_3x6_4(
    // <deflayer mouse>
                  U_REDO,   U_PST,    U_CPY,    U_CUT,    U_UNDO,          _______,    _______,     _______,     _______,      _______,    _______,
        _______,  KC_MS_L,  KC_MS_D,  KC_MS_U,  KC_MS_R,  _______,         _______,    KC_RSFT,     KC_RCTL,     KC_LALT,      KC_RGUI,    _______,
        _______,  KC_WH_L,  KC_WH_D,  KC_WH_U,  KC_WH_R,  _______,         _______,    _______,     _______,     _______,      KC_RALT,    _______,
                            _______,  KC_BTN2,  KC_BTN1,  KC_BTN3,         _______,    _______,     _______,     _______
    // </deflayer>
    ),

    // Media
    // ---------------------------------------------------------------------------------------------------------------------------------
    [LAYER_MEDIA] = LAYOUT_split_3x6_4(
    // <deflayer media>
                  _______,  _______,  _______,  _______,  _______,         _______,    _______,     _______,     _______,      _______,    _______,
        _______,  KC_MPRV,  KC_VOLD,  KC_VOLU,  KC_MNXT,  _______,         _______,    KC_RSFT,     KC_RCTL,     KC_LALT,      KC_RGUI,    _______,
        _______,  _______,  _______,  _______,  _______,  _______,         _______,    _______,     _______,     _______,      KC_RALT,    _______,
                            _______,  KC_MUTE,  KC_MPLY,  KC_MSTP,         _______,    _______,     _______,     _______
    // </deflayer>
    ),

};

/*
    [LAYER_NUMS] = LAYOUT_split_3x6_4(
                  _______,  _______,  _______,  _______,  _______,         _______,    _______,     _______,     _______,      _______,    _______,
        _______,  _______,  _______,  _______,  _______,  _______,         _______,    _______,     _______,     _______,      _______,    _______,
        _______,  _______,  _______,  _______,  _______,  _______,         _______,    _______,     _______,     _______,      _______,    _______,
                            _______,  _______,  _______,  _______,         _______,    _______,     _______,     _______
    ),

*/


/*
<hardware-layout>

!!! Keycap layout and colors
----------------------------

(keycap
  numbers         _                 symbols
  _               defsrc            _
  nav             _                 functions
  mouse           _                 media
)

(colors
  #3498DB   #000000   #D68910
  #000000   #000000   #000000
  #7D3C98   #0000ff   #ff0000
  #239B56   #000000   #5D6D7E
)

!!! Options are based on row column and kle syntax
-------------------------------------------------------
!!! (options row col data)

(options 1 1 {y:0.75, x:1})
(options 1 2 {y:-0.5})
(options 1 3 {y:-0.25})
(options 1 4 {y:0.35})
(options 1 5 {y:0.2})

(options 1 6 {x: 6})
(options 1 7 {y:-0.2})
(options 1 8 {y:-0.35})
(options 1 9 {y:0.25})
(options 1 10 {y:0.5})

(options 2 3 {y:-0.5})
(options 2 4 {y:-0.25})
(options 2 5 {y:0.35})
(options 2 6 {y:0.2})

(options 2 7 {x: 6})
(options 2 8 {y:-0.2})
(options 2 9 {y:-0.35})
(options 2 10 {y:0.25})
(options 2 11 {y:0.5})

(options 3 3 {y:-0.5})
(options 3 4 {y:-0.25})
(options 3 5 {y:0.35})
(options 3 6 {y:0.2})

(options 3 7 {x: 6})
(options 3 8 {y:-0.2})
(options 3 9 {y:-0.35})
(options 3 10 {y:0.25})
(options 3 11 {y:0.5})

(options 4 1 {x:3.75})
(options 4 5 {x:2.5})



!!! Override or assign labels
-----------------------------
!!! (label code text)

(label A_GUI A)
(label R_ALT R)
(label S_CTL S)
(label T_SFT T)

(label O_GUI O)
(label I_ALT I)
(label E_CTL E)
(label N_SFT N)

(label L_NUM Num)
(label L_FUN Fn)
(label L_MED Media)
(label L_MOU 🖱)
(label L_NAV Nav)
(label L_SYM Sym)

(label U_REDO ↷)
(label U_UNDO ↶)
(label XKC_N ñ)
(label U_CPY copy)
(label U_PST paste)
(label U_CUT cut)
(label OS_LSFT ⇮)
(label OS_RSFT ⇮)
(label BTN1 LB)
(label BTN2 RB)
(label BTN3 MB)

!!! Add some notes
------------------

(description
    Marz Split 44
)

</hardware-layout>
*/
