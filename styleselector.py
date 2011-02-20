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
from substyle import *

class StyleSelector(Kmlable):
    """Base style class, extended by Style."""
    id = 0
    def __init__(self):
        self._id = "stylesel_{0}".format(StyleSelector.id)
        StyleSelector.id += 1

    def getId(self):
        return self._id


class Style(StyleSelector):
    """Styles affect how Geometry is presented."""
    def __init__(self,
                 iconstyle=None,
                 labelstyle=None,
                 linestyle=None,
                 polystyle=None,
                 balloonstyle=None,
                 liststyle=None):
        super(Style, self).__init__()
        self.IconStyle = iconstyle
        self.LabelStyle = labelstyle
        self.LineStyle = linestyle
        self.PolyStyle = polystyle
        self.BalloonStyle = balloonstyle    #not implemented
        self.ListStyle = liststyle   #not implemented

    def __str__(self):
        str = '<Style id="{0}">'.format(self._id)
        str += super(Style, self).__str__()
        str += "</Style>"
        return str
      
    @property
    def iconstyle(self):
        if self.IconStyle is None:
            self.IconStyle = IconStyle()
        return self.IconStyle
        
    @iconstyle.setter
    def iconstyle(self, iconstyle):
        self.IconStyle = iconstyle
        
    @property
    def labelstyle(self):
        if self.LabelStyle is None:
            self.LabelStyle = LabelStyle()
        return self.LabelStyle

        
    @labelstyle.setter
    def labelstyle(self, labelstyle):
        self.LabelStyle = labelstyle
        
    @property
    def linestyle(self):
        if self.LineStyle is None:
            self.LineStyle = LineStyle()
        return self.LineStyle
        
    @linestyle.setter
    def linestyle(self, linestyle):
        self.LineStyle = linestyle

    @property
    def polystyle(self):
        if self.PolyStyle is None:
            self.PolyStyle = PolyStyle()
        return self.PolyStyle
        
    @polystyle.setter
    def polystyle(self, polystyle):
        self.PolyStyle = polystyle
        
#    @property
#    def balloonstyle(self):
#        if self.IconStyle is None:
#             self.BalloonStyle = BalloonStyle()
#         return self.BalloonStyle
#        
#    @balloonstyle.setter
#    def balloonstyle(self, balloonstyle):
#        self.BalloonStyle = balloonstyle
#        
#    @property
#    def liststyle(self):
#        if self.IconStyle is None:
#             self.ListStyle = ListStyle()
#         return self.ListStyle
#        
#    @liststyle.setter
#    def liststyle(self, liststyle):
#        self.ListStyle = liststyle
        
