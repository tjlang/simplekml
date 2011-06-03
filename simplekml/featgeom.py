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

from simplekml.base import Kmlable
from simplekml.constants import *
from simplekml.abstractview import *
from simplekml.styleselector import *
from simplekml.coordinates import *
from simplekml.region import *
from simplekml.overlay import *
from simplekml.timeprimitive import *
from simplekml.icon import *
from simplekml.model import *


class Feature(Kmlable): # TODO:ExtendedData
    """Base class extended by all features."""
    _id = 0
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
        Feature._id += 1
        super(Feature, self).__init__()
        self._kml['name'] = name
        self._kml['visibility'] = visibility
        self._kml['open'] = open
        self._kml['atom:author'] = atomauthor
        self._kml['atom:link'] = atomlink
        self._kml['address'] = address
        self._kml['xal:AddressDetails'] = xaladdressdetails
        self._kml['phoneNumber'] = phonenumber
        self._kml['description'] = description
        self._kml['Camera'] = camera
        self._kml['LookAt'] = lookat
        self._kml['snippet_'] = snippet
        self._kml['TimeStamp'] = timestamp
        self._kml['TimeSpan'] = timespan
        self._kml['Region'] = region
#        self._kml['Style'] = None
#        self._kml['StyleMap'] = None
        self._kml['styleUrl'] = None
        self._id = "feat_{0}".format(Feature._id)
        self._style = None
        self._stylemap = None
        self._features = []
        self._schemas = []
        self._schemasmaps = []
        self._folders = []

    @property
    def name(self):
        return self._kml['name']

    @name.setter
    def name(self, name):
        self._kml['name'] = name

    @property
    def visibility(self):
        return self._kml['visibility']

    @visibility.setter
    def visibility(self, visibility):
        self._kml['visibility'] = visibility

    @property
    def open(self):
        return self._kml['open']

    @open.setter
    def open(self, open):
        self._kml['open'] = open

    @property
    def atomauthor(self):
        return self._kml['atom:author']

    @atomauthor.setter
    def atomauthor(self, atomauthor):
        self._kml['atom:author'] = atomauthor

    @property
    def atomlink(self):
        return self._kml['atom:link']

    @atomlink.setter
    def atomlink(self, atomlink):
        self._kml['atom:link'] = atomlink

    @property
    def address(self):
        return self._kml['address']

    @address.setter
    def address(self, address):
        self._kml['address'] = address

    @property
    def xaladdressdetails(self):
        return self._kml['xal:AddressDetails']

    @xaladdressdetails.setter
    def xaladdressdetails(self, xaladdressdetails):
        self._kml['xal:AddressDetails'] = xaladdressdetails

    @property
    def phonenumber(self):
        return self._kml['phoneNumber']

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        self._kml['phoneNumber'] = phonenumber

    @property
    def description(self):
        return self._kml['description']

    @description.setter
    def description(self, description):
        self._kml['description'] = description

    @property
    def camera(self):
        if self._kml['Camera'] is None:
            self._kml['Camera'] = Camera()
            self._kml['LookAt'] = None
        return self._kml['Camera']

    @camera.setter
    def camera(self, camera):
        self._kml['Camera'] = camera
        self._kml['LookAt'] = None

    @property
    def lookat(self):
        if self._kml['LookAt'] is None:
            self._kml['LookAt'] = LookAt()
            self._kml['Camera'] = None
        return self._kml['LookAt']

    @lookat.setter
    def lookat(self, lookat):
        self._kml['Camera'] = None
        self._kml['LookAt'] = lookat

    @property
    def snippet(self):
        if self._kml['snippet_'] is None:
            self._kml['snippet_'] = Snippet()
        return self._kml['snippet_']

    @snippet.setter
    def snippet(self, snippet):
        self._kml['snippet_'] = snippet

    @property
    def timestamp(self):
        if self._kml['TimeStamp'] is None:
            self._kml['TimeStamp'] = TimeStamp()
        return self._kml['TimeStamp']

    @timestamp.setter
    def timestamp(self, timestamp):
        self._kml['TimeStamp'] = timestamp

    @property
    def timespan(self):
        if self._kml['TimeSpan'] is None:
            self._kml['TimeSpan'] = TimeSpan()
        return self._kml['TimeSpan']

    @timespan.setter
    def timespan(self, timespan):
        self._kml['TimeSpan'] = timespan

    @property
    def region(self):
        if self._kml['Region'] is None:
            self._kml['Region'] = Region()
        return self._kml['Region']

    @region.setter
    def region(self, region):
        self._kml['Region'] = region

    @property
    def id(self):
        return self._id

    @property
    def style(self):
        if self._style is None:
            self._style = Style()
            self._setStyle(self._style)
            self._addschema(self._style)
        return self._style

    @style.setter
    def style(self, style):
        self._setStyle(style)
        self._addschema(style)
        self._style = style

    @property
    def stylemap(self):
        if self._stylemap is None:
            self._stylemap = StyleMap()
            self._setStyle(self._stylemap)
            self._addschemamap(self._stylemap)
        return self._stylemap

    @stylemap.setter
    def stylemap(self, stylemap):
        self._setStyle(stylemap)
        self._addschemamap(stylemap)
        self._stylemap = stylemap

    @property
    def styleurl(self):
        return self._kml['styleUrl']

    @styleurl.setter
    def styleurl(self, styleurl):
        self._kml['styleUrl'] = styleurl

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

    def _addfeature(self, feature):
        """Attaches the given feature to this feature."""
        if isinstance(feature, Geometry):
            self._features.append(feature._placemark)
            feature._parent = self
            if feature._style is not None:
                self._addschema(feature._style)
        else:
            self._features.append(feature)

    def _addschema(self, schema):
        """Attaches the given schema (style) to this feature."""
        self._schemas.append(schema)

    def _addschemamap(self, schema):
        """Attaches the given schema (style) to this feature."""
        self._schemasmaps.append(schema)

    def _setStyle(self, style):
        self._kml['styleUrl'] = "#{0}".format(style.id)

    def __str__(self):
        for schemamap in self._schemasmaps:
            self._addschema(schemamap.normalstyle)
            self._addschema(schemamap.highlightstyle)
        str = '<{0} id="{1}">'.format(self.__class__.__name__, self._id)
        for schema in self._schemas:
            str += schema.__str__()
        for schemamap in self._schemasmaps:
            str += schemamap.__str__()
        str += super(Feature, self).__str__()
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
        self._addfeature(pnt)
        return pnt

    def newlinestring(self, **kwargs):
        """Creates a new Linestring and attaches it to the feature."""
        ls = LineString(**kwargs)
        ls._parent = self
        self._addfeature(ls)
        return ls

    def newpolygon(self, **kwargs):
        """Creates a new Polygon and attaches it to the feature."""
        poly = Polygon(**kwargs)
        poly._parent = self
        self._addfeature(poly)
        return poly

    def newmultigeometry(self, **kwargs):
        """Creates a new MultiGeometry container and attaches it to the feature."""
        multi = MultiGeometry(**kwargs)
        multi._parent = self
        self._addfeature(multi)
        return multi

    def newgroundoverlay(self, **kwargs):
        """Creates a new GroundOverlay and attaches it to the feature."""
        groundover = GroundOverlay(**kwargs)
        groundover._parent = self
        self._addfeature(groundover)
        return groundover

    def newscreenoverlay(self, **kwargs):
        """Creates a new ScreenOverlay and attaches it to the feature."""
        screenover = ScreenOverlay(**kwargs)
        screenover._parent = self
        self._addfeature(screenover)
        return screenover

    def newphotooverlay(self, **kwargs):
        """Creates a new PhotoOverlay and attaches it to the feature."""
        photoover = PhotoOverlay(**kwargs)
        photoover._parent = self
        self._addfeature(photoover)
        return photoover


