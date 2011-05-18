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

class TimeSpan(Kmlable): # --Document--
    """Represents an extent in time bounded by begin and end dates.

    Arguments:
    begin               -- string (default None)
    end                 -- string (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, begin=None, end=None):
        super(TimeSpan, self).__init__()
        self._kml["begin"] = begin
        self._kml["end"] = end

    @property
    def begin(self):
        return self._kml['begin']

    @begin.setter
    def begin(self, begin):
        self._kml['begin'] = begin

    @property
    def end(self):
        return self._kml['end']

    @end.setter
    def end(self, end):
        self._kml['end'] = end


class GxTimeSpan(TimeSpan): # --Document--
    """A copy of the [TimeSpan] element, in the extension namespace.

    Arguments:
    begin               -- string (default None)
    end                 -- string (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, **kwargs):
        super(GxTimeSpan, self).__init__(**kwargs)


class TimeStamp(Kmlable): # --Document--
    """Represents a single moment in time.

    Arguments:
    when                -- string (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, when=None):
        super(TimeStamp, self).__init__()
        self._kml["when"] = when

    @property
    def when(self):
        return self._kml['when']

    @when.setter
    def when(self, when):
        self._kml['when'] = when


class GxTimeStamp(TimeStamp): # --Document--
    """A copy of the [TimeStamp] element, in the extension namespace.

    Arguments:
    when                -- string (default None)

    Properties:
    Same as arguments.

    """
    def __init__(self, **kwargs):
        super(GxTimeStamp, self).__init__(**kwargs)