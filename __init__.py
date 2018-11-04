# -*- coding: utf-8 -*-
"""
/***************************************************************************
 osm2pgrouting4qgis
                                 A QGIS plugin
 Automatically builds a pgRouting-compatible layer in a PostGIS database
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-11-03
        copyright            : (C) 2018 by Isaac Boates
        email                : iboates@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load osm2pgrouting4qgis class from file osm2pgrouting4qgis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .osm2pgrouting4qgis import osm2pgrouting4qgis
    return osm2pgrouting4qgis(iface)