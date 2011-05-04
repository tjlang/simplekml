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

class Link(Kmlable): # --Document--
    """Defines an image associated with an Icon style or overlay.

    Arguments:
    href                -- string (default None)
    refreshmode         -- string from [RefreshMode] constants (default None)
    refreshinterval     -- float (default None)
    viewrefreshmode     -- string from [ViewRefreshMode] constants (default None)
    viewrefreshtime     -- float (default None)
    viewboundscale      -- float (default None)
    viewformat          -- string (default None)
    httpquery           -- string (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self,
                 href=" ",
                 refreshmode=None,
                 refreshinterval=None,
                 viewrefreshmode=None,
                 viewrefreshtime=None,
                 viewboundscale=None,
                 viewformat=None,
                 httpquery=None):
        self.href = href
        self.refreshMode = refreshmode
        self.refreshInterval = refreshinterval
        self.viewRefreshMode = viewrefreshmode
        self.viewRefreshTime = viewrefreshtime
        self.viewBoundScale = viewboundscale
        self.viewFormat = viewformat
        self.httpQuery = httpquery

    @property
    def refreshmode(self):
        return self.refreshMode

    @refreshmode.setter
    def refreshmode(self, refreshmode):
        self.refreshMode = refreshmode

    @property
    def refreshinterval(self):
        return self.refreshInterval

    @refreshinterval.setter
    def refreshinterval(self, refreshinterval):
        self.refreshInterval = refreshinterval

    @property
    def viewrefreshmode(self):
        return self.viewRefreshMode

    @viewrefreshmode.setter
    def viewrefreshmode(self, viewrefreshmode):
        self.viewRefreshMode = viewrefreshmode

    @property
    def viewrefreshtime(self):
        return self.viewRefreshTime

    @viewrefreshtime.setter
    def viewrefreshtime(self, viewrefreshtime):
        self.viewRefreshTime = viewrefreshtime

    @property
    def viewboundscale(self):
        return self.viewBoundScale

    @viewboundscale.setter
    def viewboundscale(self, viewboundscale):
        self.viewBoundScale = viewboundscale

    @property
    def viewformat(self):
        return self.viewFormat

    @viewformat.setter
    def viewformat(self, viewformat):
        self.viewFormat = viewformat

    @property
    def httpquery(self):
        return self.httpQuery

    @httpquery.setter
    def httpquery(self, httpquery):
        self.httpQuery = httpquery


class Icon(Link): # --Document--
    """Defines an image associated with an Icon style or overlay.

    Arguments:
    href                -- string (default None)
    refreshmode         -- string from [RefreshMode] constants (default None)
    refreshinterval     -- float (default None)
    viewrefreshmode     -- string from [ViewRefreshMode] constants (default None)
    viewrefreshtime     -- float (default None)
    viewboundscale      -- float (default None)
    viewformat          -- string (default None)
    httpquery           -- string (default None)
    gxx                 -- int (default None)
    gxy                 -- int (default None)
    gxh                 -- int (default None)
    gxw                 -- int (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self,
                 gxx=None,
                 gxy=None,
                 gxw=None,
                 gxh=None,
                 **kwargs):
        super(Icon, self).__init__(**kwargs)
        self.gxx = gxx
        self.gxy = gxy
        self.gxw = gxw
        self.gxh = gxh



class ItemIcon(Kmlable): # --Document--
    """Defines an image associated with an Icon style or overlay.

    Arguments:
    href                -- string (default None)
    state               -- string from [State] constants (default None)

    Properties:
    Same as arguments.

    """

    def __init__(self, state=None, href=None):
        self.href = href
        self.state = state