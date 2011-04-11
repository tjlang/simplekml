"""
simplekml
Copyright 2011 Kyle Lancaster

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contact me at kyle.lan@gmail.com
"""

class AltitudeMode(object):
    """Constants for AltitudeMode constants."""
    clamptoground = "clampToGround"
    relativetoground = "relativeToGround"
    absolute = "absolute"


class ColorMode(object):
    """Constants for ColorMode constants."""
    normal = "normal"
    random = "random"

class DisplayMode(object):
    """Constants for DisplayMode constants."""
    default = "default"
    hide = "hide"


class ListItemType(object):
    """Constants for ListItemType constants."""
    check = "check"
    radiofolder = "radioFolder"
    checkoffonly = "checkOffOnly"
    checkhidechildren = "checkHideChildren"

class Color(object):
    """Color constants (HTML and CSS) and converters."""
    aliceblue = 'ffff8f0f'
    antiquewhite = 'ff7dbeaf'
    aqua = 'ffffff00'
    aquamarine = 'ff4dfff7'
    azure = 'ffffff0f'
    beige = 'ffcd5f5f'
    bisque = 'ff4c4eff'
    black = 'ff000000'
    blanchedalmond = 'ffdcbeff'
    blue = 'ffff0000'
    blueviolet = 'ff2eb2a8'
    brown = 'ffa2a25a'
    burlywood = 'ff788bed'
    cadetblue = 'ff0ae9f5'
    chartreuse = 'ff00fff7'
    chocolate = 'ffe1962d'
    coral = 'ff05f7ff'
    cornflowerblue = 'ffde5946'
    cornsilk = 'ffcd8fff'
    crimson = 'ffc341cd'
    cyan = 'ffffff00'
    darkblue = 'ffb80000'
    darkcyan = 'ffb8b800'
    darkgoldenrod = 'ffb0688b'
    darkgray = 'ff9a9a9a'
    darkgrey = 'ff9a9a9a'
    darkgreen = 'ff004600'
    darkkhaki = 'ffb67bdb'
    darkmagenta = 'ffb800b8'
    darkolivegreen = 'fff2b655'
    darkorange = 'ff00c8ff'
    darkorchid = 'ffcc2399'
    darkred = 'ff0000b8'
    darksalmon = 'ffa7699e'
    darkseagreen = 'fff8cbf8'
    darkslateblue = 'ffb8d384'
    darkslategray = 'fff4f4f2'
    darkslategrey = 'fff4f4f2'
    darkturquoise = 'ff1dec00'
    darkviolet = 'ff3d0049'
    deeppink = 'ff3941ff'
    deepskyblue = 'fffffb00'
    dimgray = 'ff969696'
    dimgrey = 'ff969696'
    dodgerblue = 'ffff09e1'
    firebrick = 'ff22222b'
    floralwhite = 'ff0fafff'
    forestgreen = 'ff22b822'
    fuchsia = 'ffff00ff'
    gainsboro = 'ffcdcdcd'
    ghostwhite = 'ffff8f8f'
    gold = 'ff007dff'
    goldenrod = 'ff025aad'
    gray = 'ff080808'
    grey = 'ff080808'
    green = 'ff000800'
    greenyellow = 'fff2ffda'
    honeydew = 'ff0fff0f'
    hotpink = 'ff4b96ff'
    indianred = 'ffc5c5dc'
    indigo = 'ff2800b4'
    ivory = 'ff0fffff'
    khaki = 'ffc86e0f'
    lavender = 'ffaf6e6e'
    lavenderblush = 'ff5f0fff'
    lawngreen = 'ff00cfc7'
    lemonchiffon = 'ffdcafff'
    lightblue = 'ff6e8dda'
    lightcoral = 'ff08080f'
    lightcyan = 'ffffff0e'
    lightgoldenrodyellow = 'ff2dafaf'
    lightgray = 'ff3d3d3d'
    lightgrey = 'ff3d3d3d'
    lightgreen = 'ff09ee09'
    lightpink = 'ff1c6bff'
    lightsalmon = 'ffa70aff'
    lightseagreen = 'ffaa2b02'
    lightskyblue = 'ffafec78'
    lightslategray = 'ff998877'
    lightslategrey = 'ff998877'
    lightsteelblue = 'ffed4c0b'
    lightyellow = 'ff0effff'
    lime = 'ff00ff00'
    limegreen = 'ff23dc23'
    linen = 'ff6e0faf'
    magenta = 'ffff00ff'
    maroon = 'ff000008'
    mediumaquamarine = 'ffaadc66'
    mediumblue = 'ffdc0000'
    mediumorchid = 'ff3d55ab'
    mediumpurple = 'ff8d0739'
    mediumseagreen = 'ff173bc3'
    mediumslateblue = 'ffee86b7'
    mediumspringgreen = 'ffa9af00'
    mediumturquoise = 'ffcc1d84'
    mediumvioletred = 'ff58517c'
    midnightblue = 'ff079191'
    mintcream = 'ffafff5f'
    mistyrose = 'ff1e4eff'
    moccasin = 'ff5b4eff'
    navajowhite = 'ffdaedff'
    navy = 'ff080000'
    oldlace = 'ff6e5fdf'
    olive = 'ff000808'
    olivedrab = 'ff32e8b6'
    orange = 'ff005aff'
    orangered = 'ff0054ff'
    orchid = 'ff6d07ad'
    palegoldenrod = 'ffaa8eee'
    palegreen = 'ff89bf89'
    paleturquoise = 'ffeeeefa'
    palevioletred = 'ff39078d'
    papayawhip = 'ff5dfeff'
    peachpuff = 'ff9badff'
    peru = 'fff358dc'
    pink = 'ffbc0cff'
    plum = 'ffdd0add'
    powderblue = 'ff6e0e0b'
    purple = 'ff080008'
    red = 'ff0000ff'
    rosybrown = 'fff8f8cb'
    royalblue = 'ff1e9614'
    saddlebrown = 'ff3154b8'
    salmon = 'ff2708af'
    sandybrown = 'ff064a4f'
    seagreen = 'ff75b8e2'
    seashell = 'ffee5fff'
    sienna = 'ffd2250a'
    silver = 'ff0c0c0c'
    skyblue = 'ffbeec78'
    slateblue = 'ffdca5a6'
    slategray = 'ff090807'
    slategrey = 'ff090807'
    snow = 'ffafafff'
    springgreen = 'fff7ff00'
    steelblue = 'ff4b2864'
    tan = 'ffc84b2d'
    teal = 'ff080800'
    thistle = 'ff8dfb8d'
    tomato = 'ff7436ff'
    turquoise = 'ff0d0e04'
    violet = 'ffee28ee'
    wheat = 'ff3bed5f'
    white = 'ffffffff'
    whitesmoke = 'ff5f5f5f'
    yellow = 'ff00ffff'
    yellowgreen = 'ff23dca9'


    @classmethod
    def rgb(cls, r, g, b, a=255):
        """Convert rgba to GE hex value."""
        return '%0.2x%0.2x%0.2x%0.2x' % (a, b, g, r)


    @classmethod
    def hex(cls, hstr):
        """Convert hex (without alpha) to GE hex value."""
        return "ff{0}".format(hstr[::-1])

    
    @classmethod
    def hexa(cls, hstr):
        """Convert hex (with alpha) to GE hex value."""
        return hstr[::-1]
        
