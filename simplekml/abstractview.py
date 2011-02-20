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

class AbstractView(Kmlable):
    """Base class, extended by Camera and LookAt."""
    def __init__(self,
                 timeprimitive=None,
                 longitude=None,
                 latitude=None,
                 altitude=None,
                 heading=None,
                 tilt=None,
                 altitudemode=AltitudeMode.clamptoground):
        self.TimePrimitive = timeprimitive
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.heading = heading
        self.tilt = tilt
        self.AltitudeMode = altitudemode

    @property
    def timeprimitive(self):
        return self.TimePrimitive

    @timeprimitive.setter
    def timeprimitive(self, timeprim):
        self.TimePrimitive = timeprim

    @property
    def altitudemode(self):
        return self.AltitudeMode

    @altitudemode.setter
    def altitudemode(self, altmode):
        self.AltitudeMode = altmode

class Camera(AbstractView):
    """A virtual camera that views the scene."""
    def __init__(self, roll=None, **kwargs):
        super(Camera, self).__init__(**kwargs)
        self.roll = roll


class LookAt(AbstractView):
    """Positions the camera in relation to the object that is being viewed."""
    def __init__(self, range=None, **kwargs):
        super(LookAt, self).__init__(**kwargs)
        self.range = range


