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

import xml.dom.minidom
import zipfile
from simplekml.featgeom import *
from simplekml.abstractview import *
from simplekml.overlay import *
from simplekml.base import KmlElement


class Kml(object):  # --Document--
    """The main class that represents a KML file.
    The base feature is a document, all arguments and properties are the same as that of a [Document].

    Arguments:
    name                        -- string (default None)
    visibility                  -- int (default 1)
    open                        -- int (default 0)
    atomauthor                  -- string (default None)
    atomlink                    -- string (default None)
    address                     -- string (default None)
    xaladdressdetails           -- string in xal format (default None)
    phonenumber                 -- string (default None)
    snippet                     -- string (default None)
    description                 -- string (default None)
    camera                      -- [Camera] (default None)
    lookat                      -- [LookAt] (default None)
    timestamp                   -- [TimeStamp] (default None)
    timespan                    -- [TimeStamp] (default None)
    region                      -- [Region] (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style                       -- [Style] (default None)
    liststyle                   -- [ListStyle] (default None)
    document                    -- [Document] (default [Document])

    Public Methods:
    newpoint()                  -- Creates a new [Point] and attaches it to the document
    newlinestring()             -- Creates a new [LineString] and attaches it to the document
    newpolygon()                -- Creates a new [Polygon] and attaches it to the document
    newmultigeometry()          -- Creates a new [MultiGeometry] and attaches it to the document
    newgroundoverlay()          -- Creates a new [GroundOverlay] and attaches it to the document
    newscreenoverlay()          -- Creates a new [ScreenOverlay] and attaches it to the document
    newphotooverlay()           -- Creates a new [PhotoOverlay] and attaches it to the document
    newnetworklink()            -- Creates a new [NetworkLink] and attaches it to the document
    kml(format=True)            -- Returns the generated kml as a string (if format is False, KML is generated as one line)
    save(path, format=True)     -- Saves to a KML file with the given path (if format is False, KML is generated as one line)
    savekmz(path, format=True)  -- Saves to a KMZ file with the given path (if format is False, KML is generated as one line)

    """

    def __init__(self, **kwargs):
        self._feature = Document(**kwargs)

    @property
    def document(self):
        return self._feature

    @document.setter
    def document(self, doc):
        self._feature = doc

    def _genkml(self, format=True):
        """Returns the generated kml as a string as a single line or formatted."""
        kml_tag = 'xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"'
        xmlstr = "<kml {0}>{1}</kml>".format(kml_tag, self._feature.__str__())
        if format:
           xml.dom.minidom.Element = KmlElement
           s = xml.dom.minidom.parseString(xmlstr)
           result = s.toprettyxml(indent="    ", newl="\n", encoding="UTF-8")
           return result
        else:
            return xmlstr

    def kml(self, format=True):
        """Returns a string containing the KML."""
        Kmlable._setkmz(False)
        return self._genkml(format).decode("utf-8")

    def save(self, path, format=True):
        """Save the kml to the given file."""
        Kmlable._setkmz(False)
        out = self._genkml(format)
        f = open(path, 'wb')
        try:
            f.write(out)
        finally:
            f.close()

    def savekmz(self, path, format=True):
        """Save the kml as a kmz to the given file."""
        Kmlable._setkmz()
        out = self._genkml(format)
        kmz = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
        kmz.writestr("doc.kml", out)
        for image in Kmlable._getimages():
            kmz.write(image, os.path.join('files', os.path.split(image)[1]))
        kmz.close()
        Kmlable._clearimages()

    def newdocument(self, **kwargs):
        """Creates a new Document and attaches it to the document."""
        return self.document.newdocument(**kwargs)

    def newfolder(self, **kwargs):
        """Creates a new Folder and attaches it to the document."""
        return self.document.newfolder(**kwargs)

    def newpoint(self, **kwargs):
        """Creates a new Point and attaches it to the document."""
        return self.document.newpoint(**kwargs)

    def newlinestring(self, **kwargs):
        """Creates a new Linestring and attaches it to the document."""
        return self.document.newlinestring(**kwargs)

    def newpolygon(self, **kwargs):
        """Creates a new Polygon and attaches it to the document."""
        return self.document.newpolygon(**kwargs)

    def newmultigeometry(self, **kwargs):
        """Creates a new Polygon and attaches it to the document."""
        return self.document.newmultigeometry(**kwargs)

    def newgroundoverlay(self, **kwargs):
        """Creates a new GroundOverlay and attaches it to the document."""
        return self.document.newgroundoverlay(**kwargs)

    def newscreenoverlay(self, **kwargs):
        """Creates a new ScreenOverlay and attaches it to the document."""
        return self.document.newscreenoverlay(**kwargs)

    def newphotooverlay(self, **kwargs):
        """Creates a new PhotoOverlay and attaches it to the document."""
        return self.document.newphotooverlay(**kwargs)

    def newnetworklink(self, **kwargs):
        """Creates a new NetworkLink and attaches it to the document."""
        return self.document.newnetworklink(**kwargs)

    def newmodel(self, **kwargs):
        """Creates a new NetworkLink and attaches it to the document."""
        return self.document.newmodel(**kwargs)