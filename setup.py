from distutils.core import setup

setup(
    name = 'simplekml',
    packages = ['simplekml'],
    version = '0.8.2',
    description = 'A Simple KML creator',
    author='Kyle Lancaster',
    author_email='kyle.lan@gmail.com',
    url='http://code.google.com/p/simplekml/',
    license='GNU General Public License',
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.0',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Topic :: Scientific/Engineering :: GIS',
            'Topic :: Software Development :: Libraries :: Python Modules'
          ],
    long_description="""
simplekml is a python package which enables you to generate KML with as little effort as possible.

At the time of making this package nothing was available (at least I could not find anything) that could create KML files easily. You needed a lot of bloated code to even create a simple point. This is understandable because the KML standard is quite extensive, but what if you just work with the simple elements of KML like Document, Folder, Point, LineString and Polygon? This package supports those elements and more (MultiGeometry, Overlays, NetworkLinks, Models, Track and MultiTrack) with advanced styling. This makes creating a KML file containing a point as simple as::

    import simplekml
    kml = simplekml.Kml()
    kml.newpoint(name="Kirstenbosch", coords=[(18.432314,-33.988862)])
    kml.save("botanicalgarden.kml")

Please take note that this project is in its early stages. Everything seems to work, but bugs may crop up. If you would please test it and let me know if there are bugs, it would be appreciated.

See the Wiki_ for usage and reference.

.. _Wiki: http://code.google.com/p/simplekml/wiki/Welcome?tm=6

"""

)