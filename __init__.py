# -*- coding: utf-8 -*-
def classFactory(iface):
    #loading of the task plugin onto the qgis and passing the qgis interface to the task_init class through iface object
    from .task_module import task_init
    return task_init(iface)
