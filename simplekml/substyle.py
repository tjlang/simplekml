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
from icon import Icon, ItemIcon

class ColorStyle(Kmlable):
    """A base class for geometry styles."""
    def __init__(self, color=None, colormode=ColorMode.normal):
        self.color = color
        self.colorMode = colormode

    @property
    def colormode(self):
        return self.ColorMode

    @colormode.setter
    def colormode(self, colormode):
        self.ColorMode = colormode


class LineStyle(ColorStyle):
    """Specifies the drawing style for all line geometry."""
    def __init__(self, width=1, **kwargs):
        super(LineStyle, self).__init__(**kwargs)
        self.width = width


class PolyStyle(ColorStyle):
    """Specifies the drawing style for all polygons."""
    def __init__(self, fill=1, outline=1, **kwargs):
        super(PolyStyle, self).__init__(**kwargs)
        self.fill = fill
        self.outline = outline


class IconStyle(ColorStyle):
    """Specifies how icons for point Placemarks are drawn."""
    def __init__(self, scale=1, heading=0, icon=Icon(), **kwargs):
        super(IconStyle, self).__init__(**kwargs)
        self.scale = scale
        self.heading = heading
        self.Icon = icon

    @property
    def icon(self):
        return self.Icon

    @icon.setter
    def icon(self, icon):
        self.Icon = icon

#    def seticonhref(self, href):
#        """Convenience method for setting an Icon's href."""
#        self.Icon.href = href


class LabelStyle(ColorStyle):
    """Specifies how the name of a Feature is drawn."""
    def __init__(self, scale=1, **kwargs):
        super(LabelStyle, self).__init__(**kwargs)
        self.scale = scale

        
class BalloonStyle(Kmlable):
   """Specifies the content and layout of the description balloon."""
   def __init__(self, 
                bgcolor=None,
                textcolor=None,
                text=None,
                displaymode=DisplayMode.default):
       self.bgColor = bgcolor
       self.textColor = textcolor
       self.text = text
       self.displayMode = displaymode

   @property
   def bgcolor(self):
       return self.bgColor

   @bgcolor.setter
   def bgcolor(self, bgcolor):
       self.bgColor = bgcolor

   @property
   def textcolor(self):
       return self.textColor

   @textcolor.setter
   def textcolor(self, textcolor):
       self.textColor = textcolor

   @property
   def displaymode(self):
       return self.displayMode

   @displaymode.setter
   def displaymode(self, displaymode):
       self.displayMode = displaymode


class ListStyle(Kmlable):
   """Specifies the display of the elements style in the navigation bar."""
   def __init__(self,
                listitemtype=ListItemType.check,
                bgcolor=None,
                itemicon=None):
       self.listItemType = listitemtype
       self.bgColor = bgcolor
       self.ItemIcon = itemicon

   @property
   def itemicon(self):
       if self.ItemIcon is None:
            self.ItemIcon = ItemIcon()
       return self.itemicon

   @itemicon.setter
   def itemicon(self, itemicon):
       self.ItemIcon = itemicon

   @property
   def listitemtype(self):
       return self.listItemType

   @listitemtype.setter
   def listitemtype(self, listitemtype):
       self.listItemType = listitemtype

   @property
   def bgcolor(self):
       return self.bgColor

   @bgcolor.setter
   def bgcolor(self, bgcolor):
       self.bgColor = bgcolor