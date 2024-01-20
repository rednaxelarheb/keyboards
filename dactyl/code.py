# main.py
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
# from kmk.modules.layers import Layers

# keyboard.debug_enabled = True
keyboard = KMKKeyboard()

# keyboard.modules.append(Layers())

# side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

# if side == SplitSide.RIGHT:
#     print("Identified RIGHT side")
#     keyboard.row_pins = (
#         board.GP6,
#         board.GP7,
#         board.GP8,
#         board.GP9,
#         board.GP10,
#         board.GP11,
#         )
    # keyboard.col_pins = (
    #     board.GP16,
    #     board.GP17,
    #     board.GP18,
    #     board.GP19,
    #     board.GP20,
    #     board.GP22,
    #     )
# else:
#     print("Identified LEFT side")
#     keyboard.col_pins = (
#         board.GP11,
#         board.GP10,
#         board.GP9,
#         board.GP8,
#         board.GP7,
#         board.GP6,
#         )
#     keyboard.row_pins = (
#         board.GP21,
#         board.GP20,
#         board.GP19,
#         board.GP18,
#         board.GP17,
#         board.GP16,
#         )
side = SplitSide.LEFT
# Using drive names (REDOXL, REDOXR) to recognize sides; use split_side arg if you're not doing it
split = Split(split_type=SplitType.UART, split_side=side, data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
keyboard.modules.append(split)

keyboard.col_pins = (
    board.GP11,
    board.GP10,
    board.GP9,
    board.GP8,
    board.GP7,
    board.GP6,
    )
keyboard.row_pins = (
    board.GP21,
    board.GP20,
    board.GP19,
    board.GP18,
    board.GP17,
    board.GP16,
    )

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

FnKey = KC.MO(1)

keyboard.keymap = [
    [  # My Base 
        KC.ESC,  KC.N1,   KC.N2,   KC.N3, KC.N4, KC.N5,         KC.N6,  KC.N7,   KC.N8,   KC.N9, KC.N0, KC.LBRACKET,
        KC.GRV,  KC.Q,    KC.W,    KC.E,  KC.R,  KC.T,          KC.Y,  KC.U,    KC.I,    KC.O,  KC.P,  KC.RBRACKET,
        KC.LALT,  KC.A,    KC.S,    KC.D,  KC.F,  KC.G,         KC.H,  KC.J,    KC.K,    KC.L,    KC.SCOLON,  KC.QUOTE,
        KC.LGUI,  KC.Z,    KC.X,    KC.C,  KC.V,  KC.B,         KC.N,  KC.M,    KC.COMMA,    KC.DOT,  KC.SLASH,  KC.BSLASH,
        KC.NO,  KC.NO,   KC.I,    KC.U,  KC.BSPC,  KC.SPC,      KC.SPACE,  KC.ESC,   KC.MINUS,    KC.EQUAL,  KC.NO,  KC.NO,
        KC.NO,  KC.NO,   KC.DEL,    KC.ENT,  KC.PGDN,  KC.TAB,  KC.RCTL,  KC.PGUP,   KC.RALT,    KC.PGDN,  KC.NO,  KC.NO,
    ]
    # # Base Layer
    # [
    #     # COL GP28		COL GP27	COL GP26	COL GP22	COL GP21	COL GP20	COL GP19	<>	COL GP18		COL GP17	COL GP16	COL GP14	COL GP13	COL GP12	COL GP11

    #     KC.ESCAPE,		KC.N1,		KC.N2,		KC.N3,		KC.N4,		KC.N5,		KC.EQUAL, 		KC.MO(1),		KC.N6,		KC.N7,		KC.N8,		KC.N9,		KC.N0,		KC.MO(2),\

    #     KC.MEH,			KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,		KC.LBRACKET, 	KC.RBRACKET,	KC.Y,		KC.U,		KC.I,		KC.O,		KC.P,		KC.MINUS,\

    #     KC.TAB,			KC.A,		KC.S,		KC.D,		KC.F,		KC.G,		XXXXXXX, 		XXXXXXX,		KC.H,		KC.J,		KC.K,		KC.L,		KC.SCOLON,	KC.QUOTE,\

    #     KC.LSHIFT,		KC.Z,		KC.X,		KC.C,		KC.V,		KC.B,		KC.LALT, 		KC.MO(2),		KC.N,		KC.M,		KC.COMMA,	KC.DOT,		KC.SLASH,	KC.RSHIFT,\

    #     KC.LGUI,		KC.GRV,		KC.BSLASH,	KC.LALT,	KC.LCTRL,	KC.SPACE,	KC.MO(1),	 	KC.ENTER,		KC.BSPACE,	KC.MO(2),	KC.LEFT,	KC.RIGHT,	KC.UP,		KC.DOWN,\

    #  ],

    # # M1 Layer
    # [
    #     # COL GP28		COL GP27	COL GP26	COL GP22	COL GP21	COL GP20	COL GP19	<>	COL GP18		COL GP17	COL GP16			COL GP15	COL GP14			COL GP13	COL GP12
    #     _______,		KC.F1,		KC.F2,		KC.F3,		KC.F4,		KC.F5,		KC.F6,			_______,		KC.F7,		KC.F8,				KC.F9,		KC.F10,				KC.F11,		KC.F12, \

    #     _______,		KC.EXLM,	KC.AT,		KC.HASH,	KC.DOLLAR,	KC.PERCENT,	_______, 		_______,		_______,	KC.LALT(KC.LEFT),	KC.UP,		KC.LALT(KC.RIGHT),	_______,	_______, \

    #     _______,		KC.N1,		KC.N2,		KC.N3,		KC.N4,		KC.N5,		XXXXXXX, 		XXXXXXX,		_______,	KC.LEFT,			KC.DOWN,	KC.RIGHT,			_______,	_______, \

    #     _______,		_______,	_______,	_______,	_______,	_______,	_______,    	_______,    	_______,	_______,			_______,    _______,			_______,	_______, \

    #     _______,		_______,	_______,	_______,	_______,    _______,    _______,	 	_______,		_______,    _______,    		_______,    _______,    		_______,	_______, \

    #  ],

    # # M2 Layer
    # [
    #     # COL GP28		COL GP27	COL GP26	COL GP22	COL GP21	COL GP20	COL GP19	<>	COL GP18		COL GP17	COL GP16	COL GP15	COL GP14	COL GP13	COL GP12
    #     _______,		_______,	_______,	_______,	_______,	_______,	_______, 		_______,		_______,	_______,	_______,	_______,	_______,	_______, \

    #     _______,		_______,	_______,	_______,	_______,	_______,	_______, 		_______,		KC.CIRC,	KC.AMPR,	KC.ASTR,	KC.LPRN,	KC.RPRN,	_______, \

    #     _______,		_______,	_______,	_______,	_______,	_______,	XXXXXXX, 		XXXXXXX,		KC.N6,		KC.N7,		KC.N8,		KC.N9,		KC.N0,		_______, \

    #     _______,		_______,	_______,	_______,	_______,	_______,	_______,    	_______,    	_______,	_______,	_______,    _______,	_______,	_______, \

    #     _______,		_______,	_______,	_______,	_______,    _______,    _______,	 	_______,		_______,    _______,    _______,    _______,    _______,	_______, \

    #  ],
]


if __name__ == '__main__':
    keyboard.go()
