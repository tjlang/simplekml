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
from abstractview import *
from styleselector import *
from coordinates import *
from region import *
from overlay import *
from timeprimitive import *


class Feature(Kmlable): # TODO:ExtendedData
    """Base class extended by all features."""
    id = 0
    def __init__(self,
                 name=None,
                 visibility=1,
                 open=0,
                 atomauthor=None,
                 atomlink=None,
                 address=None,
                 xaladdressdetails=None,
                 phonenumber=None,
                 snippet=None,
                 description=None,
                 camera=None,
                 lookat=None,
                 timestamp=None,
                 timespan=None,
                 region=None):
        Feature.id += 1
        self.name = name
        self.visibility = visibility
        self.open = open
        self._atomauthor = atomauthor
        self._atomlink = atomlink
        self.address = address
        self._xaladdressdetails = xaladdressdetails
        self.phoneNumber = phonenumber
        self.description = description
        self.Camera = None
        self.camera = camera
        self.LookAt = None
        self.lookat = lookat
        self.styleUrl = None
        self.snippet_ = snippet
        self.TimeStamp = timestamp
        self.TimeSpan = timespan
        self.Region = region
        self._id = "feat_{0}".format(Feature.id)
        self._style = None
        self._stylemap = None
        Feature.id += 1
        self._features = []
        self._schemas = []
        self._schemasmaps = []
        self._folders = []

    @property
    def xaladdressdetails(self):
        return self._xaladdressdetails

    @xaladdressdetails.setter
    def xaladdressdetails(self, xaladdressdetails):
        self._xaladdressdetails = xaladdressdetails

    @property
    def style(self):
        if self._style is None:
            self._style = Style()
            self.setStyle(self._style)
            self.addschema(self._style)
        return self._style

    @style.setter
    def style(self, style):
        self.setStyle(style)
        self.addschema(style)
        self._style = style

    @property
    def stylemap(self):
        if self._stylemap is None:
            self._stylemap = StyleMap()
            self.setStyle(self._stylemap)
            self.addschemamap(self._stylemap)
        return self._style

    @stylemap.setter
    def stylemap(self, stylemap):
        self.setStyle(stylemap)
        self.addschemamap(stylemap)
        self._stylemap = stylemap

    def addschemamap(self, schema):
        """Attaches the given schema (style) to this feature."""
        self._schemasmaps.append(schema)

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

    @property
    def balloonstyle(self):
        return self.style.balloonstyle

    @balloonstyle.setter
    def balloonstyle(self, balloonstyle):
        self.style.balloonstyle = balloonstyle

    @property
    def liststyle(self):
        return self.style.liststyle

    @liststyle.setter
    def liststyle(self, liststyle):
        self.style.liststyle = liststyle

    def setStyle(self, style):
        self.styleUrl = "#{0}".format(style.getId())

    @property
    def styleurl(self):
        return self.styleUrl

    @styleurl.setter
    def styleurl(self, styleurl):
        self.styleUrl = styleurl

    @property
    def phonenumber(self):
        return self.phoneNumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self.phoneNumber = phonenumber
        
    @property
    def atomauthor(self):
        return self._atomauthor

    @atomauthor.setter
    def atomauthor(self, atomauthor):
        self._atomauthor = atomauthor
        
    @property
    def atomlink(self):
        return self._atomlink

    @atomlink.setter
    def atomlink(self, atomlink):
        self._atomlink = atomlink

    @property
    def camera(self):
        if self.Camera is None:
            self.Camera = Camera()
            self.LookAt = None
        return self.Camera

    @camera.setter
    def camera(self, camera):
        self.LookAt = None
        self.Camera = camera

    @property
    def lookat(self):
        if self.LookAt is None:
            self.LookAt = LookAt()
            self.Camera = None
        return self.LookAt

    @lookat.setter
    def lookat(self, lookat):
        self.Camera = None
        self.LookAt = lookat

    @property
    def snippet(self):
        if self.snippet_ is None:
            self.snippet_ = Snippet()
        return self.snippet_

    @snippet.setter
    def snippet(self, snippet):
        self.snippet_ = snippet

    @property
    def timestamp(self):
        if self.TimeStamp is None:
            self.TimeStamp = TimeStamp()
        return self.TimeStamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self.TimeStamp = timestamp

    @property
    def timespan(self):
        if self.TimeSpan is None:
            self.TimeSpan = TimeSpan()
        return self.TimeSpan

    @timespan.setter
    def timespan(self, timespan):
        self.TimeSpan = timespan

    @property
    def region(self):
        if self.Region is None:
            self.Region = Region()
        return self.Region

    @region.setter
    def region(self, region):
        self.Region = region

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
        for schemamap in self._schemasmaps:
            self.addschema(schemamap.normalstyle)
            self.addschema(schemamap.highlightstyle)
        str = '<{0} id="{1}">'.format(self.__class__.__name__, self._id)
        for schema in self._schemas:
            str += schema.__str__()
        for schemamap in self._schemasmaps:
            str += schemamap.__str__()
        str += super(Feature, self).__str__()
        if self._atomauthor is not None:
            str += '<atom:author>{0}</atom:author>'.format(self._atomauthor)
        if self._atomlink is not None:
            str += '<atom:link href="{0}"/>'.format(self._atomlink)
        if self._xaladdressdetails is not None:
            str += '<xal:AddressDetails>{0}</xal:AddressDetails>'.format(self._xaladdressdetails)
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

    def newmultigeometry(self, **kwargs):
        """Creates a new MultiGeometry container and attaches it to the feature."""
        multi = MultiGeometry(**kwargs)
        multi._parent = self
        self.addfeature(multi)
        return multi

    def newgroundoverlay(self, **kwargs):
        """Creates a new GroundOverlay and attaches it to the feature."""
        groundover = GroundOverlay(**kwargs)
        groundover._parent = self
        self.addfeature(groundover)
        return groundover

    def newscreenoverlay(self, **kwargs):
        """Creates a new ScreenOverlay and attaches it to the feature."""
        screenover = ScreenOverlay(**kwargs)
        screenover._parent = self
        self.addfeature(screenover)
        return screenover

    def newphotooverlay(self, **kwargs):
        """Creates a new PhotoOverlay and attaches it to the feature."""
        photoover = PhotoOverlay(**kwargs)
        photoover._parent = self
        self.addfeature(photoover)
        return photoover


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

