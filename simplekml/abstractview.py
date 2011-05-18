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
from timeprimitive import *

class AbstractView(Kmlable): #TODO: gxViewerOptions
    """Base class, extended by Camera and LookAt."""
    def __init__(self,
                 longitude=None,
                 latitude=None,
                 altitude=None,
                 heading=None,
                 tilt=None,
                 altitudemode=None,
                 gxaltitudemode=None,
                 gxtimespan=None,
                 gxtimestamp=None):
        super(AbstractView, self).__init__()
        self._kml["longitude"] = longitude
        self._kml["latitude"] = latitude
        self._kml["altitude"] = altitude
        self._kml["heading"] = heading
        self._kml["tilt"] = tilt
        self._kml["altitudeMode"] = altitudemode
        self._kml["gx] =AltitudeMode"] = gxaltitudemode
        self._kml["gx] =TimeSpan"] = gxtimespan
        self._kml["gx] =TimeStamp"] = gxtimestamp

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
    def altitudemode(self):
        return self._kml['altitudeMode']

    @altitudemode.setter
    def altitudemode(self, altitudemode):
        self._kml['altitudeMode'] = altitudemode

    @property
    def gxaltitudemode(self):
        return self._kml['gx:altitudeMode']

    @gxaltitudemode.setter
    def gxaltitudemode(self, gxaltmode):
        self._kml['gx:altitudeMode'] = gxaltmode

    @property
    def gxtimestamp(self):
        if self._kml['gx:TimeStamp'] is None:
            self._kml['gx:TimeStamp'] = GxTimeStamp()
        return self._kml['gx:TimeStamp']

    @gxtimestamp.setter
    def gxtimestamp(self, gxtimestamp):
        self._kml['gx:TimeStamp'] = gxtimestamp

    @property
    def gxtimespan(self):
        if self._kml['gx:TimeSpan'] is None:
            self._kml['gx:TimeSpan'] = GxTimeSpan()
        return self._kml['gx:TimeSpan']

    @gxtimespan.setter
    def gxtimespan(self, gxtimespan):
        self._kml['gx:TimeSpan'] = gxtimespan


class Camera(AbstractView): # --Document--
    """A virtual camera that views the scene.

    Arguments:
    longitude           -- float (default None)
    latitude            -- float (default None)
    altitude            -- float (default None)
    heading             -- float (default None)
    tilt                -- float (default None)
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants (default None)
    gxtimespan          -- [GxTimeSpan] (default None)
    gxtimestamp         -- [GxTimeStamp] (default None)
    roll                -- float (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, roll=None, **kwargs):
        super(Camera, self).__init__(**kwargs)
        self._kml['roll'] = roll

    @property
    def roll(self):
        return self._kml['roll']

    @roll.setter
    def roll(self, roll):
        self._kml['roll'] = roll


class LookAt(AbstractView): # --Document--
    """Positions the camera in relation to the object that is being viewed.

    Arguments:
    longitude           -- float (default None)
    latitude            -- float (default None)
    altitude            -- float (default None)
    heading             -- float (default None)
    tilt                -- float (default None)
    altitudemode        -- string from [AltitudeMode] constants (default None)
    gxaltitudemode      -- string from [GxAltitudeMode] constants (default None)
    gxtimespan          -- [GxTimeSpan] (default None)
    gxtimestamp         -- [GxTimeStamp] (default None)
    range               -- float (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, range=None, **kwargs):
        super(LookAt, self).__init__(**kwargs)
        self._kml['range'] = range

    @property
    def range(self):
        return self._kml['range']

    @range.setter
    def range(self, range):
        self._kml['range'] = range


