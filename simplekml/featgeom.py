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

from base import Kmlable
from constants import *
from styleselector import *
from coordinates import *

class Feature(Kmlable):
    """Base class extended by all features."""
    id = 0
    def __init__(self,
                 name=None,
                 visibility=1,
                 open=0,
                 description=None,
                 abstractview=None):
        self.name = name
        self.visibility = visibility
        self.open = open
        self.description = description
        self.AbstractView = abstractview
        self.styleUrl = None
        self._id = "feat_{0}".format(Feature.id)
        Feature.id += 1
        self._features = []
        self._schemas = []
        self._folders = []

    @property
    def styleurl(self):
        return self.styleUrl

    @styleurl.setter
    def styleurl(self, styleurl):
        self.styleUrl = styleurl

    @property
    def abstractview(self):
        return self.styleUrl

    @abstractview.setter
    def abstractview(self, abview):
        self.AbstractView = abview

    def addfeature(self, feature):
        """Attaches the given feature to this feature."""
        if isinstance(feature, Geometry):
            self._features.append(feature._placemark)
            feature._parent = self
            if feature._style is not None:
                self.addschema(feature._style)
        else:
            self._features.append(feature)

    def addschema(self, schema):
        """Attaches the given schema (style) to this feature."""
        self._schemas.append(schema)

    def __str__(self):
        str = '<{0} id="{1}">'.format(self.__class__.__name__, self._id)
        str += super(Feature, self).__str__()
        for schema in self._schemas:
            str += schema.__str__()
        for folder in self._folders:
            str += folder.__str__()
        for feat in self._features:
            str += feat.__str__()
        str += "</{0}>".format(self.__class__.__name__)
        return str

    def newpoint(self, **kwargs):
        """Creates a new Point and attaches it to the feature."""
        pnt = Point(**kwargs)
        pnt._parent = self
        self.addfeature(pnt)
        return pnt

    def newlinestring(self, **kwargs):
        """Creates a new Linestring and attaches it to the feature."""
        ls = LineString(**kwargs)
        ls._parent = self
        self.addfeature(ls)
        return ls

    def newpolygon(self, **kwargs):
        """Creates a new Polygon and attaches it to the feature."""
        poly = Polygon(**kwargs)
        poly._parent = self
        self.addfeature(poly)
        return poly


class Container(Feature):
    """Base class, extended by Document and Folder."""
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

    def newfolder(self, **kwargs):
        """Creates a new Folder and attaches it to the feature."""
        fol = Folder(**kwargs)
        fol._parent = self
        self.addfeature(fol)
        return fol

    def newdocument(self, **kwargs):
        """Creates a new Document and attaches it to the feature."""
        doc = Document(**kwargs)
        doc._parent = self
        self.addfeature(doc)
        return doc

class Document(Container):
    """A container for features and styles."""
    def __init__(self, **kwargs):
        super(Document, self).__init__(**kwargs)


class Folder(Container):
    """A container for features."""
    def __init__(self, **kwargs):
        super(Folder, self).__init__(**kwargs)


class Placemark(Feature):
    """A Placemark is a Feature with associated Geometry."""
    def __init__(self, geometry=None, **kwargs):
        super(Placemark, self).__init__(**kwargs)
        self.Geometry_ = geometry

    @property
    def geometry(self):
        return self.Geometry_

    @geometry.setter
    def geometry(self, geom):
        self.Geometry_ = geom

    def setStyle(self, style):
        self.styleUrl = "#{0}".format(style.getId())


class Geometry(Kmlable):
    """Base class for all Geometries."""
    id = 0
    def __init__(self,
                 name=None,
                 visibility=1,
                 description=None,
                 abstractview=None):
        self._id = "geom_{0}".format(Geometry.id)
        Geometry.id += 1
        self._placemark = Placemark(name=name,
                                    visibility=visibility,
                                    description=description,
                                    abstractview=abstractview)
        self._placemark.geometry = self
        self._parent = None
        self._style = None

    @property
    def name(self):
        return self._placemark.name

    @name.setter
    def name(self, name):
        self._placemark.name = name

    @property
    def visibility(self):
        return self._placemark.visibility

    @visibility.setter
    def visibility(self, visibility):
        self._placemark.visibility = visibility

    @property
    def description(self):
        return self._placemark.description

    @description.setter
    def description(self, description):
        self._placemark.description = description

    @property
    def abstractview(self):
        return self._placemark.AbstractView

    @abstractview.setter
    def abstractview(self, abstractview):
        self._placemark.AbstractView = abstractview

    @property
    def style(self):
        if self._style is None:
            self._style = Style()
            self._placemark.setStyle(self._style)
            if self._parent is not None:
                self._parent.addschema(self._style)
        return self._style

    @style.setter
    def style(self, style):
        self._placemark.setStyle(style)
        if self._parent is not None:
            self._parent.addschema(style)
        self._style = style

    @property
    def iconstyle(self):
        return self.style.iconstyle

    @iconstyle.setter
    def iconstyle(self, iconstyle):
        self.style.iconstyle = iconstyle

    @property
    def labelstyle(self):
        return self.style.labelstyle

    @labelstyle.setter
    def labelstyle(self, labelstyle):
        self.style.labelstyle = labelstyle

    @property
    def linestyle(self):
        return self.style.linestyle

    @linestyle.setter
    def linestyle(self, linestyle):
        self.style.linestyle = linestyle

    @property
    def polystyle(self):
        return self.style.polystyle

    @polystyle.setter
    def polystyle(self, polystyle):
        self.style.polystyle = polystyle