class Document(Container):  # --Document--
    """A container for features and styles.

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

    Public Methods:
    newpoint()          -- Creates a new [Point] and attaches it to the feature
    newlinestring()     -- Creates a new [LineString] and attaches it to the feature
    newpolygon()        -- Creates a new [Polygon] and attaches it to the feature
    newmultigeometry()  -- Creates a new [MultiGeometry] and attaches it to the feature
    newgroundoverlay()  -- Creates a new [GroundOverlay] and attaches it to the feature
    newscreenoverlay()  -- Creates a new [ScreenOverlay] and attaches it to the feature
    newphotooverlay()   -- Creates a new [PhotoOverlay] and attaches it to the feature

    """

    def __init__(self, **kwargs):
        super(Document, self).__init__(**kwargs)


class Folder(Container):  # --Document--
    """A container for features.

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

    Public Methods:
    newpoint()          -- Creates a new [Point] and attaches it to the feature
    newlinestring()     -- Creates a new [LineString] and attaches it to the feature
    newpolygon()        -- Creates a new [Polygon] and attaches it to the feature
    newmultigeometry()  -- Creates a new [MultiGeometry] and attaches it to the feature
    newgroundoverlay()  -- Creates a new [GroundOverlay] and attaches it to the feature
    newscreenoverlay()  -- Creates a new [ScreenOverlay] and attaches it to the feature
    newphotooverlay()   -- Creates a new [PhotoOverlay] and attaches it to the feature

    """

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


