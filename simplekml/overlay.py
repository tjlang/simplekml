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

from base import *
from constants import *


class ViewVolume(Kmlable): # --Document--
    """Defines how much of the current scene is visible.

    Arguments:
    leftfov             -- float (default None)
    rightfov            -- float (default None)
    bottomfov           -- float (default None)
    topfov              -- float (default None)
    near                -- float (default None)


    Properties:
    Same as arguments.

    """

    def __init__(self,
                 leftfov=0,
                 rightfov=0,
                 bottomfov=0,
                 topfov=0,
                 near=0):
        super(ViewVolume, self).__init__()
        self._kml["leftFov"] = leftfov
        self._kml["rightFov"] = rightfov
        self._kml["bottomFov"] = bottomfov
        self._kml["topFov"] = topfov
        self._kml["near"] = near

    @property
    def leftfov(self):
        return self._kml['leftFov']
    
    @leftfov.setter
    def leftfov(self, leftfov):
        self._kml['leftFov'] = leftfov

    @property
    def rightfov(self):
        return self._kml['rightFov']
    
    @rightfov.setter
    def rightfov(self, rightfov):
        self._kml['rightFov'] = rightfov

    @property
    def topfov(self):
        return self._kml['topFov']
    
    @topfov.setter
    def topfov(self, topFov):
        self._kml['topFov'] = topFov

    @property
    def bottomfov(self):
        return self._kml['bottomFov']
    
    @bottomfov.setter
    def bottomfov(self, bottomFov):
        self._kml['bottomFov'] = bottomFov
        
    @property
    def near(self):
        return self._kml['near']
    
    @near.setter
    def near(self, near):
        self._kml['near'] = near


class ImagePyramid(Kmlable): # --Document--
    """A hierarchical set of images.

    Arguments:
    titlesize           -- int (default 256)
    maxwidth            -- int (default None)
    maxheight           -- int (default None)
    gridorigin          -- string from [GridOrigin] constants (default lowerLeft)

    Properties:
    Same as arguments.

    """
    
    def __init__(self,
                 titlesize=256,
                 maxwidth=0,
                 maxheight=0,
                 gridorigin=GridOrigin.lowerleft):
        super(ImagePyramid, self).__init__()
        self._kml["titleSize"] = titlesize
        self._kml["maxWidth"] = maxwidth
        self._kml["maxHeight"] = maxheight
        self._kml["gridOrigin"] = gridorigin

    @property
    def titlesize(self):
        return self._kml["titleSize"]

    @titlesize.setter
    def titlesize(self, titlesize):
        self._kml["titleSize"] = titlesize

    @property
    def maxwidth(self):
        return self._kml["maxWidth"]

    @maxwidth.setter
    def maxwidth(self, maxwidth):
        self._kml["maxWidth"] = maxwidth

    @property
    def maxheight(self):
        return self._kml["maxHeight"]

    @maxheight.setter
    def maxheight(self, maxheight):
        self._kml["maxHeight"] = maxheight

    @property
    def gridorigin(self):
        return self._kml["gridOrigin"]

    @gridorigin.setter
    def gridorigin(self, gridorigin):
        self._kml["gridOrigin"] = gridorigin

