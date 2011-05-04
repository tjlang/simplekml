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

import os
import cgi

class Kmlable(object):
    """Enables a subclass to be converted into KML."""
    images = []
    kmz = False

    def __str__(self):
        str = ""
        for var, val in vars(self).items():
            if not var.startswith("_"):  # Exclude all variables with a leading underscore
                if val is not None:  # Exclude all variables that are None
                    if var.endswith("_"):
                        str += "{0}".format(val)  # Use the variable's __str__ as is
                    else:
                        if var in ['name', 'description', 'text']: # Parse value for HTML and convert
                            val = Kmlable.chrconvert(val)
                        elif var == 'href' and os.path.exists(val) and Kmlable.kmz == True: # Check for local images
                            Kmlable.addimage(val)
                            val = os.path.join('files', os.path.split(val)[1])
                        elif var.startswith('gx'): # Change all variables starting with gx to include the colon
                            var = 'gx:{0}'.format(var[2:])
                        str += "<{0}>{1}</{0}>".format(var, val)  # Enclose the variable's __str__ with the variables name
        return str

    @classmethod
    def chrconvert(cls, text):
        return cgi.escape(text)

    @classmethod
    def addimage(cls, image):
        Kmlable.images.append(image)

    @classmethod
    def getimages(cls):
        return set(Kmlable.images)

    @classmethod
    def clearimages(cls):
        Kmlable.images = []

    @classmethod
    def setkmz(cls, kmz=True):
        Kmlable.kmz = kmz


class Vector2(object):
    def __init__(self,
                 x=None,
                 y=None,
                 xunits=None,
                 yunits=None):
        self.x = x
        self.y = y
        self.xunits = xunits
        self.yunits = yunits

    def __str__(self):
        cname = self.__class__.__name__[0].lower() + self.__class__.__name__[1:]
        return '<{0} x="{1}" y="{2}" xunits="{3}" yunits="{4}" />'.format(cname, self.x, self.y, self.xunits, self.yunits)


class OverlayXY(Vector2): # --Document--
    """Specifies a point on (or outside of) the overlay image that is mapped to the screen coordinate [ScreenXY]

    Arguments:
    x                   -- int (default None)
    y                   -- int (default None)
    xunits              -- string from [Units] constants (default None)
    yunits              -- string from [Units] constants (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, **kwargs):
        super(OverlayXY, self).__init__(**kwargs)


class ScreenXY(Vector2): # --Document--
    """Specifies a point relative to the screen origin that the overlay image is mapped to.

    Arguments:
    x                   -- int (default None)
    y                   -- int (default None)
    xunits              -- string from [Units] constants (default None)
    yunits              -- string from [Units] constants (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, **kwargs):
        super(ScreenXY, self).__init__(**kwargs)


class RotationXY(Vector2): # --Document--
    """Point relative to the screen about which the screen overlay is rotated.

    Arguments:
    x                   -- int (default None)
    y                   -- int (default None)
    xunits              -- string from [Units] constants (default None)
    yunits              -- string from [Units] constants (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, **kwargs):

        super(RotationXY, self).__init__(**kwargs)


class Size(Vector2): # --Document--
    """Specifies the size of the image for the screen overlay.

    Arguments:
    x                   -- int (default None)
    y                   -- int (default None)
    xunits              -- string from [Units] constants (default None)
    yunits              -- string from [Units] constants (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, **kwargs):
        super(Size, self).__init__(**kwargs)

        
class HotSpot(Vector2): # --Document--
    """Specifies the position within the [Icon] that is "anchored" to the [Point].

    Arguments:
    x                   -- int (default None)
    y                   -- int (default None)
    xunits              -- string from [Units] constants (default None)
    yunits              -- string from [Units] constants (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, **kwargs):
        super(Vector2, self).__init__(**kwargs)


class Snippet(object): # --Document--
    """A short description of the feature.

    Arguments:
    content             -- string (default None)
    maxlines            -- int (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, content='', maxlines=2):
        self.content = content
        self.maxLines = maxlines

    @property
    def maxlines(self):
        return self.maxLines

    @maxlines.setter
    def maxlines(self, maxlines):
        self.maxLines = maxlines
        
    def __str__(self):
        return '<Snippet maxLines="{0}">{1}</Snippet>'.format(self.maxLines, self.content)