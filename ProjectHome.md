**simplekml** is a python package which enables you to generate KML with as little effort as possible.

At the time of making this package nothing was available (at least I could not find anything) that could create KML files easily. You needed a lot of bloated code to even create a simple point. This is understandable because the KML standard is quite extensive, but what if you just want to quickly display points, linestrings, polygons, etc? Well, simplekml makes this very easy:

```
import simplekml
kml = simplekml.Kml()
kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])
kml.save("botanicalgarden.kml")
```

Download the latest file on [PyPi](https://pypi.python.org/pypi/simplekml/).

Please report any bugs under [issues](http://code.google.com/p/simplekml/issues/list).
See the [simplekml.readthedocs.org](http://simplekml.readthedocs.org) for usage and reference.

Report any errors in the documentation under [discussions](http://groups.google.com/group/simplekml), as well as general discussions.

For samples download the [samples](http://simplekml.googlecode.com/hg/samples/SamplesLink.kml) kml file.


---

# Roadmap #
  * ~~Enable saving to KMZ~~ - Implemented April 7, 2011
  * ~~Add BallonStyle and ListStyle~~ - Implemented April 11, 2011
  * ~~Add StyleMap~~ - Implemented April 20, 2011
  * ~~Add MultiGeometry~~ - Implemented April 22, 2011
  * ~~Add Overlays~~ - Implemented May 4, 2011
  * ~~Add TimePrimitive~~ - Implemented May 4, 2011
  * ~~Add NetworkLink and Model~~ - Implemented June 3, 2011
  * ~~Add gx:Track and gx:MultiTrack~~ - Implemented October 8, 2011
  * ~~Add gx:TourPrimitive, gx:Tour and gx:PlayList~~ - Implemented April 15, 2012
  * ~~Bug fixes and release 1.0.0~~ - Implemented July 24, 2012


---


# News #

### 08 February 2015 ###
simplekml 1.2.7 released. A bug fix release. http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs  for more information.


### 08 February 2015 ###
simplekml 1.2.6 released. A bug fix release. http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs  for more information.


### 12 December 2014 ###
simplekml 1.2.5 released. A bug fix release. http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs  for more information.


### 28 November 2014 ###
simplekml 1.2.4 released. A bug fix release. http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs  for more information.

### 26 October 2013 ###
simplekml 1.2.3 released. A bug fix release. http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs for more information. Also updated the samples kml with and example of gx:Track with a model. Also, removed the downloads section on this site, so for the latest release please go to [PyPi](https://pypi.python.org/pypi/simplekml/) to download it.

### 07 June 2013 ###
simplekml 1.2.2 released. A bug fix release. http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs for more information.

### 16 December 2012 ###
simplekml 1.2.1 released. A bug fix release. http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs for more information.

### 03 December 2012 ###
simplekml 1.2.0 released. Please see the http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs for more information.

### 17 September 2012 ###
simplekml 1.1.2 released. A bug fix release. There was a major problem with version 1.1.1 that has now been fixed.

### 16 September 2012 ###
simplekml 1.1.1 released! Please see the http://simplekml.readthedocs.org/en/latest/releasehistory.html on ReadTheDocs for more information.

### 09 August 2012 ###
simplekml 1.1.0 released! Please see the [release history](http://simplekml.readthedocs.org/en/latest/releasehistory.html#simplekml-1-1-0-09-august-2012) on ReadTheDocs for more information.

### 24 July 2012 ###
simplekml 1.0.0 released! Major release! Some bugs were fixed: GxLatLonBox coordinates not displaying correctly and TimeSpan/TimeStamp had an extra tag. Type checking added for simplekml classes to help avoid mistakes. Also a lot of documentation was added to the source and [ReadTheDocs](http://simplekml.readthedocs.org/en/latest/index.html)

### 21 June 2012 ###
simplekml 0.9.3 released. Another bug fix release. simplkml was not working on Python 3, this release fixes that. Sorry for releasing versions so close together, but this fixes a crippling bug in Python 3. Thanks for the bug reports.

### 16 June 2012 ###
simplekml 0.9.2 released!  This is a bug fix release. One or two bugs were fixed as well as added a read only id property to all features that can have an id (mainly to be used with touring). Some more tutorials have been added to the [documentation](http://simplekml.readthedocs.org/en/latest/index.html).

Lastly, you can now download a [samples](http://simplekml.googlecode.com/hg/samples/SamplesLink.kml) kml file which is is simply a network link. When examples and tutorials are updated the updates will reflect in the sample file, so you do not have to download it every time something new is added to the documentation. Make sure to click on the links in Google Earth's table of contents for the source code that generated the KML.

### 02 June 2012 ###
simplekml 0.9.1 released! This is a bug fix release. GxTour and associates had many bugs, which have now been fixed. Also, GxFlyToMode was incorrectly named and now has been renamed to GxFlyTo. There is now a touring tutorial on [readthedocs](http://simplekml.readthedocs.org/en/latest/tut_tours.html).

### 15 April 2012 ###
simplekml 0.9.0 released! This release implements everything found in the KML Reference including Tours! Not only that, thanks to [tlaurinolli](http://code.google.com/p/simplekml/issues/detail?id=15) simplekml is much much faster, thanks! Also, simplekml has new documentation at [readthedocs](http://simplekml.readthedocs.org). This means that I have retired the [wiki](http://code.google.com/p/simplekml/wiki/Welcome?tm=6), so please use the [issue tracker](http://code.google.com/p/simplekml/issues/list) to report any defects in the code and the [Google Group](http://groups.google.com/group/simplekml) for problems in the documentation, or just general discussions.

If you would like to write any tutorials, please do so, the tutorials section of the documentation is a little lacking. You can email them to me or post it on the [discussions](http://groups.google.com/group/simplekml).

simplekml will remain at release 0.9 until the end of June where release 1.0 will be released. In the mean time, any issues or bug fixes will be welcome, so that simplekml can be patched before release 1.0


### 20 February 2012 ###
simplekml 0.8.2 released! This is a bug fix release. `extrude` attribute added to GxTrack constructor. Made `name` optional for Schema. Thanks for the bug reports!


### 18 December 2011 ###
simplekml 0.8.1 released! This is a bug fix release. Unicode support for Python 3 was broken, now fixed. Also using Unicode and saving to a KMZ was broken for Python 2, now fixed (thanks for the patch).

### 8 October 2011 ###
simplekml 0.8.0 released! ExtendedData, gx:Track and gx:MultiTrack added. Fixed saving to unicode crashes (thanks for the patches!). Removed default values, so less KML is generated, but still has the same effect. Also, check out the samples, they show you how to use extended data and tracks.

### 28 July 2011 ###
simplekml 0.7.3 released! Another bug fix release. Saving to kmz was broken in the previous version. Also, the altitude was not interpreted correctly for linestrings and polygons, if the altitude was anything but 0.0 then it would be interpreted as a latitude or longitude. These have been fixed.

### 2 July 2011 ###
simplekml 0.7.2 released! Another bug fix release. There was a problem where the same style would be generated over and over again if it was assigned to multiple features, that has been corrected. Also, the CDATA element was unusable because of the way the text was automatically escaped. You can now set whether the text is escaped of not (not if you want to use the CDATA element) by going `kml = Kml(); kml.parsetext(False)`

### 16 June 2011 ###
Documentation has had an overhaul. Documentation has been added throughout the source code, so now using introspection should be a little easier, as well as, having to rely less on the KML reference. The reference on the [Wiki](http://code.google.com/p/simplekml/wiki/Welcome?tm=6) has also had on overhaul. If anyone notices anything strange, please let me know. The reference is auto generated from the source code, so hopefully nothing has been missed.

### 7 June 2011 ###
simplekml 0.7.1 released! This is a bug fix release. Model now works correctly. The way the KML was formatted had the potential to affect the usage of xml.dom.minidom negatively if simplekml was used inside a program that made use of xml.dom.minidom, this has been corrected (thanks for the patch!).

### 3 June 2011 ###
simplekml 0.7.0 released, with Python 3 support! simplekml now works with Python 2.6 to 3.2 . NetworkLink and Model have been added. Also, the KML that is generated is compatible with Google Maps (thanks for the patches!) and you can pass `False` to `save()`, `samekmz()` and `kml()` to get unformatted kml (basically one long line of KML).

### 20 May 2011 ###
simplekml 0.6.2 released! This fixed a couple of bugs (sorry if they cause you any inconvenience). The bugs fixed were:
  * LatLonBox was missing the direction properties
  * You could not assign a [Camera](Camera.md) or LookAt to any feature
  * Some "gx:"s were not working properly
  * ListStyle was broken
  * HotSpot was broken
  * Any others I have already forgotten about...

### 18 May 2011 ###
simplekml 0.6.1 released! Bug fixed where all Icons would be set to the last Icon supplied, so all imaged would be the same (thanks for the bug reports and supplied patches!). ~~The way kml is saved also changed, so technically simplekml should be compatible with Python 2.4 and 2.5, but no testing has been done (again, thanks for the submitted patch~~). Also, the core code has had an overhaul. It has been cleaned up, so that when you use the dir() function for introspection (or use an IDE for auto-completion) the "private" variables and methods are hidden or start with an underscore, as per the python styling guide. Please inform me of any bugs that may have cropped up, it was a major change to the code. Finally a kml() method was added to the Kml class. It basically returns the generated KML as a string instead of saving it to a file (useful for serving KML from a server).

### 4 May 2011 ###
simplekml 0.6.0 released! Added Overlays (GroundOverlay, ScreenOverlay and PhotoOverlay) and added a LOT of attributes for all feature types and their dependencies. All implemented classes should be about 90% inline with Google's KML reference. TimePrimitives were also added. Very basic implementation, hopefully in future the time attributes will accept python datetime instances (but not yet).

### 22 April 2011 ###
simplekml 0.5.0 released! Added MultiGeometry and extended the [Color](Color.md) class with an alpha value changer.

### 20 April 2011 ###
The reference documentation has been updated! Next step it to provide more styling information, especially for ListStyle, BalloonStyle and StyleMap. Also, the [Color](Color.md) class.

### 19 April 2011 ###
simplekml 0.4.0 released! Added StyleMap for all Geometry elements. Also added a new [Color](Color.md) class that can convert RGB, hex and hex with alpha into KML hex values. The color class also comes with all the HTML and CSS color constants (named colors). (Please note that the documentation on the wiki has not been updated since V0.1, but hopefully it will be soon!)

### 11 April 2011 ###
simplekml 0.3.0 released! Fixed bug for points "altitudemode". Added BalloonStyle and ListStyle. (Please note that the documentation on the wiki has not been updated since V0.1)

### 7 April 2011 ###
simplekml 0.2.0 released! Fixed bug where you were unable to assign to "altitudemode". Added support for HTML in "name" and "description" fields. simplekml can now save to KMZ.

### 24 March 2011 ###
simplekml 0.1.1 released! Fixed bug that now allows you to have multiple inner boundaries for a Polygon.

### 20 February 2011 ###
simplekml 0.1 released!