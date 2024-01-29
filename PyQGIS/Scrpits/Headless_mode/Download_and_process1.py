import os
from qgis.core import QgsApplication

qgs = QgsApplication([], False)
qgs.initQgis()

import processing
from processing.core.Processing import Processing
Processing.initialize()

extracted_points = processing.runAndLoadResults("native:extractbylocation", 
{'INPUT':'/Users/nilay/Downloads/latest.zip',
'PREDICATE':[0],
'INTERSECT':'/Users/nilay/NESAC/Training/AdvancedQGIS/PyQGIS/Data/IndiaBoundary.shp',
'OUTPUT':'TEMPORARY_OUTPUT'})

fixed_vector_layer = extracted_points['OUTPUT']

processing.run("native:printlayouttoimage", 
{'LAYOUT':'print',
'LAYERS':[fixed_vector_layer,
'/Users/nilay/NESAC/Training/AdvancedQGIS/PyQGIS/Data/IndiaBoundary.shp'],
'DPI':None,
'GEOREFERENCE':True,
'INCLUDE_METADATA':True,
'ANTIALIAS':True,
'OUTPUT':'/Users/nilay/Downloads/print8.png'})

print('Output Layer Created', output_path)
qgs.exitQgis()