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

from xml.dom.minidom import parseString
import zipfile

from featgeom import *
from abstractview import *


class Kml(object):
    """The main class that represents a KML file."""
    def __init__(self, **kwargs):
        self._feature = Document(**kwargs)

    @property
    def document(self):
        return self._feature

    @document.setter
    def document(self, doc):
        self._feature = doc

    def _genkml(self):
        """Returns the generated kml as a string."""
        kml_tag = 'xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"'
        xmlstr = "<kml {0}>{1}</kml>".format(kml_tag, self._feature.__str__())
        s = parseString(xmlstr)
        return s.toprettyxml(indent="    ", newl="\n", encoding="UTF-8")

    def save(self, path):
        """Save the kml to the given file."""
        Kmlable.setkmz(False)
        out = self._genkml()
        with open(path, 'w') as f:
            f.write(str(out))

    def savekmz(self, path):
        """Save the kml as a kmz to the given file."""
        Kmlable.setkmz()
        out = self._genkml()
        kmz = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
        kmz.writestr("doc.kml", out)
        for image in Kmlable.getimages():
            kmz.write(image, os.path.join('files', os.path.split(image)[1]))
        kmz.close()
        Kmlable.clearimages()

    def newdocument(self, **kwargs):
        """Creates a new Document and attaches it to the feature."""
        doc = Document(**kwargs)
        doc._parent = self
        self._feature.addfeature(doc)
        return doc

    def newfolder(self, **kwargs):
        """Creates a new Folder and attaches it to the feature."""
        fol = Folder(**kwargs)
        fol._parent = self
        self._feature.addfeature(fol)
        return fol

    def newpoint(self, **kwargs):
        """Creates a new Point and attaches it to the feature."""
        pnt = Point(**kwargs)
        pnt._parent = self
        self._feature.addfeature(pnt)
        return pnt

    def newlinestring(self, **kwargs):
        """Creates a new Linestring and attaches it to the feature."""
        ls = LineString(**kwargs)
        ls._parent = self
        self._feature.addfeature(ls)
        return ls

    def newpolygon(self, **kwargs):
        """Creates a new Polygon and attaches it to the feature."""
        poly = Polygon(**kwargs)
        poly._parent = self
        self._feature.addfeature(poly)
        return poly
