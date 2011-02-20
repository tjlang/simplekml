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

    def save(self, path):
        kml_tag = 'xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"'
        xmlstr = "<kml {0}>{1}</kml>".format(kml_tag, self._feature.__str__())
        s = parseString(xmlstr)
        out = s.toprettyxml(indent="    ", newl="\n", encoding="UTF-8")
        with open(path, 'w') as f:
            f.write(str(out))

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



def main():
    kml = Kml()
    doc = kml.newdocument(name="Doc Test")
    doc = doc.newdocument()
    doc.name = "Doc2 Test"
    doc.description = "Doc2 Description"

    fol = kml.newfolder()
    fol.name = "Folder Test"
    fol.description = "Description of Test Folder"
    fol = fol.newfolder(name='Folder Nested Tests', description="Description of Nested Folder")

    fol = doc.newfolder(name='Point Tests', description="Description of Point Folder")
    pnt = fol.newpoint(name="p1", description='d1', coords=[(10.0,10.0)]) #TODO: Test AbstractView
    pnt = fol.newpoint()
    pnt.name = "p2"
    pnt.description = "d2"
    pnt.coords = [(15.0,15.0)]
    pnt.style.labelstyle.color = 'ff0000ff'
    pnt.labelstyle.scale = 2
    pnt.labelstyle.colormode = ColorMode.random
    pnt.style.iconstyle.color = 'ffff00ff'
    pnt.iconstyle.heading = 45
    pnt.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/arrow.png'

    pnt2 = kml.newpoint(name="p3", description="Same style as p2", coords=[(12.0,12.0)])
    pnt2.style = pnt.style

    pnt = kml.newpoint(name="p4", description="Style from class", coords=[(13.0,13.0)])
    style = Style()
    style.labelstyle.color = "ff00ffff"
    pnt.style = style

    fol = doc.newfolder(name="LineString Tests", description="Description of LineString Folder")
    lin = fol.newlinestring(name='l1', description='d1', coords=[(10.0,10.0), (15.0,15.0)])
    lin = fol.newlinestring()
    lin.name = "l2"
    lin.description = 'd2'
    lin.coords = [(10.0,15.0), (15.0,20.0)]
    lin.altitudemode = AltitudeMode.clamptoground
    lin.style.linestyle.width = 10
    lin.linestyle.color = "ff00ffff"

    fol = doc.newfolder(name="Polygon Tests", description="Description of Polgon Folder")
    pol = fol.newpolygon(name='p1', description='d1', outerboundaryis=[(12.0,15.0), (11.0,14.0), (13.0,14.0),(12.0,15.0)])
    pol = fol.newpolygon()
    pol.name = 'p2'
    pol.description = 'd2'
    pol.outerboundaryis = [(13.0,14.0), (13.0,16.0), (12.0,15.0),(13.0,14.0)]
    pol.innerboundaryis = [(12.7,14.9), (12.7,15.4), (12.4,15.0),(12.7,14.9)]
    pol.style.linestyle.color = 'ff0000ff'
    pol.linestyle.width = 5
    pol.style.polystyle.color = 'ffff00ff'

    kml.save("tests.kml")


    kml = Kml()

    kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])

    lin = kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch",
                            coords=[(18.43312,-33.98924), (18.43224,-33.98914), (18.43144,-33.98911), (18.43095,-33.98904)])
    
    pol = kml.newpolygon(name="Atrium Garden",
                         outerboundaryis=[(18.43348,-33.98985), (18.43387,-33.99004262216968), (18.43410,-33.98972), (18.43371,-33.98952), (18.43348,-33.98985)],
                         innerboundaryis=[(18.43360,-33.98982), (18.43386,-33.98995), (18.43401,-33.98974), (18.43376,-33.98962), (18.43360,-33.98982)])

    kml.save("c://botanicalgarden.kml")


if __name__ == "__main__":
    main()