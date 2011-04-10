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
                        if var in ['name', 'description', 'text']:
                            val = Kmlable.chrconvert(val)
                        elif var == 'href' and os.path.exists(val) and Kmlable.kmz == True:
                            Kmlable.addimage(val)
                            val = os.path.join('files', os.path.split(val)[1])
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