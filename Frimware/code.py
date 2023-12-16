print("Starting")

import board
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
Media_Keys = MediaKeys()
keyboard.modules = [layers, encoder_handler, Media_Keys, ]


keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13,board.GP14,board.GP15,board.GP16,board.GP17,
)
keyboard.row_pins = (board.GP28, board.GP27, board.GP26, board.GP22, board.GP21)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# I2C example
#import busio
#SDA = board.GP0\
#SCL = board.GP1
#i2c = busio.I2C(SCL, SDA)
#encoder_handler.i2c = ((i2c, 0x36, False),)

# encoder_handler.divisor = 2 # for encoders with more precision
encoder_handler.pins = ((board.GP20, board.GP19, board.GP18, False,),)

# keyboard.tap_time = 250
# keyboard.debug_enabled = False


# Filler keys
_______ = KC.TRNS
xxxxxxx = KC.NO
tbdtbd = KC.AJHK 
KPEQAS= KC.KP_EQUAL_AS400


# Layers
LYR_COLMAK, LYR_QWERTY, LYR_NUM, LYR_FN = 0, 1, 2, 3

TO_COLMAK = KC.TO(LYR_COLMAK)
MT_QWERTY = KC.TO(LYR_QWERTY)
TG_NUM = KC.TG(LYR_NUM)
FN = KC.MO(LYR_FN)

# Keymap