class Geometry(Kmlable):
    """Base class for all Geometries."""
    id = 0
    def __init__(self, **kwargs): # same arguments as feature
        self._id = "geom_{0}".format(Geometry.id)
        Geometry.id += 1
        self._placemark = Placemark(**kwargs)
        self._placemark.geometry = self
        self._parent = None
        self._style = None
        self._stylemap = None

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
    def atomauthor(self):
        return self._placemark.atomauthor

    @atomauthor.setter
    def atomauthor(self, atomauthor):
        self._placemark.atomauthor = atomauthor

    @property
    def atomlink(self):
        return self._placemark.atomlink

    @atomlink.setter
    def atomlink(self, atomlink):
        self._placemark.atomlink = atomlink

    @property
    def address(self):
        return self._placemark.address

    @address.setter
    def address(self, address):
        self._placemark.address = address

    @property
    def xaladdressdetails(self):
        return self._placemark.xaladdressdetails

    @xaladdressdetails.setter
    def xaladdressdetails(self, xaladdressdetails):
        self._placemark.xaladdressdetails = xaladdressdetails

    @property
    def phonenumber(self):
        return self._placemark.phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self._placemark.phonenumber = phonenumber

    @property
    def description(self):
        return self._placemark.description

    @description.setter
    def description(self, description):
        self._placemark.description = description

    @property
    def camera(self):
        if self._placemark.Camera is None:
            self._placemark.Camera = Camera()
            self._placemark.LookAt = None
        return self._placemark.Camera

    @camera.setter
    def camera(self, camera):
        self._placemark.LookAt = None
        self._placemark.Camera = camera

    @property
    def lookat(self):
        if self._placemark.LookAt is None:
            self._placemark.LookAt = LookAt()
            self._placemark.Camera = None
        return self._placemark.LookAt

    @lookat.setter
    def lookat(self, lookat):
        self._placemark.Camera = None
        self._placemark.LookAt = lookat

    @property
    def snippet(self):
        return self._placemark.snippet

    @snippet.setter
    def snippet(self, snippet):
        self._placemark.snippet = snippet

    @property
    def timespan(self):
        return self._placemark.timespan

    @timespan.setter
    def timespan(self, timespan):
        self._placemark.timespan = timespan

    @property
    def timestamp(self):
        return self._placemark.timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._placemark.timestamp = timestamp

    @property
    def region(self):
        return self._placemark.region

    @region.setter
    def region(self, region):
        self._placemark.region = region

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
    def stylemap(self):
        if self._stylemap is None:
            self._stylemap = StyleMap()
            self._placemark.setStyle(self._stylemap)
            if self._parent is not None:
                self._parent.addschemamap(self._stylemap)
        return self._stylemap

    @stylemap.setter
    def stylemap(self, stylemap):
        self._placemark.setStyle(stylemap)
        if self._parent is not None:
            self._parent.addschemamap(stylemap)
        self._stylemap = stylemap

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

    @property
    def balloonstyle(self):
        return self.style.balloonstyle

    @balloonstyle.setter
    def balloonstyle(self, balloonstyle):
        self.style.balloonstyle = balloonstyle

    @property
    def liststyle(self):
        return self.style.liststyle

    @liststyle.setter
    def liststyle(self, liststyle):
        self.style.liststyle = liststyle
    
    @property
    def placemark(self):
        return self._placemark


class PointGeometry(Geometry):
    """Base class for any geometry requiring coordinates (not Polygon)."""
    def __init__(self,
                 coords=(), **kwargs):
        super(PointGeometry, self).__init__(**kwargs)
        self.coordinates = Coordinates()
        self.coordinates.addcoordinates(list(coords))

    @property
    def coords(self):
        return self.coordinates

    @coords.setter
    def coords(self, coords):
        self.coordinates = Coordinates()
        self.coordinates.addcoordinates(coords)


