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
from overlay import *


class Kml(object):  # --Document--
    """The main class that represents a KML file.
    The base feature is a document, all arguments and properties are the same as that of a [Document].

    Arguments:
    name                -- string (default None)
    visibility          -- int (default 1)
    open                -- int (default 0)
    atomauthor          -- string (default None)
    atomlink            -- string (default None)
    address             -- string (default None)
    xaladdressdetails   -- string in xal format (default None)
    phonenumber         -- string (default None)
    snippet             -- string (default None)
    description         -- string (default None)
    camera              -- [Camera] (default None)
    lookat              -- [LookAt] (default None)
    timestamp           -- [TimeStamp] (default None)
    timespan            -- [TimeStamp] (default None)
    region              -- [Region] (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    liststyle           -- [ListStyle] (default None)
    document            -- [Document] (default [Document])

    Public Methods:
    newpoint()          -- Creates a new [Point] and attaches it to the feature
    newlinestring()     -- Creates a new [LineString] and attaches it to the feature
    newpolygon()        -- Creates a new [Polygon] and attaches it to the feature
    newmultigeometry()  -- Creates a new [MultiGeometry] and attaches it to the feature
    newgroundoverlay()  -- Creates a new [GroundOverlay] and attaches it to the feature
    newscreenoverlay()  -- Creates a new [ScreenOverlay] and attaches it to the feature
    newphotooverlay()   -- Creates a new [PhotoOverlay] and attaches it to the feature
    save(path)          -- Saves to a KML file with the given path
    savekmz(path)       -- Saves to a KMZ file with the given path

    """

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
        kml_tag = 'xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"'
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

    def newmultigeometry(self, **kwargs):
        """Creates a new Polygon and attaches it to the feature."""
        multi = MultiGeometry(**kwargs)
        multi._parent = self
        self._feature.addfeature(multi)
        return multi

    def newgroundoverlay(self, **kwargs):
        """Creates a new GroundOverlay and attaches it to the feature."""
        groundover = GroundOverlay(**kwargs)
        groundover._parent = self
        self._feature.addfeature(groundover)
        return groundover

    def newscreenoverlay(self, **kwargs):
        """Creates a new ScreenOverlay and attaches it to the feature."""
        screenover = ScreenOverlay(**kwargs)
        screenover._parent = self
        self._feature.addfeature(screenover)
        return screenover

    def newphotooverlay(self, **kwargs):
        """Creates a new PhotoOverlay and attaches it to the feature."""
        photoover = PhotoOverlay(**kwargs)
        photoover._parent = self
        self._feature.addfeature(photoover)
        return photoover
