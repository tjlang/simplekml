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
import xml.dom.minidom

class Kmlable(object):
    """Enables a subclass to be converted into KML."""
    _images = []
    _kmz = False

    def __init__(self):
        self._kml = {}

    def __str__(self):
        str = ""
        for var, val in self._kml.items():
            if val is not None:  # Exclude all variables that are None
                if var.endswith("_"):
                    str += "{0}".format(val)  # Use the variable's __str__ as is
                else:
                    if var in ['name', 'description', 'text']: # Parse value for HTML and convert
                        val = Kmlable._chrconvert(val)
                    elif (var == 'href' and os.path.exists(val) and Kmlable._kmz == True)\
                            or (var == 'targetHref' and os.path.exists(val) and Kmlable._kmz == True): # Check for local images
                        Kmlable._addimage(val)
                        val = os.path.join('files', os.path.split(val)[1])
                    str += "<{0}>{1}</{0}>".format(var, val)  # Enclose the variable's __str__ with the variables name
        return str

    @classmethod
    def _chrconvert(cls, text):
        return cgi.escape(text)

    @classmethod
    def _addimage(cls, image):
        Kmlable._images.append(image)

    @classmethod
    def _getimages(cls):
        return set(Kmlable._images)

    @classmethod
    def _clearimages(cls):
        Kmlable._images = []

    @classmethod
    def _setkmz(cls, kmz=True):
        Kmlable._kmz = kmz


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
    x                   -- float (default None)
    y                   -- float (default None)
    xunits              -- string from [Units] constants (default None)
    yunits              -- string from [Units] constants (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, **kwargs):
        super(HotSpot, self).__init__(**kwargs)


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
        self.maxlines = maxlines
        
    def __str__(self):
        return '<Snippet maxLines="{0}">{1}</Snippet>'.format(self.maxlines, self.content)


class KmlElement(xml.dom.minidom.Element):
   """Overrides the original Element to format the KML to Google Maps standards."""
   original_element = xml.dom.minidom.Element

   def writexml(self, writer, indent="", addindent="", newl=""):
       """If the element only contains a single string value then don't add white space around it."""
       if self.childNodes and len(self.childNodes) == 1 and\
          self.childNodes[0].nodeType == xml.dom.minidom.Node.TEXT_NODE:
           writer.write(indent)
           KmlElement.original_element.writexml(self, writer)
           writer.write(newl)
       else:
           KmlElement.original_element.writexml(self, writer, indent, addindent, newl)