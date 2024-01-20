print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.row_pins = (
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    )
keyboard.col_pins = (
    board.GP22,
    board.GP20,
    board.GP19,
    board.GP18,
    board.GP17,
    board.GP16,
    )

keyboard.diode_orientation = DiodeOrientation.COL2ROW
#Test Map Left
#keyboard.keymap = [
#    [   #0
#        KC.N9,  KC.N1,   KC.N2,   KC.N3, KC.N4, KC.N5,
#        KC.N8,  KC.Q,    KC.W,    KC.E,  KC.R,  KC.T,
#        KC.N7,  KC.A,    KC.S,    KC.D,  KC.F,  KC.G,
#        KC.N6,  KC.Z,    KC.X,    KC.C,  KC.V,  KC.B,
#        KC.NO,  KC.NO,   KC.I,    KC.U,  KC.P,  KC.O,
#        KC.NO,  KC.NO,   KC.Y,    KC.H,  KC.K,  KC.L,
#    ]
#]
keyboard.keymap = [
    [   #0
        KC.N6,  KC.N7,   KC.N8,   KC.N9, KC.N0, KC.LBRACKET,
        KC.Y,  KC.U,    KC.I,    KC.O,  KC.P,  KC.RBRACKET,
        KC.H,  KC.J,    KC.K,    KC.L,    KC.SCOLON,  KC.QUOTE,
        KC.N,  KC.M,    KC.COMMA,    KC.DOT,  KC.SLASH,  KC.BSLASH,
        KC.SPACE,  KC.ESC,   KC.MINUS,    KC.EQUAL,  KC.NO,  KC.NO,
        KC.RCTL,  KC.PGUP,   KC.RALT,    KC.PGDN,  KC.NO,  KC.NO,
    ]
]
if __name__ == '__main__':
    keyboard.go()
