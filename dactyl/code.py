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

keyboard.modules.append(Layers())

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
    board.GP22,
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

keyboard.keymap = [
    [  # Base Layer
        KC.GRV,             KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,      KC.N6,          KC.N7,          KC.N8,      KC.N9,      KC.N0,      KC.LBRACKET,
        KC.TAB,             KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       KC.Y,           KC.U,           KC.I,       KC.O,       KC.P,       KC.RBRACKET,
        KC.LGUI,            KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       KC.H,           KC.J,           KC.K,       KC.L,       KC.SCOLON,  KC.QUOTE,
        KC.LCTRL,           KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       KC.N,           KC.M,           KC.COMMA,   KC.DOT,     KC.SLASH,   KC.BSLASH,
        #
        #                               X #         # X         # #         # #              # #             # #             X #         # X
        #                                  # #         # #         X #         # X        X #             # X             # #         # #
        #                                    # #         # #         # #         # #    # #             # #             # #         # #
        #                                    # #         # #         # #         # #    # #             # #             # #         # #
        XXXXXXX,              XXXXXXX,  KC.TT(1),   KC.TT(2),   KC.BSPC,    KC.SPC,     KC.SPACE,       KC.ESC,         KC.MINUS,   KC.EQUAL,   XXXXXXX,    XXXXXXX,
        #
        #                               # #         # #         # #         # #              # #             # #             # #         # #
        #                                  # #         # #         # #         # #        # #             # #             # #         # #
        #                                    X #         # X         # #         # #    X #             # X             # #         # #
        #                                    # #         # #         X #         # X    # #             # #             X #         # X
        XXXXXXX,              XXXXXXX,  KC.DEL,     KC.LSHIFT,  KC.PGDN,    KC.ENT,     KC.RSHIFT,      KC.PGUP,        KC.RALT,    KC.PGDN,    XXXXXXX,    XXXXXXX,
    ],
    [  # M1 Function Keys and Arrows
        KC.F1,              KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6,      KC.F7,          KC.F8,          KC.F9,      KC.F10,     KC.F11,     KC.F12
        _______,            _______,    _______,    _______,    _______,    _______,    _______,        KC.PGDN,        KC.PGUP,    _______,    _______,    _______,
        _______,            _______,    _______,    _______,    _______,    _______,    KC.LEFT,        KC.DOWN,        KC.UP,      KC.RIGHT,   _______,    _______,
        _______,            _______,    _______,    _______,    _______,    _______,    _______,        _______,        _______,    _______,    _______,    _______,
        #
        #                               X #         # X         # #         # #              # #             # #             X #         # X
        #                                  # #         # #         X #         # X        X #             # X             # #         # #
        #                                    # #         # #         # #         # #    # #             # #             # #         # #
        #                                    # #         # #         # #         # #    # #             # #             # #         # #
        XXXXXXX,            XXXXXXX,    _______,    _______,    _______,    _______,    _______,        _______,        _______,    _______,    XXXXXXX,    XXXXXXX,
        #
        #                               # #         # #         # #         # #              # #             # #             # #         # #
        #                                  # #         # #         # #         # #        # #             # #             # #         # #
        #                                    X #         # X         # #         # #    X #             # X             # #         # #
        #                                    # #         # #         X #         # X    # #             # #             X #         # X
        XXXXXXX,            XXXXXXX,    _______,    _______,    _______,    _______,    _______,        _______,        _______,    _______,    XXXXXXX,    XXXXXXX,
    ],
    [  # M2 Mouse Control and Function Keys
        KC.F1,              KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6,      KC.F7,          KC.F8,          KC.F9,      KC.F10,     KC.F11,     KC.F12
        _______,            _______,    _______,    _______,    KC.MB_MMB,  _______,    KC.MW_LEFT,     KC.MW_DOWN,     KC.MW_UP,   KC.MW_RIGHT,_______,    _______,
        _______,            _______,    _______,    _______,    KC.MB_LMB,  KC.MB_RMB,  KC.MS_LEFT,     KC.MS_DOWN,     KC.MS_UP,   KC.MS_RIGHT,_______,    _______,
        _______,            _______,    _______,    _______,    _______,    _______,    KC.MB_LMB,      KC.MB_RMB,      _______,    _______,    _______,    _______,
        #
        #                               X #         # X         # #         # #              # #             # #             X #         # X
        #                                  # #         # #         X #         # X        X #             # X             # #         # #
        #                                    # #         # #         # #         # #    # #             # #             # #         # #
        #                                    # #         # #         # #         # #    # #             # #             # #         # #
        XXXXXXX,            XXXXXXX,    _______,    _______,    _______,    _______,    _______,        _______,        _______,    _______,    XXXXXXX,    XXXXXXX,
        #
        #                               # #         # #         # #         # #              # #             # #             # #         # #
        #                                  # #         # #         # #         # #        # #             # #             # #         # #
        #                                    X #         # X         # #         # #    X #             # X             # #         # #
        #                                    # #         # #         X #         # X    # #             # #             X #         # X
        XXXXXXX,            XXXXXXX,    _______,    _______,    _______,    _______,    _______,        _______,        _______,    _______,    XXXXXXX,    XXXXXXX,
    ],
]


if __name__ == '__main__':
    keyboard.go()
