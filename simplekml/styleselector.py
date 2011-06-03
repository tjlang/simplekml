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
from simplekml.substyle import *

class StyleSelector(Kmlable):
    """Base style class, extended by Style."""
    _id = 0
    def __init__(self):
        super(StyleSelector, self).__init__()
        self._id = "stylesel_{0}".format(StyleSelector._id)
        StyleSelector._id += 1

    @property
    def id(self):
        return self._id


class Style(StyleSelector): # --Document--
    """Styles affect how Geometry is presented.

    Arguments:
    iconstyle           -- [IconStyle] (default None)
    labelstyle          -- [LabelStyle] (default None)
    linestyle           -- [LineStyle] (default None)
    polystyle           -- [PolyStyle] (default None)
    balloonstyle        -- [BalloonStyle] (default None)
    liststyle           -- [ListStyle] (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self,
                 iconstyle=None,
                 labelstyle=None,
                 linestyle=None,
                 polystyle=None,
                 balloonstyle=None,
                 liststyle=None):
        super(Style, self).__init__()
        self._kml["IconStyle"] = iconstyle
        self._kml["LabelStyle"] = labelstyle
        self._kml["LineStyle"] = linestyle
        self._kml["PolyStyle"] = polystyle
        self._kml["BalloonStyle"] = balloonstyle
        self._kml["ListStyle"] = liststyle

    def __str__(self):
        str = '<Style id="{0}">'.format(self._id)
        str += super(Style, self).__str__()
        str += "</Style>"
        return str
      
    @property
    def iconstyle(self):
        if self._kml["IconStyle"] is None:
            self._kml["IconStyle"] = IconStyle()
        return self._kml["IconStyle"]
        
    @iconstyle.setter
    def iconstyle(self, iconstyle):
        self._kml["IconStyle"] = iconstyle
        
    @property
    def labelstyle(self):
        if self._kml["LabelStyle"] is None:
            self._kml["LabelStyle"] = LabelStyle()
        return self._kml["LabelStyle"]

    @labelstyle.setter
    def labelstyle(self, labelstyle):
        self._kml["LabelStyle"] = labelstyle
        
    @property
    def linestyle(self):
        if self._kml["LineStyle"] is None:
            self._kml["LineStyle"] = LineStyle()
        return self._kml["LineStyle"]
        
    @linestyle.setter
    def linestyle(self, linestyle):
        self._kml["LineStyle"] = linestyle

    @property
    def polystyle(self):
        if self._kml["PolyStyle"] is None:
            self._kml["PolyStyle"] = PolyStyle()
        return self._kml["PolyStyle"]
        
    @polystyle.setter
    def polystyle(self, polystyle):
        self._kml["PolyStyle"] = polystyle
        
    @property
    def balloonstyle(self):
        if self._kml["BalloonStyle"] is None:
            self._kml["BalloonStyle"] = BalloonStyle()
        return self._kml["BalloonStyle"]

    @balloonstyle.setter
    def balloonstyle(self, balloonstyle):
        self._kml["BalloonStyle"] = balloonstyle

    @property
    def liststyle(self):
        if self._kml["ListStyle"] is None:
            self._kml["ListStyle"] = ListStyle()
        return self._kml["ListStyle"]

    @liststyle.setter
    def liststyle(self, liststyle):
        self._kml["ListStyle"] = liststyle


class StyleMap(StyleSelector): # --Document--
    """Styles affect how Geometry is presented.

    Arguments:
    normalstyle         -- [Style] (default None)
    highlightstyle      -- [Style] (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self,
                 normalstyle=None,
                 highlightstyle=None):
        super(StyleMap, self).__init__()
        self._pairnormal = None
        self._pairhighlight = None
        self.normalstyle = normalstyle
        self.highlightstyle = highlightstyle

    def __str__(self):
        str = '<StyleMap id="{0}">'.format(self._id)
        str += super(StyleMap, self).__str__()
        if self._pairnormal is not None:
            str += "<Pair>"
            str += "<key>normal</key>"
            str += "<styleUrl>#{0}</styleUrl>".format(self._pairnormal._id)
            str += "</Pair>"
        if self._pairhighlight is not None:
            str += "<Pair>"
            str += "<key>highlight</key>"
            str += "<styleUrl>#{0}</styleUrl>".format(self._pairhighlight._id)
            str += "</Pair>"
        str += "</StyleMap>"
        return str

    @property
    def normalstyle(self):
        if self._pairnormal is None:
            self._pairnormal = Style()
        return self._pairnormal

    @normalstyle.setter
    def normalstyle(self, normal):
        self._pairnormal = normal

    @property
    def highlightstyle(self):
        if self._pairhighlight is None:
            self._pairhighlight = Style()
        return self._pairhighlight

    @highlightstyle.setter
    def highlightstyle(self, highlighturl):
        self._pairhighlight = highlighturl