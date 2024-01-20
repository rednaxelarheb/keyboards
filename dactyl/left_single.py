print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

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
        KC.ESC,  KC.N1,   KC.N2,   KC.N3, KC.N4, KC.N5,
        KC.GRV,  KC.Q,    KC.W,    KC.E,  KC.R,  KC.T,
        KC.LALT,  KC.A,    KC.S,    KC.D,  KC.F,  KC.G,
        KC.LGUI,  KC.Z,    KC.X,    KC.C,  KC.V,  KC.B,
        KC.NO,  KC.NO,   KC.I,    KC.U,  KC.BSPC,  KC.SPC,
        KC.NO,  KC.NO,   KC.DEL,    KC.ENT,  KC.PGDN,  KC.TAB,
    ]
]
if __name__ == '__main__':
    keyboard.go()
