# -*- coding: utf-8 -*-
"""
/***************************************************************************
 task_init
                                 A QGIS plugin
 task_handling
                             -------------------
        begin                : 2015-03-16
        copyright            : (C) 2015 by pyordan
        email                : pyordan@me
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
    """Load task_init class from file task_init.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .task_module import task_init
    return task_init(iface)
