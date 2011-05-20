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
        super(Box, self).__init__()
        self._kml["north"] = north
        self._kml["south"] = south
        self._kml["east"] = east
        self._kml["west"] = west
        
    @property
    def north(self):
        return self._kml['north']
    
    @north.setter
    def north(self, north):
        self._kml['north'] = north
        
    @property
    def south(self):
        return self._kml['south']
    
    @south.setter
    def south(self, south):
        self._kml['south'] = south
        
    @property
    def east(self):
        return self._kml['east']
    
    @east.setter
    def east(self, east):
        self._kml['east'] = east
        
    @property
    def west(self):
        return self._kml['west']
    
    @west.setter
    def west(self, west):
        self._kml['west'] = west


class LatLonBox(Box): # --Document--
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
        self._kml['rotation'] = rotation
        
    @property
    def rotation(self):
        return self._kml['rotation']
    
    @rotation.setter
    def rotation(self, rotation):
        self._kml['rotation'] = rotation


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
        self._kml["minAltitude"] = minaltitude
        self._kml["maxAltitude"] = maxaltitude
        self._kml["altitudeMode"] = altitudemode

    @property
    def minaltitude(self):
        return self._kml["minAltitude"]

    @minaltitude.setter
    def minaltitude(self, minAltitude):
        self._kml["minAltitude"] = minAltitude

    @property
    def maxaltitude(self):
        return self._kml["maxAltitude"]

    @maxaltitude.setter
    def maxaltitude(self, maxaltitude):
        self._kml["maxAltitude"] = maxaltitude

    @property
    def altitudemode(self):
        return self._kml["altitudeMode"]

    @altitudemode.setter
    def altitudemode(self, altitudemode):
        self._kml["altitudeMode"] = altitudemode


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
        super(Lod, self).__init__()
        self._kml["minLodPixels"] = minlodpixels
        self._kml["maxLodPixels"] = maxlodpixels
        self._kml["minFadeExtent"] = minfadeextent
        self._kml["maxFadeExtent"] = maxfadeextent

    @property
    def minlodpixels(self):
        return self._kml["minLodPixels"]

    @minlodpixels.setter
    def minlodpixels(self, minlodpixels):
        self._kml["minLodPixels"] = minlodpixels

    @property
    def maxlodpixels(self):
        return self._kml["maxLodPixels"]

    @maxlodpixels.setter
    def maxlodpixels(self, maxlodpixels):
        self._kml["maxLodPixels"] = maxlodpixels

    @property
    def minfadeextent(self):
        return self._kml["minFadeExtent"]

    @minfadeextent.setter
    def minfadeextent(self, minfadeextent):
        self._kml["minFadeExtent"] = minfadeextent

    @property
    def maxfadeextent(self):
        return self._kml["maxFadeExtent"]

    @maxfadeextent.setter
    def maxfadeextent(self, maxfadeextent):
        self._kml["maxFadeExtent"] = maxfadeextent


class GxLatLonQuad(Kmlable): # --Document--
    """Used for nonrectangular quadrilateral ground overlays.

    Arguments:
    coords              -- list of 4 tuples (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, coords=None):
        super(GxLatLonQuad, self).__init__()
        self._coords = None
        self._kml["coordinates"] = coords

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coords):
        self._kml["coordinates"] = ''
        self._coords = coords
        for coord in coords:
            self._kml["coordinates"] += "{0},{1} ".format(coord[0], coord[1])
        self._kml["coordinates"] = self._kml["coordinates"][:-1]


class Region(Kmlable): # --Document--
    """Used for nonrectangular quadrilateral ground overlays.

    Arguments:
    latlonaltbox            -- [LatLonAltBox] (default None)
    lod                     -- [Lod] (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, latlonaltbox=LatLonAltBox(), lod=Lod()):
        super(Region, self).__init__()
        self._kml["LatLonAltBox"] = latlonaltbox
        self._kml["Lod"] = lod

    @property
    def latlonaltbox(self):
        return self._kml["LatLonAltBox"]

    @latlonaltbox.setter
    def latlonaltbox(self, latlonaltbox):
        self._kml["LatLonAltBox"] = latlonaltbox

    @property
    def lod(self):
        return self._kml["Lod"]

    @lod.setter
    def lod(self, lod):
        self._kml["Lod"] = lod