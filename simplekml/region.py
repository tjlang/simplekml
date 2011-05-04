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

class Box(Kmlable):
    def __init__(self,
                 north=None,
                 south=None,
                 east=None,
                 west=None):
        self.north = north
        self.south = south
        self.east = east
        self.west = west


class LatLonBox(Kmlable): # --Document--
    """Specifies where the top, bottom, right, and left sides of a bounding box for the ground overlay are aligned.

    Arguments:
    north               -- float (default None)
    south               -- float (default None)
    east                -- float (default None)
    west                -- float (default None)
    rotation            -- float (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, rotation=None, **kwargs):
        super(LatLonBox, self).__init__(**kwargs)
        self.rotation = rotation


class LatLonAltBox(Box): # --Document--
    """A bounding box that describes an area of interest defined by geographic coordinates and altitudes.

    Arguments:
    north               -- float (default None)
    south               -- float (default None)
    east                -- float (default None)
    west                -- float (default None)
    minaltitude         -- float (default None)
    maxaltitude         -- float (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self,
                 minaltitude=0,
                 maxaltitude=0,
                 altitudemode=AltitudeMode.clamptoground,
                 **kwargs):
        super(LatLonAltBox, self).__init__(**kwargs)
        self.minAltitude = minaltitude
        self.maxAltitude = maxaltitude
        self.altitudeMode = altitudemode

    @property
    def minaltitude(self):
        return self.minAltitude

    @minaltitude.setter
    def minaltitude(self, minAltitude):
        self.minAltitude = minAltitude

    @property
    def maxaltitude(self):
        return self.maxAltitude

    @maxaltitude.setter
    def maxaltitude(self, maxaltitude):
        self.maxAltitude = maxaltitude

    @property
    def altitudemode(self):
        return self.altitudeMode

    @altitudemode.setter
    def altitudemode(self, altitudemode):
        self.altitudeMode = altitudemode


class Lod(Kmlable): # --Document--
    """Level of Detail describes the size of the projected region on the screen that is required in order for the
    region to be considered "active".

    Arguments:
    minlodpixels        -- int (default 0)
    maxlodpixels        -- int (default -1)
    minfadeextent       -- int (default 0)
    maxfadeextent       -- int (default 0)

    Properties:
    Same as arguments.

    """
    def __init__(self,
                 minlodpixels=0,
                 maxlodpixels=-1,
                 minfadeextent=0,
                 maxfadeextent=0):
        self.minLodPixels = minlodpixels
        self.maxLodPixels = maxlodpixels
        self.minFadeExtent = minfadeextent
        self.maxFadeExtent = maxfadeextent

    @property
    def minlodpixels(self):
        return self.minLodPixels

    @minlodpixels.setter
    def minlodpixels(self, minlodpixels):
        self.minLodPixels = minlodpixels

    @property
    def maxlodpixels(self):
        return self.maxLodPixels

    @maxlodpixels.setter
    def maxlodpixels(self, maxlodpixels):
        self.maxLodPixels = maxlodpixels

    @property
    def minfadeextent(self):
        return self.minFadeExtent

    @minfadeextent.setter
    def minfadeextent(self, minfadeextent):
        self.minFadeExtent = minfadeextent

    @property
    def maxfadeextent(self):
        return self.maxFadeExtent

    @maxfadeextent.setter
    def maxfadeextent(self, maxfadeextent):
        self.maxFadeExtent = maxfadeextent


class GxLatLonQuad(Kmlable): # --Document--
    """Used for nonrectangular quadrilateral ground overlays.

    Arguments:
    coords              -- list of 4 tuples (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, coords=None):
        self._coords = None
        self.coordinates = coords

    @property
    def coords(self):
        return self.coordinates

    @coords.setter
    def coords(self, coords):
        self.coordinates = ''
        for coord in coords:
            self.coordinates += "{0},{1} ".format(coord[0], coord[1])
        self.coordinates = self.coordinates[:-1]


class Region(Kmlable): # --Document--
    """Used for nonrectangular quadrilateral ground overlays.

    Arguments:
    latlonaltbox            -- [LatLonAltBox] (default None)
    lod                     -- [Lod] (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, latlonaltbox=LatLonAltBox(), lod=Lod()):
        self.LatLonAltBox = latlonaltbox
        self.Lod = lod

    @property
    def latlonaltbox(self):
        return self.LatLonAltBox

    @latlonaltbox.setter
    def latlonaltbox(self, latlonaltbox):
        self.LatLonAltBox = latlonaltbox

    @property
    def lod(self):
        return self.Lod

    @lod.setter
    def lod(self, lod):
        self.Lod = lod