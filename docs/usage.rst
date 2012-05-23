Usage
=====

Overview
--------

With simplekml everything starts with creating an instance of the :class:`simplekml.Kml` class: `kml = simplekml.Kml()`. The compilation of the KML file will be done through this class. The base feature attached to this class is a document, all arguments passed to the class on creation are the same as that of a :class:`simplekml.Document`. To change any properties after creation you can do so through the :func:`simplekml.Kml.document` property (eg. `kml.document.name = "Test"`).

To create a fully fledged KML document a document tree is created via calls to various commands like `kml.newpoint()`. These calls build up a tree which will be converted into KML when a call to `kml.save()`, `kml.savekmz()` or `kml.kml()` is made. This tree is generated in the background and does not need direct manipulation. If there is something that needs to be removed from the tree, simply set it to `None`. This is useful to prevent an image from being displayed for a point. By default a point has the image of a yellow push pin, but if you want to remove it you have to do this: `pnt.icon.href = None`. This removes the href from the icon, thus nothing will be displayed in google earth, except the points text.

Quick Example
-------------

Here is a quick example to get you started::

    import simplekml
    kml = simplekml.Kml()
    kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])  # lon, lat, optional height
    kml.save("botanicalgarden.kml")

Creating a KML document
-----------------------

To create a KML document you just have to import simplekml and then create an instance of :class:`simplekml.Kml`. Doing this will create a KML 'file' in memory and assign a :class:`simplekml.Document` as the main feature::

    import simplekml
    kml = simplekml.Kml()

Saving a KML document
---------------------

Simply call `kml.save("pathtomyfile.kml")` passing a path to the file you want to create. Alternatively you can call `kml.savekmz("pathtomyfile.kmz")` to save the KML as a KMZ, or even `kml.kml()` to get the KML as a string. See :func:`simplekml.Kml.save`, :func:`simplekml.Kml.savekmz` and :func:`simplekml.Kml.kml` for more details.

Creating a Point
----------------

A Point is a geographic location defined by longitude, latitude, and altitude.

.. note::

    All coordinates in simplekml are in the order longitude, latitude and then an optional height.

Creating a :class:`simplekml.Point` is quite simple and has been done in the section above. Once you have your :class:`simplekml.Kml` object you have to ask it to create a new :class:`simplekml.Point` for you by calling :func:`simplekml.Kml.newpoint`. If you call :func:`simplekml.Kml.newpoint` without any parameters a :class:`simplekml.Point` is created at 0.0, 0.0 with no name. You can later change the name and location (among other things) by changing the attributes of the :class:`simplekml.Point` instance that was returned to you by calling :func:`simplekml.Kml.newpoint`. Passing parameters to :func:`simplekml.Kml.newpoint` may be more convenient. All the attributes have to be set like so: `attributename=value`. See :class:`simplekml.Point` for a list of possible parameters and attributes.

Here is an example::

    pnt = kml.newpoint(name="Kirstenbosch", description="A botanical Garden", 
                       coords=[(18.432314,-33.988862)])  # lon, lat optional height

The values of the above parameters can be changed later by directly assigning to them::

    pnt.name = "Tree"
    pnt.description = "A big plant."


Creating a LineString
---------------------
A Linestring is a connected set of line segments.

A :class:`simplekml.LineString` is created in a similar manner to a :class:`simplekml.Point`, except you can have more than one coordinate. Just call :func:`simplekml.Kml.newlinestring`. See :class:`simplekml.LineString` for a list of possible parameters and attributes.

Here is an example::

    lin = kml.newlinestring(name="Pathway", description="A pathway in Kirstenbosch", 
                            coords=[(18.43312,-33.98924), (18.43224,-33.98914),
                                    (18.43144,-33.98911), (18.43095,-33.98904)])

Creating a Polygon
------------------

A Polygon is defined by an outer boundary and/or an inner boundary.

A :class:`simplekml.Polygon` is created in a similar manner to a :class:`simplekml.LineString`, except there is no coordinate parameter. Just call :func:`simplekml.Kml.newpolygon`. The coordinate parameter has been replaced with two others, :func:`simplekml.Polygon.outerboundaryis` and :func:`simplekml.Polygon.innerboundaryis`. The outer and inner boundaries describe the outside of the :class:`simplekml.Polygon` and an inner opening. You pass a list of tuples to these parameters, as if it were a coordinate list. See :class:`simplekml.Polygon` for a list of possible parameters and attributes.

Here is an example::

    pol = kml.newpolygon(name="Atrium Garden",
                         outerboundaryis=[(18.43348,-33.98985), (18.43387,-33.99004),
                                          (18.43410,-33.98972), (18.43371,-33.98952),
                                          (18.43348,-33.98985)],
                         innerboundaryis=[(18.43360,-33.98982), (18.43386,-33.98995),
                                          (18.43401,-33.98974), (18.43376,-33.98962),
                                          (18.43360,-33.98982)])

