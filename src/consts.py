"""
MIT License: Copyright (c) 2022 JustKoi (iamjustkoi) <https://github.com/iamjustkoi>
Full license text available in "LICENSE" file packaged with the program.
"""
from typing import NewType


CURRENT_VERSION = '0.0.4-alpha'

ANKI_LEGACY_VER = 35


class String:
    TOOLBAR_OPTIONS = '&Leech Toolkit Options...'
    VIEW_LEECHES = 'Leech Cards'
    BUTTON_SHORTCUT_HINT = 'Shortcut key'
    LAPSES_DECREASED = r"Card's lapses decreased"
    LAPSES_RESET = r"Card's lapses reset"

    LEECHES_URL = 'viewleeches'


PosType = NewType('PosIndex', int)
DEFAULT = PosType(0)
LEFT = PosType(1)
RIGHT = PosType(2)
MARKER_POS_STYLES = {DEFAULT: 'unset', LEFT: 'left', RIGHT: 'right'}

ReverseType = NewType('ReverseType', int)
REV_DECREASE = ReverseType(0)
REV_RESET = ReverseType(1)

CARD_TYPE_STR = {0: 'new', 1: 'learn', 2: 'review', 3: 'relearn'}

LEECH_TAG = 'leech'


class Config:
    TOOLBAR_ENABLED = 'show tools menu options'

    SHOW_LEECH_MARKER = 'show leech marker'
    USE_ALMOST_MARKER = 'show almost leech marker'
    ONLY_SHOW_BACK_MARKER = 'show marker on back'
    MARKER_POSITION = 'almost mark position'

    SHOW_BROWSE_BUTTON = 'show browse button'
    BROWSE_BUTTON_ON_BROWSER = 'show browse button on browser'
    BROWSE_BUTTON_ON_OVERVIEW = 'show browse button on overview'

    REVERSE_ENABLED = 'reverse enabled'
    REVERSE_METHOD = 'reverse type'
    REVERSE_THRESHOLD = 'reverse threshold'
    REVERSE_CONS_ANS = 'reverse consecutive answers'

    LEECH_ACTIONS = 'leech actions'

    DEFAULT_CONFIG = {
        TOOLBAR_ENABLED: True,
        SHOW_LEECH_MARKER: True,
        USE_ALMOST_MARKER: True,
        ONLY_SHOW_BACK_MARKER: True,
        MARKER_POSITION: DEFAULT,
        SHOW_BROWSE_BUTTON: True,
        BROWSE_BUTTON_ON_BROWSER: True,
        BROWSE_BUTTON_ON_OVERVIEW: True,
        REVERSE_ENABLED: True,
        REVERSE_THRESHOLD: 4,
        REVERSE_CONS_ANS: 2,
        REVERSE_METHOD: 0,
        LEECH_ACTIONS: {{'flag': [0]}}
    }


class Action:
    FLAG = 'flag'