class LinearRing(PointGeometry):  # --Document--
    """A closed line string, typically the outer boundary of a Polygon.

    Arguments:
    coords              -- list of tuples (default [(0.0,0.0,0.0)]
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
    extrude             -- int (default 0)
    tessellate          -- int (default 0)
    altitudemode        -- string from [AltitudeMode] contants (default None)
    gxaltitudemode      -- string from [gxAltitudeMode] contants [Region] (default None)
    gxaltitudeoffset    -- float (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    stylemap            -- [StyleMap] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    iconstyle           -- [IconStyle] (default None)
    labelstyle          -- [LabelStyle] (default None)
    linestyle           -- [LineStyle] (default None)
    polystyle           -- [PolyStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    """

    def __init__(self, coords=(),
                 extrude=0,
                 tessellate=0,
                 altitudemode=None,
                 gxaltitudemode=None,
                 gxaltitudeoffset=None,
                 **kwargs):
        super(LinearRing, self).__init__(list(coords), **kwargs)
        self.extrude = extrude
        self.tessellate = tessellate
        self.altitudeMode = altitudemode
        self.gxaltitudeMode = gxaltitudemode
        self.gxaltitudeOffset = gxaltitudeoffset

    def __str__(self):
        str = '<LinearRing>'
        str += super(LinearRing, self).__str__()
        str += "</LinearRing>"
        return str

    @property
    def altitudemode(self):
        return self.altitudeMode

    @altitudemode.setter
    def altitudemode(self, mode):
        self.altitudeMode = mode

    @property
    def gxaltitudemode(self):
        return self.gxaltitudeMode

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self.gxaltitudeMode = mode

    @property
    def gxaltitudeoffset(self):
        return self.gxaltitudeOffset

    @gxaltitudeoffset.setter
    def gxaltitudeoffset(self, offset):
        self.gxaltitudeOffset = offset


class Point(PointGeometry):  # --Document--
    """A geographic location defined by lon, lat, and altitude.

    Arguments:
    coords              -- list of tuples (default [(0.0,0.0,0.0)]
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
    extrude             -- int (default 0)
    altitudemode        -- string from [AltitudeMode] contants (default None)
    gxaltitudemode      -- string from [gxAltitudeMode] contants [Region] (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    stylemap            -- [StyleMap] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    iconstyle           -- [IconStyle] (default None)
    labelstyle          -- [LabelStyle] (default None)
    linestyle           -- [LineStyle] (default None)
    polystyle           -- [PolyStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    """

    def __init__(self,
                 extrude=0,
                 altitudemode=None,
                 gxaltitudemode=None,
                 **kwargs):
        super(Point, self).__init__(**kwargs)
        self.extrude = extrude
        self.altitudeMode = altitudemode
        self.gxaltitudeMode = gxaltitudemode

    @property
    def altitudemode(self):
        return self.altitudeMode

    @altitudemode.setter
    def altitudemode(self, mode):
        self.altitudeMode = mode

    @property
    def gxaltitudemode(self):
        return self.gxaltitudeMode

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self.gxaltitudeMode = mode

    def __str__(self):
        str = '<Point id="{0}">'.format(self._id)
        str += super(Point, self).__str__()
        str += "</Point>"
        return str