keyboard.keymap = [
    # COLMAK Layer
    [
        KC.ESC  , KC.F1   , KC.F2   , KC.F3   , KC.F4   , KC.F5  ,    KC.DEL  , KC.GRV  , KC.EQL  , KC.PSLS    , KC.F6  , KC.F7   , KC.F8      , KC.F9      , KC.F10  , KC.F11  , KC.F12  , KC.MUTE   ,
        KC.TAB  , KC.Q    , KC.W    , KC.F    , KC.P    , KC.G   ,    KC.N7   , KC.N8   , KC.N9   , KC.PAST    , KC.J   , KC.L    , KC.U       , KC.Y       , KC.SCLN , KC.LBRC , KC.RBRC , KC.BSLS   ,
        KC.BSPC , KC.A    , KC.R    , KC.S    , KC.T    , KC.D   ,    KC.N4   , KC.N5   , KC.N6   , KC.MINS    , KC.H   , KC.N    , KC.E       , KC.I       , KC.O    , KC.QUOT , xxxxxxx , KC.ENTER  ,
        KC.LSFT , KC.Z    , KC.X    , KC.C    , KC.V    , KC.B   ,    KC.N1   , KC.N2   , KC.N3   , KC.PPLS    , KC.K   , KC.M    , KC.COMMA   , KC.DOT     , KC.SLSH , KC.RSFT , KC.UP   , MT_QWERTY ,
        KC.LCTL , KC.LGUI , KC.LALT , FN      , xxxxxxx , KC.SPC ,    KC.N0   , KC.PDOT , KC.PENT , TG_NUM     , KC.SPC , xxxxxxx , KC.WINMENU , KC.RALT    , KC.RCTL , KC.LEFT , KC.DOWN , KC.RGHT   ,
    ],
    # QWERTY Layer
    [
        KC.ESC  , KC.F1   , KC.F2   , KC.F3   , KC.F4   , KC.F5  ,    KC.DEL  , KC.GRV  , KC.EQL  , KC.PSLS    , KC.F6  , KC.F7   , KC.F8      , KC.F9      , KC.F10  , KC.F11  , KC.F12  , KC.MUTE  ,
        KC.TAB  , KC.Q    , KC.W    , KC.E    , KC.R    , KC.T   ,    KC.N7   , KC.N8   , KC.N9   , KC.PAST    , KC.Y   , KC.U    , KC.I       , KC.O       , KC.P    , KC.LBRC , KC.RBRC , KC.BSLS   ,
        KC.BSPC , KC.A    , KC.S    , KC.D    , KC.F    , KC.G   ,    KC.N4   , KC.N5   , KC.N6   , KC.MINS    , KC.H   , KC.J    , KC.K       , KC.L       , KC.SCLN , KC.QUOT , xxxxxxx , KC.ENTER  ,
        KC.LSFT , KC.Z    , KC.X    , KC.C    , KC.V    , KC.B   ,    KC.N1   , KC.N2   , KC.N3   , KC.PPLS    ,  KC.N  , KC.M    , KC.COMMA   , KC.DOT     , KC.SLSH , KC.RSFT , KC.UP   , TO_COLMAK ,
        KC.LCTL , KC.LGUI , KC.LALT , FN      , xxxxxxx , KC.SPC ,    KC.N0   , KC.PDOT , KC.PENT , TG_NUM     , KC.SPC , xxxxxxx , KC.WINMENU , KC.RALT    , KC.RCTL , KC.LEFT , KC.DOWN , KC.RGHT   ,
    ],
    # NumPad Layer
    [
        _______ , _______ , _______ , _______ , _______ , _______ ,    KC.DEL   , KC.NLCK  , KC.EQL   , KC.PSLS    , _______ , _______ , _______ , _______ , _______ , _______ , _______ , KC.MUTE   ,
        _______ , _______ , _______ , _______ , _______ , _______ ,    KC.KP_7  , KC.KP_8  , KC.KP_9  , KC.PAST    , _______ , _______ , _______ , _______ , _______ , _______ , _______ , _______   ,
        _______ , _______ , _______ , _______ , _______ , _______ ,    KC.KP_4  , KC.KP_5  , KC.KP_6  , KC.PMNS    , _______ , _______ , _______ , _______ , _______ , _______ , xxxxxxx , _______   ,
        _______ , _______ , _______ , _______ , _______ , _______ ,    KC.KP_1  , KC.KP_2  , KC.KP_3  , KC.PPLS    , _______ , _______ , _______ , _______ , _______ , _______ , KC.UP   , TO_COLMAK ,
        _______ , _______ , _______ , FN      , xxxxxxx , _______ ,    KC.KP_0  , KC.PDOT  , KC.PENT  , TG_NUM     , _______ , xxxxxxx , _______ , _______ , _______ , KC.LEFT , KC.DOWN , KC.RGHT   ,
    ],
    # FN Layer
    [
        KC.ESC  , KC.MPRV , KC.MPLY , KC.MNXT , KC.BRID , KC.BRIU  ,    _______  , _______  , _______  , _______    , KC.PSCR , KC.SLCK  , KC.PAUS , KC.F9   , KC.F10  , KC.F11  , KC.F12  , xxxxxxx ,
        _______ , _______ , _______ , _______ , _______ , _______  ,    _______  , _______  , _______  , _______    , _______ , _______  , _______ , _______ , _______ , _______ , _______ , _______ ,
        _______ , _______ , _______ , _______ , _______ , _______  ,    _______  , _______  , _______  , _______    , _______ , _______  , _______ , _______ , _______ , _______ , xxxxxxx , _______ ,
        KC.CAPS , _______ , _______ , _______ , _______ , _______  ,    _______  , _______  , _______  , _______    , _______ , _______  , _______ , _______ , _______ , _______ , KC.UP   , _______ ,
        _______ , _______ , _______ , _______ , xxxxxxx , KC.SPC   ,    _______  , _______  , _______  , _______    , KC.SPC  , xxxxxxx  , _______ , _______ , _______ , KC.LEFT , KC.DOWN , KC.RGHT ,
    ]

]

# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = [ ((KC.VOLD, KC.VOLU, xxxxxxx),), # COLMAK
                        ((KC.VOLD, KC.VOLU, xxxxxxx),), # QWERTY
                        ((KC.VOLD, KC.VOLU, xxxxxxx),), # NumPad
                        ((KC.VOLD, KC.VOLU, xxxxxxx),), # FN
                        ]

if __name__ == "__main__":
    keyboard.go()