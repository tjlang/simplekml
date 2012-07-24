"""
Copyright 2011-2012 Kyle Lancaster

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
import codecs
import os

from simplekml.base import Kmlable, KmlElement, check
from simplekml.featgeom import Document, Container
from simplekml.makeunicode import u


class Kml(object):
    """The main class that represents a KML file.

    This class represents a KML file, and the compilation of the KML file will
    be done through this class. The base feature is a document, all arguments
    passed to the class on creation are the same as that of a
    :class:`simplekml.Document`. To change any properties after creation you can
    do so through the :attr:`simplekml.Kml.document` property
    (eg. `kml.document.name = "Test"`). For a description of what the
    arguments mean see the KML reference documentation published by Google:
    http://code.google.com/apis/kml/documentation/kmlreference.html

    Simple Example::

        from simplekml import Kml
        kml = Kml(name='KmlUsage')
        kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])  # A simple Point
        kml.save("KmlClass.kml")  # Saving
        kml.savekmz("KmlClass.kmz", format=False)  # Saving as KMZ
        print kml.kml()  # Printing out the kml to screen
    """

    def __init__(self, **kwargs):
        self._feature = Document(**kwargs)

    @property
    def document(self):
        """
        The top level item in the kml document.

        A top level document is required for a kml document, the default is an
        instance of :class:`simplekml.Document`. This property can be set to an
        instance of :class:`simplekml.Document` or :class:`simplekml.Folder`

        Example::

            import simplekml
            kml = simplekml.Kml()
            kml.document = simplekml.Folder(name = "Top Level Folder")
            kml.save('Document Replacement.kml')
        """
        return self._feature

    @document.setter
    @check(Container, True)
    def document(self, doc):
        self._feature = doc

    def _genkml(self, format=True):
        """Returns the kml as a string or "prettyprinted" if format = True."""
        kml_str = self._feature.__str__()
        xml_str = u("<kml {0}>{1}</kml>").format(Kmlable._getnamespaces(), kml_str)
        if format:
           KmlElement.patch()
           kml_str = xml.dom.minidom.parseString(xml_str.encode("utf-8"))
           KmlElement.unpatch()
           return kml_str.toprettyxml(indent="    ", newl="\n", encoding="UTF-8").decode("utf-8")
        else:
            return xml_str

    def parsetext(self, parse=True):
        """Sets the behavior of how text tags are parsed.

        If True the values of the text tags (<name>, <description> and <text>)
        are escaped, so that the values are rendered properly. If False, the
        values are left as is. If the CDATA element is being used to escape
        the text strings, them set this to False.
        """
        Kmlable._parsetext(parse)

    def kml(self, format=True):
        """Returns the kml as a string or "prettyprinted" if `format = True`.

        PrettyPrinted Example (default)::

            import simplekml
            kml = simplekml.Kml()
            pnt = kml.newpoint(name='A Point')
            pnt.coords = [(1.0, 2.0)]
            print kml.kml()

        PrettyPrinted Result:

        .. code-block:: xml

            <?xml version="1.0" encoding="UTF-8"?>
            <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
                <Document id="feat_1">
                    <Placemark id="feat_2">
                        <name>A Point</name>
                        <Point id="geom_0">
                            <coordinates>1.0,2.0,0.0</coordinates>
                        </Point>
                    </Placemark>
                </Document>
            </kml>

        Single Line Example::

            import simplekml
            kml = simplekml.Kml()
            pnt = kml.newpoint(name='A Point')
            pnt.coords = [(1.0, 2.0)]
            print kml.kml(False)

        Single Line Result:

        .. code-block:: xml

            <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2"><Document id="feat_1"><Placemark id="feat_2"><name>A Point</name><Point id="geom_0"><coordinates>1.0,2.0,0.0</coordinates></Point></Placemark></Document></kml>

        """
        Kmlable._setkmz(False)
        return self._genkml(format)

    def save(self, path, format=True):
        """Save the kml to the given file supplied by `path`.

        The KML is saved to a file in one long string if `format=False` else it
        gets saved "prettyprinted" (as formatted xml). This works the same as :func:`simplekml.Kml.kml`

        Usage::

            import simplekml
            kml = simplekml.Kml()
            kml.save("Saving.kml")
            #kml.save("Saving.kml", False)  # or this
        """
        Kmlable._setkmz(False)
        out = self._genkml(format)
        f = codecs.open(path, 'wb', 'utf-8')
        try:
            f.write(out)
        finally:
            f.close()

    def savekmz(self, path, format=True):
        """Save the kml as a kmz to the given file supplied by `path`.

        The KML is saved to a file in a long string if `format=False` else it
        gets saved "prettyprinted". This works the same as :func:`simplekml.Kml.kml`

        Usage::

            import simplekml
            kml = simplekml.Kml()
            kml.savekmz("Saving.kml")
            #kml.savekmz("Saving.kml", False)  # or this
        """
        Kmlable._setkmz()
        out = self._genkml(format).encode('utf-8')
        kmz = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
        kmz.writestr("doc.kml", out)
        for image in Kmlable._getimages():
            kmz.write(image, os.path.join('files', os.path.split(image)[1]))
        kmz.close()
        Kmlable._clearimages()

    def newdocument(self, **kwargs):
        """
        Creates a new :class:`simplekml.Document`.

        The document is attached to this KML document. The arguments are the same as for :class:`simplekml.Document`.
        See :class:`simplekml.Document` for usage.
        """
        return self.document.newdocument(**kwargs)

    def newfolder(self, **kwargs):
        """
        Creates a new :class:`simplekml.Folder`.

        The folder is attached to this KML document. The arguments are the same as those for :class:`simplekml.Folder`
        See :class:`simplekml.Folder` for usage.
        """
        return self.document.newfolder(**kwargs)

    def newpoint(self, **kwargs):
        """
        Creates a new :class:`simplekml.Point`.

        The point is attached to this KML document. The arguments are the same as those for :class:`simplekml.Point`
        See :class:`simplekml.Point` for usage.
        """
        return self.document.newpoint(**kwargs)

    def newlinestring(self, **kwargs):
        """
        Creates a new :class:`simplekml.LineString`.

        The linestring is attached to this KML document. The arguments are the same as for :class:`simplekml.LineString`
        See :class:`simplekml.LineString` for usage.
        """
        return self.document.newlinestring(**kwargs)

    def newpolygon(self, **kwargs):
        """
        Creates a new :class:`simplekml.Polygon`.

        The polygon is attached to this KML document. The arguments are the same as those for :class:`simplekml.Polygon`
        See :class:`simplekml.Polygon` for usage.
        """
        return self.document.newpolygon(**kwargs)

    def newmultigeometry(self, **kwargs):
        """
        Creates a new :class:`simplekml.MultiGeometry`.

        The multigeometry is attached to this KML document. The arguments are the same as
        for :class:`simplekml.MultiGeometry`. See :class:`simplekml.MultiGeometry` for usage.
        """
        return self.document.newmultigeometry(**kwargs)

    def newgroundoverlay(self, **kwargs):
        """
        Creates a new :class:`simplekml.GroundOverlay`.

        The groundoverlay is attached to this KML document. The arguments are the same as those
        for :class:`simplekml.GroundOverlay`. See :class:`simplekml.GroundOverlay` for usage.
        """
        return self.document.newgroundoverlay(**kwargs)

    def newscreenoverlay(self, **kwargs):
        """
        Creates a new :class:`simplekml.ScreenOverlay`.

        The screenoverlay is attached to this KML document. The arguments are the same as those
        for :class:`simplekml.ScreenOverlay`. See :class:`simplekml.ScreenOverlay` for usage.
        """
        return self.document.newscreenoverlay(**kwargs)

    def newphotooverlay(self, **kwargs):
        """
        Creates a new :class:`simplekml.PhotoOverlay`.

        The photooverlay is attached to this KML document. The arguments are the same as those
        for :class:`simplekml.PhotoOverlay`. See :class:`simplekml.PhotoOverlay` for usage.
        """
        return self.document.newphotooverlay(**kwargs)

    def newnetworklink(self, **kwargs):
        """
        Creates a new :class:`simplekml.NetworkLink`.

        The networklink is attached to this KML document. The arguments are the same as those
        for :class:`simplekml.NetworkLink`. See :class:`simplekml.NetworkLink` for usage.
        """
        return self.document.newnetworklink(**kwargs)

    def newmodel(self, **kwargs):
        """
        Creates a new :class:`simplekml.Model`.

        The model is attached to this KML document. The arguments are the
        same as those for :class:`simplekml.Model`
        """
        return self.document.newmodel(**kwargs)

    def newschema(self, **kwargs):
        """
        Creates a new :class:`simplekml.Schema`.

        The schem is attached to this KML document. The arguments are the
        same as those for :class:`simplekml.Schema`
        """
        return self.document.newschema(**kwargs)

    def newgxtrack(self, **kwargs):
        """
        Creates a new :class:`simplekml.GxTrack`.

        The gxtrack is attached to this KML document. The arguments are the same as those for :class:`simplekml.GxTrack`
        See :class:`simplekml.GxTrack` for usage.
        """
        return self.document.newgxtrack(**kwargs)

    def newgxmultitrack(self, **kwargs):
        """
        Creates a new :class:`simplekml.GxMultiTrack`.

        The gxmultitrack is attached to this KML document. The arguments are the same as those
        for :class:`simplekml.GxMultiTrack`. See :class:`simplekml.GxMultiTrack` for usage.
        """
        return self.document.newgxmultitrack(**kwargs)

    def newgxtour(self, **kwargs):
        """
        Creates a new :class:`simplekml.GxTour`.

        The tour is attached to this KML document. The arguments are the same as those for :class:`simplekml.GxTour`
        See :class:`simplekml.GxTour` for usage.
        """
        return self.document.newgxtour(**kwargs)