class LineString(PointGeometry):  # --Document--
    """A connected set of line segments.

    Arguments:
    coords              -- list of tuples (default [(0.0,0.0,0.0)]
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
    extrude             -- int (default 0)
    tessellate          -- int (default 0)
    altitudemode        -- string from [AltitudeMode] contants (default None)
    gxaltitudemode      -- string from [gxAltitudeMode] contants [Region] (default None)
    gxaltitudeoffset    -- float (default None)
    gxdraworder         -- int (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    stylemap            -- [StyleMap] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    iconstyle           -- [IconStyle] (default None)
    labelstyle          -- [LabelStyle] (default None)
    linestyle           -- [LineStyle] (default None)
    polystyle           -- [PolyStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    """
    def __init__(self,
                 extrude=0,
                 tessellate=0,
                 altitudemode=None,
                 gxaltitudemode=None,
                 gxaltitudeoffset=None,
                 gxdraworder=None,
                 **kwargs):
        super(LineString, self).__init__(**kwargs)
        self.extrude = extrude
        self.tessellate = tessellate
        self.altitudeMode = altitudemode
        self.gxaltitudeMode = gxaltitudemode
        self.gxaltitudeOffset = gxaltitudeoffset
        self.gxdrawOrder = gxdraworder

    @property
    def altitudemode(self):
        return self.altitudeMode

    @altitudemode.setter
    def altitudemode(self, mode):
        self.altitudeMode = mode

    @property
    def gxaltitudemode(self):
        return self.gxaltitudeMode

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self.gxaltitudeMode = mode

    @property
    def gxaltitudeoffset(self):
        return self.gxaltitudeOffset

    @gxaltitudeoffset.setter
    def gxaltitudeoffset(self, offset):
        self.gxaltitudeOffset = offset

    @property
    def gxdraworder(self):
        return self.gxdrawOrder

    @gxdraworder.setter
    def gxdraworder(self, gxdraworder):
        self.gxdrawOrder = gxdraworder

    def __str__(self):
        str = '<LineString id="{0}">'.format(self._id)
        str += super(LineString, self).__str__()
        str += "</LineString>"
        return str


class Polygon(Geometry):  # --Document--
    """A Polygon is defined by an outer boundary and/or an inner boundary.

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
    extrude             -- int (default 0)
    tessellate          -- int (default 0)
    altitudemode        -- string from [AltitudeMode] contants (default None)
    gxaltitudemode      -- string from [gxAltitudeMode] contants [Region] (default None)
    gxdraworder         -- int (default None)
    outerboundaryis     -- list of tuples (default [(0.0,0.0,0.0)]
    innerboundaryis     -- list of lists of tuples (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    stylemap            -- [StyleMap] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    iconstyle           -- [IconStyle] (default None)
    labelstyle          -- [LabelStyle] (default None)
    linestyle           -- [LineStyle] (default None)
    polystyle           -- [PolyStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    """
    def __init__(self,
                 extrude=0,
                 tessellate=0,
                 altitudemode=None,
                 gxaltitudemode=None,
                 outerboundaryis=(),
                 innerboundaryis=(), **kwargs):
        super(Polygon, self).__init__(**kwargs)
        self.extrude = extrude
        self.tessellate = tessellate
        self.altitudeMode = altitudemode
        self.gxaltitudeMode = gxaltitudemode
        self.outerBoundaryIs = LinearRing(list(outerboundaryis))
        self.innerboundaryis = list(innerboundaryis)

    @property
    def altitudemode(self):
        return self.altitudeMode

    @altitudemode.setter
    def altitudemode(self, mode):
        self.altitudeMode = mode

    @property
    def gxaltitudemode(self):
        return self.gxaltitudeMode

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self.gxaltitudeMode = mode

    @property
    def innerboundaryis(self):
        return self._innerboundaryis

    @innerboundaryis.setter
    def innerboundaryis(self, rings):
        self._innerboundaryis = []
        if not len(rings):
            self.innerBoundaryIs = None
        else:
            if type(rings[0]) == type(()):
                rings = [rings]
            self.innerBoundaryIs = ''
            for ring in rings:
                self.innerBoundaryIs += LinearRing(ring).__str__()
                self._innerboundaryis.append(LinearRing(ring))

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


