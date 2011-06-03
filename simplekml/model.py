from simplekml.base import Kmlable


class Location(Kmlable):  # --Document--
    """Specifies the exact coordinates of the Model's origin in latitude, longitude, and altitude.

    Arguments:
    longitude           -- int (default None)
    latitude            -- int (default None)
    altitude            -- int (default 0)

    Properties:
    Same as arguments.

    """

    def __init__(self,
                 longitude=None,
                 latitude=None,
                 altitude=0):
        super(Location, self).__init__()
        self._kml['longitude'] = longitude
        self._kml['latitude'] = latitude
        self._kml['altitude'] = altitude

    @property
    def longitude(self):
        return self._kml['longitude']

    @longitude.setter
    def longitude(self, longitude):
        self._kml['longitude'] = longitude

    @property
    def latitude(self):
        return self._kml['latitude']

    @latitude.setter
    def latitude(self, latitude):
        self._kml['latitude'] = latitude

    @property
    def altitude(self):
        return self._kml['altitude']

    @altitude.setter
    def altitude(self, altitude):
        self._kml['altitude'] = altitude


class Orientation(Kmlable):  # --Document--
    """Describes rotation of a 3D model's coordinate system to position the object in Google Earth.

    Arguments:
    heading             -- int (default 0)
    tilt                -- int (default 0)
    roll                -- int (default 0)

    Properties:
    Same as arguments.

    """
    def __init__(self,
                 heading=0,
                 tilt=0,
                 roll=0):
        super(Orientation, self).__init__()
        self._kml['heading'] = heading
        self._kml['tilt'] = tilt
        self._kml['roll'] = roll

    @property
    def heading(self):
        return self._kml['heading']

    @heading.setter
    def heading(self, heading):
        self._kml['heading'] = heading

    @property
    def tilt(self):
        return self._kml['tilt']

    @tilt.setter
    def tilt(self, tilt):
        self._kml['tilt'] = tilt

    @property
    def roll(self):
        return self._kml['roll']

    @roll.setter
    def roll(self, roll):
        self._kml['roll'] = roll


class Scale(Kmlable): # --Document--
    """Scales a model along the x, y, and z axes in the model's coordinate space.

    Arguments:
    x                   -- int (default 1)
    y                   -- int (default 1)
    z                   -- int (default 1)

    Properties:
    Same as arguments.

    """

    def __init__(self,
                 x=1,
                 y=1,
                 z=1):
        super(Scale, self).__init__()
        self._kml['x'] = x
        self._kml['y'] = y
        self._kml['z'] = z

    @property
    def x(self):
        return self._kml['x']

    @x.setter
    def x(self, x):
        self._kml['x'] = x

    @property
    def y(self):
        return self._kml['y']

    @y.setter
    def y(self, y):
        self._kml['y'] = y

    @property
    def z(self):
        return self._kml['z']

    @z.setter
    def z(self, z):
        self._kml['z'] = z


class Alias(Kmlable): # --Document--
    """Contains a mapping from a sourcehref to a targethref.

    Arguments:
    targethref          -- string (default None)
    sourcehref          -- string (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self,
                 targethref=None,
                 sourcehref=None):
        super(Alias, self).__init__()
        self._kml['targetHref'] = targethref
        self._kml['sourceHref'] = sourcehref

    @property
    def targethref(self):
        return self._kml['targetHref']

    @targethref.setter
    def targethref(self, targethref):
        self._kml['targetHref'] = targethref

    @property
    def sourcehref(self):
        return self._kml['sourceHref']

    @sourcehref.setter
    def sourcehref(self, sourcehref):
        self._kml['sourceHref'] = sourcehref


class ResourceMap(Kmlable): # --Document--
    """Contains and specifies 0 or more [Alias] elements.

    Arguments:
    aliases             -- list of aliases (default None)

    Properties:
    Same as arguments.

    Public Methods:
    newalias()          -- Creates a new [Alias] and attaches it to the resourcemap

    """

    def __init__(self,
                 aliases=None):
        super(ResourceMap, self).__init__()
        self._aliases = aliases
        if self._aliases is None:
            self._aliases = []

    @property
    def aliases(self):
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        self._aliases = aliases

    def newalias(self, **kwargs):
        alias = Alias(**kwargs)
        self._aliases.append(alias)
        return alias

    def __str__(self):
        str = ''
        for alias in self._aliases:
            str += alias.__str__() 
        return str