class Container(Feature):
    """Base class, extended by Document and Folder."""
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

    def newfolder(self, **kwargs):
        """Creates a new Folder and attaches it to the container."""
        fol = Folder(**kwargs)
        fol._parent = self
        self._addfeature(fol)
        return fol

    def newdocument(self, **kwargs):
        """Creates a new Document and attaches it to the container."""
        doc = Document(**kwargs)
        doc._parent = self
        self._addfeature(doc)
        return doc

    def newnetworklink(self, **kwargs):
        """Creates a new NetworkLink and attaches it to the container."""
        netlink = NetworkLink(**kwargs)
        netlink._parent = self
        self._addfeature(netlink)
        return netlink

    def newmodel(self, **kwargs):
        """Creates a new NetworkLink and attaches it to the container."""
        model = Model(**kwargs)
        model._parent = self
        self._addfeature(model)
        return model

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
    newpoint()          -- Creates a new [Point] and attaches it to the document
    newlinestring()     -- Creates a new [LineString] and attaches it to the document
    newpolygon()        -- Creates a new [Polygon] and attaches it to the document
    newmultigeometry()  -- Creates a new [MultiGeometry] and attaches it to the document
    newgroundoverlay()  -- Creates a new [GroundOverlay] and attaches it to the document
    newscreenoverlay()  -- Creates a new [ScreenOverlay] and attaches it to the document
    newphotooverlay()   -- Creates a new [PhotoOverlay] and attaches it to the document
    newnetworklink()    -- Creates a new [NetworkLink] and attaches it to the document

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
    newpoint()          -- Creates a new [Point] and attaches it to the folder
    newlinestring()     -- Creates a new [LineString] and attaches it to the folder
    newpolygon()        -- Creates a new [Polygon] and attaches it to the folder
    newmultigeometry()  -- Creates a new [MultiGeometry] and attaches it to the folder
    newgroundoverlay()  -- Creates a new [GroundOverlay] and attaches it to the folder
    newscreenoverlay()  -- Creates a new [ScreenOverlay] and attaches it to the folder
    newphotooverlay()   -- Creates a new [PhotoOverlay] and attaches it to the folder
    newnetworklink()    -- Creates a new [NetworkLink] and attaches it to the folder

    """

    def __init__(self, **kwargs):
        super(Folder, self).__init__(**kwargs)


class Placemark(Feature):
    """A Placemark is a Feature with associated Geometry."""
    def __init__(self, geometry=None, **kwargs):
        super(Placemark, self).__init__(**kwargs)
        self._kml['Geometry_'] = geometry

    @property
    def geometry(self):
        return self._kml['Geometry_']

    @geometry.setter
    def geometry(self, geom):
        self._kml['Geometry_'] = geom


class Geometry(Kmlable):
    """Base class for all Geometries."""
    _id = 0
    def __init__(self, **kwargs): # same arguments as feature
        super(Geometry, self).__init__()
        self._id = "geom_{0}".format(Geometry._id)
        Geometry._id += 1
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
        if self._placemark.camera is None:
            self._placemark.camera = Camera()
        return self._placemark.camera

    @camera.setter
    def camera(self, camera):
        self._placemark.camera = camera

    @property
    def lookat(self):
        if self._placemark.lookat is None:
            self._placemark.lookat = LookAt()
        return self._placemark.lookat

    @lookat.setter
    def lookat(self, lookat):
        self._placemark.lookat = lookat

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
            self._placemark._setStyle(self._style)
            if self._parent is not None:
                self._parent._addschema(self._style)
        return self._style

    @style.setter
    def style(self, style):
        self._placemark._setStyle(style)
        if self._parent is not None:
            self._parent._addschema(style)
        self._style = style

    @property
    def stylemap(self):
        if self._stylemap is None:
            self._stylemap = StyleMap()
            self._placemark._setStyle(self._stylemap)
            if self._parent is not None:
                self._parent._addschemamap(self._stylemap)
        return self._stylemap

    @stylemap.setter
    def stylemap(self, stylemap):
        self._placemark._setStyle(stylemap)
        if self._parent is not None:
            self._parent._addschemamap(stylemap)
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
        self._kml['coordinates'] = Coordinates()
        self._kml['coordinates'].addcoordinates(list(coords))

    @property
    def coords(self):
        return self._kml['coordinates']

    @coords.setter
    def coords(self, coords):
        self._kml['coordinates'] = Coordinates()
        self._kml['coordinates'].addcoordinates(coords)


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
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants [Region] (default None)
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
    placemark           -- [Placemark] (default [Placemark], read-only)

    """

    def __init__(self, coords=(),
                 extrude=0,
                 tessellate=0,
                 altitudemode=None,
                 gxaltitudemode=None,
                 gxaltitudeoffset=None,
                 **kwargs):
        super(LinearRing, self).__init__(list(coords), **kwargs)
        self._kml['extrude'] = extrude
        self._kml['tessellate'] = tessellate
        self._kml['altitudeMode'] = altitudemode
        self._kml['gx:altitudeMode'] = gxaltitudemode
        self._kml['gx:altitudeOffset'] = gxaltitudeoffset

    def __str__(self):
        str = '<LinearRing>'
        str += super(LinearRing, self).__str__()
        str += "</LinearRing>"
        return str

    @property
    def extrude(self):
        return self._kml['extrude']

    @extrude.setter
    def extrude(self, extrude):
        self._kml['extrude'] = extrude

    @property
    def tessellate(self):
        return self._kml['tessellate']

    @tessellate.setter
    def tessellate(self, tessellate):
        self._kml['tessellate'] = tessellate

    @property
    def altitudemode(self):
        return self._kml['altitudeMode']

    @altitudemode.setter
    def altitudemode(self, mode):
        self._kml['altitudeMode'] = mode

    @property
    def gxaltitudemode(self):
        return self._kml['gx:altitudeMode']

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self._kml['gx:altitudeMode'] = mode

    @property
    def gxaltitudeoffset(self):
        return self._kml['gx:altitudeOffset']

    @gxaltitudeoffset.setter
    def gxaltitudeoffset(self, offset):
        self._kml['gx:altitudeOffset'] = offset


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
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants [Region] (default None)

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
    placemark           -- [Placemark] (default [Placemark], read-only)

    """

    def __init__(self,
                 extrude=0,
                 altitudemode=None,
                 gxaltitudemode=None,
                 **kwargs):
        super(Point, self).__init__(**kwargs)
        self._kml['extrude'] = extrude
        self._kml['altitudeMode'] = altitudemode
        self._kml['gx:altitudeMode'] = gxaltitudemode

    @property
    def extrude(self):
        return self._kml['extrude']

    @extrude.setter
    def extrude(self, extrude):
        self._kml['extrude'] = extrude

    @property
    def altitudemode(self):
        return self._kml['altitudeMode']

    @altitudemode.setter
    def altitudemode(self, mode):
        self._kml['altitudeMode'] = mode

    @property
    def gxaltitudemode(self):
        return self._kml['gx:altitudeMode']

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self._kml['gx:altitudeMode'] = mode

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
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants [Region] (default None)
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
    placemark           -- [Placemark] (default [Placemark], read-only)

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
        self._kml['extrude'] = extrude
        self._kml['tessellate'] = tessellate
        self._kml['altitudeMode'] = altitudemode
        self._kml['gx:altitudeMode'] = gxaltitudemode
        self._kml['gx:altitudeOffset'] = gxaltitudeoffset
        self._kml['gx:drawOrder'] = gxdraworder

    @property
    def extrude(self):
        return self._kml['extrude']

    @extrude.setter
    def extrude(self, extrude):
        self._kml['extrude'] = extrude

    @property
    def tessellate(self):
        return self._kml['tessellate']

    @tessellate.setter
    def tessellate(self, tessellate):
        self._kml['tessellate'] = tessellate

    @property
    def altitudemode(self):
        return self._kml['altitudeMode']

    @altitudemode.setter
    def altitudemode(self, mode):
        self._kml['altitudeMode'] = mode

    @property
    def gxaltitudemode(self):
        return self._kml['gx:altitudeMode']

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self._kml['gx:altitudeMode'] = mode

    @property
    def gxaltitudeoffset(self):
        return self._kml['gx:altitudeOffset']

    @gxaltitudeoffset.setter
    def gxaltitudeoffset(self, offset):
        self._kml['gx:altitudeOffset'] = offset

    @property
    def gxdraworder(self):
        return self._kml['gx:drawOrder']

    @gxdraworder.setter
    def gxdraworder(self, gxdraworder):
        self._kml['gx:drawOrder'] = gxdraworder

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
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants [Region] (default None)
    gxdraworder         -- int (default None)
    outerboundaryis     -- list of tuples (default (0.0,0.0,0.0))
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
    placemark           -- [Placemark] (default [Placemark], read-only)

    """
    def __init__(self,
                 extrude=0,
                 tessellate=0,
                 altitudemode=None,
                 gxaltitudemode=None,
                 outerboundaryis=(),
                 innerboundaryis=(), **kwargs):
        super(Polygon, self).__init__(**kwargs)
        self._kml['extrude'] = extrude
        self._kml['tessellate'] = tessellate
        self._kml['altitudeMode'] = altitudemode
        self._kml['gx:altitudeMode'] = gxaltitudemode
        self._kml['outerBoundaryIs'] = LinearRing(list(outerboundaryis))
        self._kml['innerBoundaryIs'] = None
        self.innerboundaryis = list(innerboundaryis)

    @property
    def extrude(self):
        return self._kml['extrude']

    @extrude.setter
    def extrude(self, extrude):
        self._kml['extrude'] = extrude

    @property
    def tessellate(self):
        return self._kml['tessellate']

    @tessellate.setter
    def tessellate(self, tessellate):
        self._kml['tessellate'] = tessellate

    @property
    def altitudemode(self):
        return self._kml['altitudeMode']

    @altitudemode.setter
    def altitudemode(self, mode):
        self._kml['altitudeMode'] = mode

    @property
    def gxaltitudemode(self):
        return self._kml['gx:altitudeMode']

    @gxaltitudemode.setter
    def gxaltitudemode(self, mode):
        self._kml['gx:altitudeMode'] = mode

    @property
    def innerboundaryis(self):
        return self._innerboundaryis

    @innerboundaryis.setter
    def innerboundaryis(self, rings):
        self._innerboundaryis = []
        if not len(rings):
            self._kml['innerBoundaryIs'] = None
        else:
            if type(rings[0]) == type(()):
                rings = [rings]
            self._kml['innerBoundaryIs'] = ''
            for ring in rings:
                self._kml['innerBoundaryIs'] += LinearRing(ring).__str__()
                self._innerboundaryis.append(LinearRing(ring))

    @property
    def outerboundaryis(self):
        return self._kml['outerBoundaryIs']

    @outerboundaryis.setter
    def outerboundaryis(self, coords):
        self._kml['outerBoundaryIs'] = LinearRing(coords)

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
    placemark           -- [Placemark] (default [Placemark], read-only)

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
        self._addfeature(pnt)
        return pnt

    def newlinestring(self, **kwargs):
        """Creates a new Linestring and attaches it to the MultiGeometry."""
        ls = LineString(**kwargs)
        ls._parent = self._placemark
        self._addfeature(ls)
        return ls

    def newpolygon(self, **kwargs):
        """Creates a new Polygon and attaches it to the MultiGeometry."""
        poly = Polygon(**kwargs)
        poly._parent = self._placemark
        self._addfeature(poly)
        return poly

    def newgroundoverlay(self, **kwargs):
        """Creates a new GroundOverlay and attaches it to the feature."""
        groundover = GroundOverlay(**kwargs)
        groundover._parent = self._placemark
        self._addfeature(groundover)
        return groundover

    def newscreenoverlay(self, **kwargs):
        """Creates a new ScreenOverlay and attaches it to the feature."""
        screenover = ScreenOverlay(**kwargs)
        screenover._parent = self._placemark
        self._addfeature(screenover)
        return screenover

    def newphotooverlay(self, **kwargs):
        """Creates a new PhotoOverlay and attaches it to the feature."""
        photoover = PhotoOverlay(**kwargs)
        photoover._parent = self._placemark
        self._addfeature(photoover)
        return photoover
    
    def _addfeature(self, feat):
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
        self._kml['color'] = color
        self._kml['drawOrder'] = draworder
        self._kml['Icon'] = icon

    @property
    def color(self):
        return self._kml['color']

    @color.setter
    def color(self, color):
        self._kml['color'] = color

    @property
    def draworder(self):
        return self._kml['drawOrder']

    @draworder.setter
    def draworder(self, draworder):
        self._kml['drawOrder'] = draworder

    @property
    def icon(self):
        if self._kml['Icon'] is None:
            self._kml['Icon'] = Icon()
        return self._kml['Icon']

    @icon.setter
    def icon(self, icon):
        self._kml['Icon'] = icon


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
    placemark           -- [Placemark] (default [Placemark], read-only)

    """

    def __init__(self, altitude=None,
                       altitudemode=None,
                       gxaltitudemode=None,
                       latlonbox=None,
                       gxlatlonquad=None,
                       **kwargs):
        super(GroundOverlay, self).__init__(**kwargs)
        self._kml['altitude'] = altitude
        self._kml['altitudeMode'] = altitudemode
        self._kml['gx:altitudeMode'] = gxaltitudemode
        self._kml['LatLonBox'] = latlonbox
        self._kml['gx:LatLonQuad'] = gxlatlonquad

    @property
    def altitude(self):
        return self._kml['altitude']

    @altitude.setter
    def altitude(self, altitude):
        self._kml['altitude'] = altitude

    @property
    def altitudemode(self):
        return self._kml['altitudeMode']

    @altitudemode.setter
    def altitudemode(self, altitudemode):
        self._kml['altitudeMode'] = altitudemode

    @property
    def gxaltitudemode(self):
        return self._kml['gx:altitudeMode']

    @gxaltitudemode.setter
    def gxaltitudemode(self, gxaltitudemode):
        self._kml['gx:altitudeMode'] = gxaltitudemode

    @property
    def latlonbox(self):
        if self._kml['LatLonBox'] is None:
            self._kml['LatLonBox'] = LatLonBox()
        return self._kml['LatLonBox']

    @latlonbox.setter
    def latlonbox(self, latlonbox):
        self._kml['LatLonBox'] = latlonbox

    @property
    def gxlatlonquad(self):
        if self._kml['gx:LatLonQuad'] is None:
            self._kml['gx:LatLonQuad'] = GxLatLonQuad()
        return self._kml['gx:LatLonQuad']

    @gxlatlonquad.setter
    def gxlatlonquad(self, gxlatlonquad):
        self._kml['gx:LatLonQuad'] = gxlatlonquad


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
    placemark           -- [Placemark] (default [Placemark], read-only)

    """

    def __init__(self, overlayxy=None,
                       screenxy=None,
                       rotationxy=None,
                       size=None,
                       rotation=None,
                       **kwargs):
        super(ScreenOverlay, self).__init__(**kwargs)
        self._kml['rotation'] =rotation
        self._kml['overlayXY_'] = overlayxy
        self._kml['screenXY_'] = screenxy
        self._kml['rotationXY_'] = rotationxy
        self._kml['size_'] = size

    @property
    def rotation(self):
        return self._kml['rotation']

    @rotation.setter
    def rotation(self, rotation):
        self._kml['rotation'] = rotation

    @property
    def overlayxy(self):
        if self._kml['overlayXY_'] is None:
            self._kml['overlayXY_'] = OverlayXY()
        return self._kml['overlayXY_']

    @overlayxy.setter
    def overlayxy(self, overlayxy):
        self._kml['overlayXY_'] = overlayxy

    @property
    def screenxy(self):
        if self._kml['screenXY_'] is None:
            self._kml['screenXY_'] = ScreenXY()
        return self._kml['screenXY_']

    @screenxy.setter
    def screenxy(self, screenxy):
        self._kml['screenXY_'] = screenxy

    @property
    def rotationxy(self):
        if self._kml['rotationXY_'] is None:
            self._kml['rotationXY_'] = RotationXY()
        return self._kml['rotationXY_']

    @rotationxy.setter
    def rotationxy(self, rotationxy):
        self._kml['rotationXY_'] = rotationxy

    @property
    def size(self):
        if self._kml['size_'] is None:
            self._kml['size_'] = Size()
        return self._kml['size_']

    @size.setter
    def size(self, size):
        self._kml['size_'] = size


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
    shape               -- string from [Shape] constants (default None)

    Properties:
    Same as arguments, with the following additional properties:
    style               -- [Style] (default None)
    iconstyle           -- [IconStyle] (default None)
    liststyle           -- [ListStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    placemark           -- [Placemark] (default [Placemark], read-only)

    """

    def __init__(self, rotation=0,
                       viewvolume=None,
                       imagepyramid=None,
                       point=None,
                       shape=None,
                       **kwargs):
        super(PhotoOverlay, self).__init__(**kwargs)
        self._kml['rotation'] = rotation
        self._kml['ViewVolume'] = viewvolume
        self._kml['ImagePyramid'] = imagepyramid
        self._kml['point_'] = point
        self._kml['shape'] = shape

    @property
    def rotation(self):
        return self._kml['rotation']

    @rotation.setter
    def rotation(self, rotation):
        self._kml['rotation'] = rotation

    @property
    def viewvolume(self):
        if self._kml['ViewVolume'] is None:
            self._kml['ViewVolume'] = ViewVolume()
        return self._kml['ViewVolume']

    @viewvolume.setter
    def viewvolume(self, viewvolume):
        self._kml['ViewVolume'] = viewvolume

    @property
    def imagepyramid(self):
        if self._kml['ImagePyramid'] is None:
            self._kml['ImagePyramid'] = ImagePyramid()
        return self._kml['ImagePyramid']

    @imagepyramid.setter
    def imagepyramid(self, imagepyramid):
        self._kml['ImagePyramid'] = imagepyramid

    @property
    def point(self):
        if self._kml['point_'] is None:
            self._kml['point_'] = Point()
        return self._kml['point_']

    @point.setter
    def point(self, point):
        self._kml['point_'] = point

    @property
    def shape(self):
        return self._kml['shape']

    @shape.setter
    def shape(self, shape):
        self._kml['shape'] = shape


class NetworkLink(Feature):  # --Document--
    """References a KML file or KMZ archive on a local or remote network.

    Arguments:
    refreshvisibility   -- int (default 0)
    flytoview           -- int (default 0)
    link                -- [Link] (default None)

    Properties:
    Same as arguments.

    """
    
    def __init__(self, refreshvisibility=0,
                       flytoview=0,
                       link=None,
                       **kwargs):
        super(NetworkLink, self).__init__(**kwargs)
        self._kml['refreshVisibility'] = refreshvisibility
        self._kml['flyToView'] = flytoview
        self._kml['Link'] = link

    @property
    def refreshvisibility(self):
        return self._kml['refreshVisibility']

    @refreshvisibility.setter
    def refreshvisibility(self, refreshvisibility):
        self._kml['refreshVisibility'] = refreshvisibility

    @property
    def flytoview(self):
        return self._kml['flyToView']

    @flytoview.setter
    def flytoview(self, flytoview):
        self._kml['flyToView'] = flytoview

    @property
    def link(self):
        if self._kml['Link'] is None:
            self._kml['Link'] = Link()
        return self._kml['Link']

    @link.setter
    def link(self, link):
        self._kml['Link'] = link


class Model(Kmlable):  # --Document--
    """A 3D object described in a COLLADA file.

    Arguments:
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants (default None)
    location            -- [Location] (default None)
    orientation         -- [Orientation] (default None)
    scale               -- [Scale] (default None)
    link                -- [Link] (default None)
    resourcemap         -- [ResourceMap] (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self,
                 altitudemode=None,
                 gxaltitudemode=None,
                 location=None,
                 orientation=None,
                 scale=None,
                 link=None,
                 resourcemap=None):
        super(Model, self).__init__()
        self._kml['altitudeMode'] = altitudemode
        self._kml['gx:altitudeMode'] = gxaltitudemode
        self._kml['Location'] = location
        self._kml['Orientation'] = orientation
        self._kml['Scale'] = scale
        self._kml['Link'] = link
        self._kml['ResourceMap'] = resourcemap

    @property
    def altitudemode(self):
        return self._kml['altitudeMode']

    @altitudemode.setter
    def altitudemode(self, altitudemode):
        self._kml['altitudeMode'] = altitudemode

    @property
    def gxaltitudemode(self):
        return self._kml['gx:altitudeMode']

    @gxaltitudemode.setter
    def gxaltitudemode(self, gxaltitudemode):
        self._kml['gx:altitudeMode'] = gxaltitudemode

    @property
    def location(self):
        if self._kml['Location'] is None:
            self._kml['Location'] = Location()
        return self._kml['Location']

    @location.setter
    def location(self, location):
        self._kml['Location'] = location

    @property
    def orientation(self):
        if self._kml['Orientation'] is None:
            self._kml['Orientation'] = Orientation()
        return self._kml['Orientation']

    @orientation.setter
    def orientation(self, orientation):
        self._kml['Orientation'] = orientation

    @property
    def scale(self):
        if self._kml['Scale'] is None:
            self._kml['Scale'] = Scale()
        return self._kml['Scale']

    @scale.setter
    def scale(self, scale):
        self._kml['Scale'] = scale

    @property
    def link(self):
        if self._kml['Link'] is None:
            self._kml['Link'] = Link()
        return self._kml['Link']

    @link.setter
    def link(self, link):
        self._kml['Link'] = link

    @property
    def resourcemap(self):
        if self._kml['ResourceMap'] is None:
            self._kml['ResourceMap'] = ResourceMap()
        return self._kml['ResourceMap']

    @resourcemap.setter
    def resourcemap(self, resourcemap):
        self._kml['ResourceMap'] = resourcemap