class MultiGeometry(Geometry):  # --Document--
    """A Polygon is defined by an outer boundary and/or an inner boundary.

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
    stylemap            -- [StyleMap] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    iconstyle           -- [IconStyle] (default None)
    labelstyle          -- [LabelStyle] (default None)
    linestyle           -- [LineStyle] (default None)
    polystyle           -- [PolyStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    Public Methods:
    newpoint()          -- Creates a new [Point] and attaches it to the feature
    newlinestring()     -- Creates a new [LineString] and attaches it to the feature
    newpolygon()        -- Creates a new [Polygon] and attaches it to the feature
    newgroundoverlay()  -- Creates a new [GroundOverlay] and attaches it to the feature
    newscreenoverlay()  -- Creates a new [ScreenOverlay] and attaches it to the feature
    newphotooverlay()   -- Creates a new [PhotoOverlay] and attaches it to the feature


    """

    def __init__(self,
                 geometries=(), **kwargs):
        super(MultiGeometry, self).__init__(**kwargs)
        self._geometries = list(geometries)

    def newpoint(self, **kwargs):
        """Creates a new Point and attaches it to the MultiGeometry."""
        pnt = Point(**kwargs)
        pnt._parent = self._placemark
        self.addfeature(pnt)
        return pnt

    def newlinestring(self, **kwargs):
        """Creates a new Linestring and attaches it to the MultiGeometry."""
        ls = LineString(**kwargs)
        ls._parent = self._placemark
        self.addfeature(ls)
        return ls

    def newpolygon(self, **kwargs):
        """Creates a new Polygon and attaches it to the MultiGeometry."""
        poly = Polygon(**kwargs)
        poly._parent = self._placemark
        self.addfeature(poly)
        return poly

    def newgroundoverlay(self, **kwargs):
        """Creates a new GroundOverlay and attaches it to the feature."""
        groundover = GroundOverlay(**kwargs)
        groundover._parent = self._placemark
        self.addfeature(groundover)
        return groundover

    def newscreenoverlay(self, **kwargs):
        """Creates a new ScreenOverlay and attaches it to the feature."""
        screenover = ScreenOverlay(**kwargs)
        screenover._parent = self._placemark
        self.addfeature(screenover)
        return screenover

    def newphotooverlay(self, **kwargs):
        """Creates a new PhotoOverlay and attaches it to the feature."""
        photoover = PhotoOverlay(**kwargs)
        photoover._parent = self._placemark
        self.addfeature(photoover)
        return photoover
    
    def addfeature(self, feat):
        """Attaches a feature to this MultiGeometry."""
        self._geometries.append(feat)

    def __str__(self):
        str = '<MultiGeometry id="{0}">'.format(self._id)
        str += super(MultiGeometry, self).__str__()
        for geom in self._geometries:
            str += geom.__str__()
        str += "</MultiGeometry>"
        return str


class Overlay(Feature):
    """Base type for image overlays."""
    def __init__(self, color=None,
                       draworder=None,
                       icon=None,
                       **kwargs):
        super(Overlay, self).__init__(**kwargs)
        self.color = color
        self.drawOrder = draworder
        self.Icon = icon

    @property
    def draworder(self):
        return self.drawOrder

    @draworder.setter
    def draworder(self, draworder):
        self.drawOrder = draworder

    @property
    def icon(self):
        if self.Icon is None:
            self.Icon = Icon()
        return self.Icon

    @icon.setter
    def icon(self, icon):
        self.Icon = icon


class GroundOverlay(Overlay):  # --Document--
    """Draws an image overlay draped onto the terrain.

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
    color               -- string of [Color] constants (default None)
    draworder           -- int (default None)
    icon                -- [Icon] (default None)
    altitude            -- float (default None)
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants (default None)
    latlonbox           -- [LatLonBox] (default None)
    gxlatlonquad        -- [GxLatLonQuad] (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    """

    def __init__(self, altitude=None,
                       altitudemode=None,
                       gxaltitudemode=None,
                       latlonbox=None,
                       gxlatlonquad=None,
                       **kwargs):
        super(GroundOverlay, self).__init__(**kwargs)
        self.altitude = altitude
        self.altitudeMode = altitudemode
        self.gxaltitudeMode = gxaltitudemode
        self.LatLonBox = latlonbox
        self.gxLatLonQuad = gxlatlonquad

    @property
    def altitudemode(self):
        return self.altitudeMode

    @altitudemode.setter
    def altitudemode(self, altitudemode):
        self.altitudeMode = altitudemode

    @property
    def gxaltitudemode(self):
        return self.gxaltitudeMode

    @gxaltitudemode.setter
    def gxaltitudemode(self, gxaltitudemode):
        self.gxaltitudeMode = gxaltitudemode

    @property
    def latlonbox(self):
        if self.LatLonBox is None:
            self.LatLonBox = LatLonBox()
            self.gxLatLonBox = None
        return self.LatLonBox

    @latlonbox.setter
    def latlonbox(self, latlonbox):
        self.LatLonBox = latlonbox

    @property
    def gxlatlonquad(self):
        if self.gxLatLonQuad is None:
            self.gxLatLonQuad = GxLatLonQuad()
        return self.gxLatLonQuad

    @gxlatlonquad.setter
    def gxlatlonquad(self, gxlatlonquad):
        self.GxLatLonQuad = gxlatlonquad