#    @property
#    def balloonstyle(self):
#        return self.style.balloonstyle
#
#    @balloonstyle.setter
#    def balloonstyle(self, balloonstyle):
#        self.style.balloonstyle = balloonstyle
#
#    @property
#    def liststyle(self):
#        return self.style.liststyle
#
#    @liststyle.setter
#    def liststyle(self, liststyle):
#        self.style.liststyle = liststyle
    
    @property
    def placemark(self):
        return self._placemark


class PointGeometry(Geometry):
    """Base class for any geometry requireing coordinates (not Polygon)."""
    def __init__(self,
                 coords=[], **kwargs):
        super(PointGeometry, self).__init__(**kwargs)
        self.coordinates = Coordinates()
        self.coordinates.addcoordinates(coords)

#    def addCoordinate(self, coord):
#        self.coordinates.addcoordinates([coord])
#
#    def addCoordinates(self, coords):
#        self.coordinates.addcoordinates([coords])

    @property
    def coords(self):
        return self.coordinates

    @coords.setter
    def coords(self, coords):
        self.coordinates = Coordinates()
        self.coordinates.addcoordinates(coords)


class LinearRing(PointGeometry):
    """A closed line string, typically the outer boundary of a Polygon."""
    def __init__(self, coords=[], **kwargs):
        super(LinearRing, self).__init__(coords, **kwargs)

    def __str__(self):
        str = '<LinearRing>'
        str += super(LinearRing, self).__str__()
        str += "</LinearRing>"
        return str


class Point(PointGeometry):
    """A geographic location defined by lon, lat, and altitude."""
    def __init__(self, extrude=0, **kwargs):
        super(Point, self).__init__(**kwargs)
        self.extrude = extrude

#    def addcoordinate(self, coord):
#        self.coordinates = Coordinates([coord])

    def __str__(self):
        str = '<Point id="{0}">'.format(self._id)
        str += super(Point, self).__str__()
        str += "</Point>"
        return str


class LineString(PointGeometry):
    """A connected set of line segments."""
    def __init__(self,
                 extrude=0,
                 tessellate=0,
                 altitudemode=AltitudeMode.clamptoground, **kwargs):
        super(LineString, self).__init__(**kwargs)
        self.extrude = extrude
        self.tessellate = tessellate
        self.altitudeMode = altitudemode

    def __str__(self):
        str = '<LineString id="{0}">'.format(self._id)
        str += super(LineString, self).__str__()
        str += "</LineString>"
        return str


class Polygon(Geometry):
    """A Polygon is defined by an outer boundary and/or an inner boundary."""
    def __init__(self,
                 extrude=0,
                 tessellate=0,
                 altitudemode=AltitudeMode.clamptoground,
                 outerboundaryis=[],
                 innerboundaryis=[], **kwargs):
        super(Polygon, self).__init__(**kwargs)
        self.extrude = extrude
        self.tessellate = tessellate
        self.altitudeMode = altitudemode
        self.outerBoundaryIs = LinearRing(outerboundaryis)
        self.innerBoundaryIs = LinearRing(innerboundaryis)

    @property
    def innerboundaryis(self):
        return self.innerBoundaryIs

    @innerboundaryis.setter
    def innerboundaryis(self, coords):
        self.innerBoundaryIs = LinearRing(coords)

    @property
    def outerboundaryis(self):
        return self.outerBoundaryIs

    @outerboundaryis.setter
    def outerboundaryis(self, coords):
        self.outerBoundaryIs = LinearRing(coords)

    def __str__(self):
        str = '<Polygon id="{0}">'.format(self._id)
        str += super(Polygon, self).__str__()
        str += "</Polygon>"
        return str