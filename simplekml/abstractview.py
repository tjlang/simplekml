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
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.heading = heading
        self.tilt = tilt
        self.AltitudeMode = altitudemode
        self.gxAltitudeMode = gxaltitudemode
        self.gxTimeSpan = gxtimespan
        self.gxTimeStamp = gxtimestamp

    @property
    def gxtimestamp(self):
        if self.gxtimestamp is None:
            self.gxtimestamp = GxTimeStamp()
        return self.gxtimestamp

    @gxtimestamp.setter
    def gxtimestamp(self, gxtimestamp):
        self.gxtimestamp = gxtimestamp

    @property
    def gxtimespan(self):
        if self.gxtimespan is None:
            self.gxtimespan = GxTimeSpan()
        return self.gxtimespan

    @gxtimespan.setter
    def gxtimespan(self, gxtimespan):
        self.gxtimespan = gxtimespan

    @property
    def altitudemode(self):
        return self.AltitudeMode

    @altitudemode.setter
    def altitudemode(self, altmode):
        self.AltitudeMode = altmode

    @property
    def gxaltitudemode(self):
        return self.gxAltitudeMode

    @gxaltitudemode.setter
    def gxaltitudemode(self, gxaltmode):
        self.gxAltitudeMode = gxaltmode


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
        self.roll = roll


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
        self.range = range