class ScreenOverlay(Overlay):   # --Document--
    """Draws an image overlay fixed to the screen.

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
    color               -- string of [Color] constants (default None)
    draworder           -- int (default None)
    icon                -- [Icon] (default None)
    overlayxy           -- [OverlayXY] (default None)
    screenxy            -- [ScreenXY] (default None)
    rotationxy          -- [RoatationXY] (default None)
    size                -- [Size] (default None)
    rotation            -- float (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    """

    def __init__(self, overlayxy=None,
                       screenxy=None,
                       rotationxy=None,
                       size=None,
                       rotation=None,
                       **kwargs):
        super(ScreenOverlay, self).__init__(**kwargs)
        self.rotation = rotation
        self.overlayxy_ = overlayxy
        self.screenxy_ = screenxy
        self.rotationxy_ = rotationxy
        self.size_ = size

    @property
    def overlayxy(self):
        if self.overlayxy_ is None:
            self.overlayxy_ = OverlayXY()
        return self.overlayxy_

    @overlayxy.setter
    def overlayxy(self, overlayxy):
        self.overlayxy_ = overlayxy

    @property
    def screenxy(self):
        if self.screenxy_ is None:
            self.screenxy_ = ScreenXY()
        return self.screenxy_

    @screenxy.setter
    def screenxy(self, screenxy):
        self.screenxy_ = screenxy

    @property
    def rotationxy(self):
        if self.rotationxy_ is None:
            self.rotationxy_ = RotationXY()
        return self.rotationxy_

    @rotationxy.setter
    def rotationxy(self, rotationxy):
        self.rotationxy_ = rotationxy

    @property
    def size(self):
        if self.size_ is None:
            self.size_ = Size()
        return self.size_

    @size.setter
    def size(self, size):
        self.size_ = size


class PhotoOverlay(Overlay):  # --Document--
    """Geographically locate a photograph in Google Earth.

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
    color               -- string of [Color] constants (default None)
    draworder           -- int (default None)
    icon                -- [Icon] (default None)
    rotation            -- float (default 0)
    viewvolume          -- [ViewVolume] (default None)
    imagepyramid        -- [ImagePyramid] (default None)
    point               -- [Point] (default None)
    shape               -- string from [Shape] contants (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    placemark           -- [Placemark (default [Placemark], read-only)

    """

    def __init__(self, rotation=0,
                       viewvolume=None,
                       imagepyramid=None,
                       point=None,
                       shape=None,
                       **kwargs):
        super(PhotoOverlay, self).__init__(**kwargs)
        self.rotation = rotation
        self.ViewVolume = viewvolume
        self.ImagePyramid = imagepyramid
        self.point_ = point
        self.shape = shape

    @property
    def viewvolume(self):
        if self.ViewVolume is None:
            self.ViewVolume = ViewVolume()
        return self.ViewVolume

    @viewvolume.setter
    def viewvolume(self, viewvolume):
        self.ViewVolume = viewvolume

    @property
    def imagepyramid(self):
        if self.ImagePyramid is None:
            self.ImagePyramid = ImagePyramid()
        return self.ImagePyramid

    @imagepyramid.setter
    def imagepyramid(self, imagepyramid):
        self.ImagePyramid = imagepyramid

    @property
    def point(self):
        if self.point_ is None:
            self.point_ = Point()
        return self.point_

    @point.setter
    def point(self, point):
        self.point_ = point
    