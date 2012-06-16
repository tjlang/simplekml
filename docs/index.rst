.. simplekml documentation master file, created by
   sphinx-quickstart on Mon Apr 09 17:54:09 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Overview
========

simplekml is a python library for generating kml (or kmz). It was designed to alleviate the burden of having to study KML in order to achieve anything worthwhile with it. If you have a simple understanding of the structure of KML, then simplekml is easy to run with and create usable KML.

If you want get started right away head over to the table of Contents_ or straight to :ref:`usage` for a quick example.


Resources
=========

Visit simplekml's `homepage <http://code.google.com/p/simplekml/>`_ for news and updates.

For example code with corresponding KML download the `samples <http://simplekml.googlecode.com/hg/samples/SamplesLink.kml>`_ file. This file is simply a network link. When examples and tutorials are updated the updates will reflect in the sample file, so you do not have to download it every time something new is added to the documentation.

For discussions, questions, comments or requests visit the `simplekml Google group <https://groups.google.com/forum/?fromgroups#!forum/simplekml>`_

Be sure to check out the `KML Reference <http://code.google.com/apis/kml/documentation/kmlreference.html>`_ as published by Google for a good understanding of what KML is capable of. simplekml implements everything found in the KML Reference, and all properties and arguments are named exactly the same as in the KML Reference except special characters are dropped and everything is lower case (for example the colon in all the gx names are dropped and the name is converted to lowercase, gx:TimeSpan becomes gxtimespan)


Contents
========

.. toctree::
   :maxdepth: 3

   usage
   styling
   reference    
   tutorials



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
