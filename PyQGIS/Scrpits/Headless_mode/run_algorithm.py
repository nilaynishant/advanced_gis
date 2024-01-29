import os
from qgis.core import QgsApplication
#from Downloading_and_processing import Downloading_and_processing

qgs = QgsApplication([], False)
qgs.initQgis()

import processing
from processing.core.Processing import Processing
Processing.initialize()

provider = Downloading_and_processing

QgsApplication.ProcessingRegistry().addProvider(provider)
parameters={'inputlayer':'/Users/nilay/NESAC/Training/AdvancedQGIS/PyQGIS/Data/IndiaBoundary.shp',
                'native:extractbylocation_1:Output':'TEMPORARY_OUTPUT',
                'native:printlayouttoimage_1:output':'/Users/nilay/Downloads/print5.png'}

processing.run("model:Downloading_and_processing", parameters)

print('Output Layer Created')
qgs.exitQgis()